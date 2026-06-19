from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for,
    request,
    flash
)


app = Flask(__name__)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar(): 
    tarefas = [
        {'id': 1, 'nome': 'brócolis','calorias': 10.00},
        {'id': 2, 'nome': 'picanha','calorias': 280.00},
        {'id': 3, 'nome': 'miojo SABOORRRR picanha','calorias': 150.00},
        {'id': 4, 'nome': 'macarrão prego','calorias': 200.00},
        {'id': 5, 'nome': 'feijão preto', 'calorias': 250.00},
        {'id': 6, 'nome': 'bixcoito maizena','calorias': 300.00}
    ]
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['GET', 'POST'])
def tarefas():
    if request.method == 'POST':

        session['arroz'] = request.form.POST('arroz')
        session['frango'] = request.form.POST('frango')

        return redirect(url_for('adicionar'))

    return render_template('index.html')


#agora para limpar o session, basta usar o método clear() do objeto session, como mostrado abaixo:

@app.route('/limpar', methods=['POST'])
def limpar():
    session.clear()
    if not session:
        flash('Sessão limpa com sucesso!, dia zerado!')
    return redirect(url_for('adicionar'))


if __name__ == '__main__':
    app.run(debug=True)