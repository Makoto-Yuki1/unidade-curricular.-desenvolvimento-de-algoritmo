from flask import Flask, render_template, request

app = Flask(__name__)

app.route('/validação', methods=['POST'])
def cadastro():

    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    CPF = request.form.get('CPF', '').strip().title()
    telefone = request.form.get('telefone', '').strip().title().strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('.', '').replace('+', '')
    cidade = request.form.get('cidade', '').strip().title()
    idade = request.form.get('idade', '').strip().title()
    senha = request.form.get('senha', '').strip().title()
    nome = request.form.get('nome', '').strip().title()
    curso = request.form.get('curso', '').strip().title()
    email = request.form.get('email', '').strip().lower()

    CPF = request.form.get('CPF', '').strip().replace('.', '').replace('-', '')
    
    telefone = request.form.get('telefone', '').strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('.', '').replace('+', '')
    cidade = request.form.get('cidade', '').strip().title()

    erros = []
    
    if nome and email and CPF and telefone and cidade:
        return render_template('trabalho.html',
                            usuario_logado=True,
                            nome=nome, email=email, CPF=CPF, telefone=telefone, cidade=cidade)
    
    
    
    
    if not telefone.isdigit() or len(telefone) != 11:
        return render_template('trabalho.html',
                            usuario_logado=True,
                            erro="Telefone inválido (11 dígitos numéricos)",
                            nome=nome, email=email)

    if not nome or not email:
            return render_template('trabalho.html',
        usuario_logado=True,
        erro="Preencha todos os campos, abestalhado",
        nome=nome, email=email)

    if len(nome) != 8 or not CPF.isdigit():
        return render_template('trabalho.html',
                            usuario_logado=True,
                            erro="Nome inválido (8 caracteres)",
                            nome=nome, email=email)
    
    if len(CPF) != 11 or not CPF.isdigit():
        return render_template('trabalho.html',
                            usuario_logado=True,
                            erro="CPF inválido (11 dígitos numéricos)",
                            nome=nome, email=email)

if __name__ == "__main__":
    app.run(debug=True)