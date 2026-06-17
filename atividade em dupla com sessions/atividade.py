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

app.config['SECRET_KEY'] = 'fã de drag/on ball 12345'
usuário = 'Júlio César'
senha = '676767676767 '

@app.route('/login', methods=['GET', 'POST'])#post serve para enviar os dados do formulário, get para acessar a página de login
def login():
  if request.method == 'POST':
    usuário = request.form['usuário']
    senha = request.form['senha']
    if usuário == app.config.get('usuário') and senha == app.config.get('senha'):
      session.permanent = True
      session['usuário'] = usuário
      flash('Login bem-sucedido!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Usuário ou senha incorretos. Tente novamente.', 'danger')
  return render_template('login.html')









































if __name__ == '__main__':
    app.run(debug=True)