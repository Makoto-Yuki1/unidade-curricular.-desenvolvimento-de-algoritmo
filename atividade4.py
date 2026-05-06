from flask import Flask, render_template

app = Flask(__name__)



@app.route('/soma', defaults = {"n1": "0", "n2":"0" })
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
  resultado = n1+n2
  return str(resultado)

if __name__ == '__main__':
    app.run()
