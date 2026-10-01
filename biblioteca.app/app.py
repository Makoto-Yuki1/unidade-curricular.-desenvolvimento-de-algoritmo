from __future__ import annotations

import sqlite3
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "bibliotecadb"

app = Flask(__name__, template_folder=str(BASE_DIR / "template"), static_folder=str(BASE_DIR / "static"))
app.config["SECRET_KEY"] = "biblioteca-secret-key"


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_db_connection() as conn:
        tabela_autores = {row[1] for row in conn.execute("PRAGMA table_info(autores)").fetchall()}
        tabela_categorias = {row[1] for row in conn.execute("PRAGMA table_info(categorias)").fetchall()}
        tabela_livros = {row[1] for row in conn.execute("PRAGMA table_info(livros)").fetchall()}

        required_autores = {"id", "nome"}
        required_categorias = {"id", "nome"}
        required_livros = {"id", "titulo", "isbn", "ano_publicacao", "autor_id", "categoria_id"}

        if tabela_autores and not required_autores.issubset(tabela_autores):
            conn.execute("DROP TABLE IF EXISTS autores")
        if tabela_categorias and not required_categorias.issubset(tabela_categorias):
            conn.execute("DROP TABLE IF EXISTS categorias")
        if tabela_livros and not required_livros.issubset(tabela_livros):
            conn.execute("DROP TABLE IF EXISTS livros")

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                isbn TEXT,
                ano_publicacao INTEGER,
                autor_id INTEGER,
                categoria_id INTEGER,
                FOREIGN KEY (autor_id) REFERENCES autores(id),
                FOREIGN KEY (categoria_id) REFERENCES categorias(id)
            )
            """
        )
        conn.commit()

        if conn.execute("SELECT COUNT(*) FROM autores").fetchone()[0] == 0:
            conn.executemany(
                "INSERT INTO autores (nome) VALUES (?)",
                [
                    ("Machado de Assis",),
                    ("Clarice Lispector",),
                    ("José de Alencar",),
                    ("Cecília Meireles",),
                ],
            )

        if conn.execute("SELECT COUNT(*) FROM categorias").fetchone()[0] == 0:
            conn.executemany(
                "INSERT INTO categorias (nome) VALUES (?)",
                [
                    ("Romance",),
                    ("Poesia",),
                    ("Literatura Infantil",),
                    ("Histórico",),
                ],
            )

        if conn.execute("SELECT COUNT(*) FROM livros").fetchone()[0] == 0:
            conn.execute(
                """
                INSERT INTO livros (titulo, isbn, ano_publicacao, autor_id, categoria_id)
                VALUES
                    ('Memórias Póstumas de Brás Cubas', '978-85-359-0611-9', 1881, 1, 1),
                    ('A Hora da Estrela', '978-85-352-1900-0', 1977, 2, 2),
                    ('O Guarani', '978-85-211-0252-8', 1857, 3, 4),
                    ('Romanceiro da Inconfidência', '978-85-744-3644-4', 1940, 4, 3)
                """
            )

        conn.commit()


init_db()


def get_or_create_autor(nome: str) -> int:
    nome = nome.strip()
    if not nome:
        raise ValueError("O nome do autor é obrigatório.")

    with get_db_connection() as conn:
        autor = conn.execute("SELECT id FROM autores WHERE nome = ?", (nome,)).fetchone()
        if autor is not None:
            return autor["id"]

        cursor = conn.execute("INSERT INTO autores (nome) VALUES (?)", (nome,))
        return cursor.lastrowid


def get_or_create_categoria(nome: str) -> int:
    nome = nome.strip()
    if not nome:
        raise ValueError("A categoria é obrigatória.")

    with get_db_connection() as conn:
        categoria = conn.execute("SELECT id FROM categorias WHERE nome = ?", (nome,)).fetchone()
        if categoria is not None:
            return categoria["id"]

        cursor = conn.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))
        return cursor.lastrowid


@app.route("/")
def index():
    with get_db_connection() as conn:
        total_livros = conn.execute("SELECT COUNT(*) AS total FROM livros").fetchone()["total"]
        total_autores = conn.execute("SELECT COUNT(*) AS total FROM autores").fetchone()["total"]
        total_categorias = conn.execute("SELECT COUNT(*) AS total FROM categorias").fetchone()["total"]
        livros_recentes = conn.execute(
            """
            SELECT l.id, l.titulo, l.ano_publicacao, a.nome AS autor, c.nome AS categoria
            FROM livros l
            LEFT JOIN autores a ON a.id = l.autor_id
            LEFT JOIN categorias c ON c.id = l.categoria_id
            ORDER BY l.id DESC
            LIMIT 5
            """
        ).fetchall()

    return render_template(
        "index.html",
        total_livros=total_livros,
        total_autores=total_autores,
        total_categorias=total_categorias,
        livros_recentes=livros_recentes,
    )


@app.route("/livros", methods=["GET", "POST"])
def livros():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        isbn = request.form.get("isbn", "").strip()
        ano_publicacao = request.form.get("ano_publicacao", "").strip()
        autor_nome = request.form.get("autor", "").strip()
        categoria_nome = request.form.get("categoria", "").strip()

        if not titulo or not autor_nome or not categoria_nome:
            flash("Preencha os campos obrigatórios: título, autor e categoria.", "erro")
            return redirect(url_for("livros"))

        try:
            autor_id = get_or_create_autor(autor_nome)
            categoria_id = get_or_create_categoria(categoria_nome)
            with get_db_connection() as conn:
                conn.execute(
                    """
                    INSERT INTO livros (titulo, isbn, ano_publicacao, autor_id, categoria_id)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (titulo, isbn or None, int(ano_publicacao) if ano_publicacao else None, autor_id, categoria_id),
                )
                conn.commit()
            flash("Livro cadastrado com sucesso!", "sucesso")
        except ValueError as exc:
            flash(str(exc), "erro")

        return redirect(url_for("livros"))

    with get_db_connection() as conn:
        autores = conn.execute("SELECT id, nome FROM autores ORDER BY nome").fetchall()
        categorias = conn.execute("SELECT id, nome FROM categorias ORDER BY nome").fetchall()
        livros_cadastrados = conn.execute(
            """
            SELECT l.id, l.titulo, l.isbn, l.ano_publicacao, a.nome AS autor, c.nome AS categoria
            FROM livros l
            LEFT JOIN autores a ON a.id = l.autor_id
            LEFT JOIN categorias c ON c.id = l.categoria_id
            ORDER BY l.titulo
            """
        ).fetchall()

    return render_template("livros.html", autores=autores, categorias=categorias, livros=livros_cadastrados)


@app.route("/acervo")
def acervo():
    with get_db_connection() as conn:
        livros = conn.execute(
            """
            SELECT l.id, l.titulo, l.isbn, l.ano_publicacao, a.nome AS autor, c.nome AS categoria
            FROM livros l
            LEFT JOIN autores a ON a.id = l.autor_id
            LEFT JOIN categorias c ON c.id = l.categoria_id
            ORDER BY l.titulo
            """
        ).fetchall()

    return render_template("consultadeacervo.html", livros=livros)


@app.route("/autores")
def autores():
    with get_db_connection() as conn:
        autores_lista = conn.execute(
            """
            SELECT a.id, a.nome, COUNT(l.id) AS total_livros
            FROM autores a
            LEFT JOIN livros l ON l.autor_id = a.id
            GROUP BY a.id, a.nome
            ORDER BY a.nome
            """
        ).fetchall()

    return render_template("autores.html", autores=autores_lista)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
