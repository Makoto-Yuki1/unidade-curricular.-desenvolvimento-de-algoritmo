from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

app = Flask(__name__)
app.secret_key = "mude_para_uma_chave_secreta_diferente"

ARQUIVO = "cantinho.json"

DEFAULT_DADOS = {
    "nome": "Seu Nome",
    "senha": "1234",
    "cor_favorita": "Azul",
    "linguagem_favorita": "Python",
    "frase": "Sempre aprendendo e criando com carinho."
}


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return DEFAULT_DADOS.copy()

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)
            if not isinstance(dados, dict):
                return DEFAULT_DADOS.copy()
            return {**DEFAULT_DADOS, **dados}
        except json.JSONDecodeError:
            return DEFAULT_DADOS.copy()


@app.route("/", methods=["GET", "POST"])
def login():
    dados = carregar_dados()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        senha = request.form.get("senha", "").strip()

        if nome == dados["nome"] and senha == dados["senha"]:
            session["usuario_nome"] = nome
            session["visitas_cantinho"] = 0
            return redirect(url_for("painel"))

        flash("Nome ou senha inválidos. Tente novamente.")

    return render_template("login.html")


@app.route("/painel")
def painel():
    if "usuario_nome" not in session:
        flash("Você precisa estar logado para acessar o painel.")
        return redirect(url_for("login"))

    return render_template("painel.html", nome=session["usuario_nome"])


@app.route("/cantinho")
def cantinho():
    if "usuario_nome" not in session:
        flash("Acesse o login antes de entrar no seu cantinho.")
        return redirect(url_for("login"))

    dados = carregar_dados()
    visitas = session.get("visitas_cantinho", 0) + 1
    session["visitas_cantinho"] = visitas

    return render_template(
        "cantinho.html",
        nome=session["usuario_nome"],
        visitas=visitas,
        cor_favorita=dados["cor_favorita"],
        linguagem_favorita=dados["linguagem_favorita"],
        frase=dados["frase"]
    )


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da área privada.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
