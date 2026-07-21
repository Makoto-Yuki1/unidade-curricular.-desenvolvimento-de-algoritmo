from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"


def carregar_livros():
    """Lê o arquivo JSON e retorna uma lista de livros."""
    if not os.path.exists(ARQUIVO):
        return []
    
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_livros(lista_livros):
    """Salva a lista de livros no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista_livros,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def validar_livro(titulo, autor, ano, categoria, quantidade):
    """Valida os dados do livro."""
    erros = []
    
    if not titulo.strip():
        erros.append("Título é obrigatório.")
    if not autor.strip():
        erros.append("Autor é obrigatório.")
    if not ano.strip():
        erros.append("Ano é obrigatório.")
    elif not ano.isdigit():
        erros.append("Ano deve conter apenas números.")
    if not categoria.strip():
        erros.append("Categoria é obrigatória.")
    if not quantidade.strip():
        erros.append("Quantidade é obrigatória.")
    else:
        try:
            qtd = int(quantidade)
            if qtd <= 0:
                erros.append("Quantidade deve ser maior que zero.")
        except ValueError:
            erros.append("Quantidade deve ser um número inteiro.")
    
    return erros


@app.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor = request.form.get("autor", "").strip()
        ano = request.form.get("ano", "").strip()
        categoria = request.form.get("categoria", "").strip()
        quantidade = request.form.get("quantidade", "").strip()
        
        erros = validar_livro(titulo, autor, ano, categoria, quantidade)
        
        if not erros:
            livro = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "categoria": categoria,
                "quantidade": int(quantidade)
            }
            
            livros = carregar_livros()
            livros.append(livro)
            salvar_livros(livros)
            
            return redirect(url_for("listar"))
        else:
            return render_template("cadastro.html", erros=erros)
    
    return render_template("cadastro.html", erros=[])


@app.route("/livros")
def listar():
    livros = carregar_livros()
    return render_template("livros.html", livros=livros)


@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    livro_encontrado = None
    mensagem = ""
    
    if request.method == "POST":
        titulo_busca = request.form.get("titulo", "").strip().lower()
        
        if not titulo_busca:
            mensagem = "Digite um título para buscar."
        else:
            livros = carregar_livros()
            for livro in livros:
                if livro["titulo"].lower() == titulo_busca:
                    livro_encontrado = livro
                    
            
            if not livro_encontrado:
                mensagem = "Livro não encontrado."
    
    return render_template("buscar.html", livro=livro_encontrado, mensagem=mensagem)


@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):
    livros = carregar_livros()
    
    if indice < 0 or indice >= len(livros):
        return redirect(url_for("listar"))
    
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor = request.form.get("autor", "").strip()
        ano = request.form.get("ano", "").strip()
        categoria = request.form.get("categoria", "").strip()
        quantidade = request.form.get("quantidade", "").strip()
        
        erros = validar_livro(titulo, autor, ano, categoria, quantidade)
        
        if not erros:
            livros[indice] = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "categoria": categoria,
                "quantidade": int(quantidade)
            }
            salvar_livros(livros)
            return redirect(url_for("listar"))
        else:
            livro = livros[indice]
            return render_template("editar.html", livro=livro, indice=indice, erros=erros)
    
    livro = livros[indice]
    return render_template("editar.html", livro=livro, indice=indice, erros=[])


@app.route("/excluir/<int:indice>")
def excluir(indice):
    livros = carregar_livros()
    
    if 0 <= indice < len(livros):
        livros.pop(indice)
        salvar_livros(livros)
    
    return redirect(url_for("listar"))


if __name__ == "__main__":
    app.run(debug=True)