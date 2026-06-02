from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

   mensagem = ""
if request.method == "POST": 
    nickname = request.form.get("nickname", "").strip() 
jogo = request.form.get("jogo", "")
email = request.form.get("email", "").strip() 
if len(nickname) < 4 or jogo == "" or email == "": 
    mensagem = "Preencha todos os campos obrigatórios." 
 
else: mensagem = "Inscrição realizada com sucesso!" 


return render_template("index.html", mensagem=mensagem) 
 if __name__ == "__main__": app.run(debug=True)