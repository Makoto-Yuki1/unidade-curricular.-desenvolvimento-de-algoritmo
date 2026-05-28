from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = 'sua_chave_secreta'

@app.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip().lower()
        
        if not nome:
            flash('o nome é obrigatório', 'erro')
        return redirect(url_for('cadastro'))
    
        if not email:
            flash('o email é obrigatório', 'erro')
        return redirect(url_for('cadastro'))
    
#tudo certo
        flash(f'bem-vindo, {nome}! cadastro realizado.', 'sucesso')
        return redirect(url_for('cadastro'))
    
        return render_template('cadastro.html')



