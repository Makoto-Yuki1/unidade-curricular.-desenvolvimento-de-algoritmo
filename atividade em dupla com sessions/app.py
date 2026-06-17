from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Obrigatório para usar sessions
app.secret_key = "segredo123"

# Usuário e senha fixos
USUARIO = "admin"
SENHA = "1234"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    erro = ""

    if request.method == "POST":

        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == USUARIO and senha == SENHA:
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))

        erro = "Usuário ou senha inválidos."

    return render_template("login.html", erro=erro)


@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        usuario=session["usuario"]
    )


@app.route("/logout")
def logout():

    session.pop("usuario", None)

    return redirect(url_for("login"))


# Rota extra solicitada no enunciado
@app.route("/rotalogin")
def rotalogin():
    return """
    <h1>Rota Login Extra</h1>
    <p>Esta rota foi adicionada conforme solicitado no enunciado.</p>
    <a href="/login">Ir para Login</a>
    """


if __name__ == "__main__":
    app.run(debug=True)