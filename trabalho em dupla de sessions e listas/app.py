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
