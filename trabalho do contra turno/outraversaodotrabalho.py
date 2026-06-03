import re
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash # Importante para salvar senhas reais

app = Flask(__name__)

@app.route('/validacao', methods=['POST'])
def cadastro():
 
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    CPF = request.form.get('CPF', '').strip().replace('.', '').replace('-', '')
    telefone = request.form.get('telefone', '').strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('.', '').replace('+', '')
    cidade = request.form.get('cidade', '').strip().title()
    
    
    idade_str = request.form.get('idade', '').strip()
    senha = request.form.get('senha', '') 
    curso = request.form.get('curso', '').strip().title()

    erros = []

    
    if not nome:
        erros.append("O campo 'Nome' é obrigatório.")
    elif len(nome) < 3:
        erros.append("O nome deve ter pelo menos 3 caracteres.")
    elif not all(c.isalpha() or c.isspace() for c in nome):
        erros.append("O nome deve conter apenas letras.")

    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not email:
        erros.append("O campo 'E-mail' é obrigatório.")
    elif not re.match(padrao_email, email):
        erros.append("Formato de e-mail inválido.")

    if not CPF:
        erros.append("O campo 'CPF' é obrigatório.")
    elif len(CPF) != 11 or not CPF.isdigit():
        erros.append("O CPF deve conter exatamente 11 dígitos numéricos.")

    if not telefone:
        erros.append("O campo 'Telefone' é obrigatório.")
    elif not telefone.isdigit() or len(telefone) not in [ 11]:
        erros.append("Telefone inválido. Inclua o DDD e apenas números (11 dígitos).")

    if not cidade:
        erros.append("O campo 'Cidade' é obrigatório.")
    elif len(cidade) < 1:
        erros.append("Nome da cidade inválido.")

    if not idade_str:
        erros.append("O campo 'Idade' é obrigatório.")
    elif not idade_str.isdigit():
        erros.append("A idade deve ser um número válido.")
    else:
        idade = int(idade_str) 
        if idade < 1 or idade > 130: 
            erros.append("A idade deve ser entre 1 e 130 anos.")


    if not senha:
        erros.append("O campo 'Senha' é obrigatório.")
    elif len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
    
    if not curso:
        erros.append("O campo 'Curso' é obrigatório.")
    elif len(curso) < 3:
        erros.append("O nome do curso deve ter pelo menos 3 caracteres.")

    if erros:
        return ({"sucesso": False, "erros": erros}), 400


    return ({"sucesso": True, "mensagem": "Cadastro validado com sucesso!"}), 