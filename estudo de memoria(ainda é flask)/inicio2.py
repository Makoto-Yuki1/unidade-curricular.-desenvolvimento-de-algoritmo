from flask import (Flask, render_template, request, make_response, redirect, url_for)

app = Flask(__name__)



@app.route('/')
def inicio():

    tema = request.cookies.get('tema', 'claro')
    return render_template(
       'inicio.html',
       tema=tema
   )

@app.route('/tema/<escolha>')
def trocar_tema(escolha):

    if escolha not in ['claro', 'escuro']:
        escolha = 'claro'  
    
    resposta = make_response(
        redirect(url_for('inicio'))
    )

       
    resposta.set_cookie(
      'tema',
      escolha,
      max_age= 60*60*24*30
    )
     
    return resposta


 
@app.route('/')
def inicio():


   nome = request.cookies.get('nome', 'Visitante', '')
   return render_template(
       'inicio.html',
       nome=nome
    )

@app.route('/salvar-nome/', methods=['POST'])
def salvar_nome():

    visitante = request.form.get('nome', '').strip().title()#para retirar os espaços e colocar a primeira letra maiúscula
    
    resposta = make_response(
        redirect(url_for('inicio'))
    )

    resposta.set_cookie(
        'nome',
        visitante,
        max_age= 60*60*24*30
    )

    if visitante:
        return f'Bem-vindo, {visitante}!'
    else:
        return 'Cookie de usuário não encontrado.'
    return resposta


 
@app.route('/')
def inicio():


   email = request.cookies.get('email','')
   return render_template(
       'inicio.html',
      email=email
    )

@app.route('/salvar-email/', methods=['POST'])
def salvar_email():

    email = request.form.get('email', '').strip().lower()

    resposta = make_response(
        redirect(url_for('inicio'))
    )

    resposta.set_cookie(
        'email',
        email,
        max_age= 60*60*24*30
    )

    return resposta

























































if __name__ == '__main__':
    app.run(debug=True)































