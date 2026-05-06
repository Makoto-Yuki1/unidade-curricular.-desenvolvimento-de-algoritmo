from flask import Flask, render_template

app = Flask(__name__)


@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return 'o produto é:{nome}, e seu preço é: {preco}|'
   




if __name__ == '__main__':
    app.run()