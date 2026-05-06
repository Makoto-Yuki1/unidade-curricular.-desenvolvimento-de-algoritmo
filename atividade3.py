from flask import Flask, render_template

app = Flask(__name__)

@app.route('/nomw', defaults={"nome":"usuário comum"})
@app.route('/nome/<nome>')
def dados(nome): 
  return f'olá, {nome}!'







if __name__ == '__main__':
    app.run()