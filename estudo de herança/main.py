from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/formregistrar')
def login():
    return render_template('registrar.html')




@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    email = request.form.get
    estado = request.form['estado']
    formação = request.form['formacao']
    modalidade = request.form.getlist('modalidades')
    senha = request.form.get('senha')
    return "{} e {} e {} e {} e {}">format(nome, email, estado, formação, modalidade)

if "senha" == 1234:
 print("Usuário registrado com sucesso")

else:
 print("As senhas não conferem")

if __name__ == '__main__':
    app.run(debug=True)



