from flask import Flask, render_template

app = Flask(__name__)



@app.route('/idade/<nome>/<int:idade>')
def idade(idade):
    if idade >= 18:
     return 'você é de maior'
    else:
        return 'você é de menor'

if __name__ == '__main__':
    app.run()
