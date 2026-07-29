from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import Flask, render_template

@app.route('/')
def cadastro():
 senha = ""
 nome = ""
 senha_hash = generate_password_hash(senha)
 nome_hash = generate_password_hash(nome)

print("\nHash gerado:")
print(senha_hash)

tentativa = input("\ndigite novamente a senha:")

if check_password_hash(hash_senha, tentativa):
    print("Senha correta!")
else:
    print("senha incorreta!")
   
 return render_template('cadastro.html')

@app.route('/login')
def login():
    
 if request.method =="POST"
  nome = request.form["nome"]
  senha = request.form["senha"]
 
  if check_password_hash(hash_nome, tentativa):
    print("nome correto!")
  else:
    print("nome incorreto!")
 
  if check_password_hash(hash_senha, tentativa):
    print("Senha correta!")
  else:
    print("senha incorreta!")

 return render_template('login.html', mensagem = mensagem)

if __name__ == '__main__':
    app.run(debug=True)




