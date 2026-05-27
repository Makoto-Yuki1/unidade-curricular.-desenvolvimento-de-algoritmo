from flask import Flask, render_template

app = Flask(__name__)

@app.route("/inicio")
def inicio():
 return render_template("inicio.html")

@app.route("/cursos")
def cursos():
  return render_template("cursos.html")

@app.route("/professores")
def professores():
  return render_template("professores.html")


if __name__== "__main__":
  app.run(debug=True)