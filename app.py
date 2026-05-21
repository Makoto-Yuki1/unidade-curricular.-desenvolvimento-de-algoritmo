from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/autenticar', methods = ['GET'])
def autenticar():
     nome= request.args.get('nome')
     curso= request.args.get('nome')
     cidade = request.args.get('cidade')
     idade = request.args.get('idade')
     return "nome {} e curso {} e cidade {} e idade {}".format(nome, curso, cidade, idade)


if __name__ == '__main__':
    app.run(debug=True)
