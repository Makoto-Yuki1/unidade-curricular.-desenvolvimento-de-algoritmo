from flask import Flask, render_template, 
session, 
redirect, 
url_for, 
request, 
flash

app = Flask(__name__)
# Defina uma secret key segura em produção (aqui só um valor de exemplo)
app.secret_key = ("FLASK_SECRET_KEY")

@app.route('/')
def index():
    # Inicializa a lista de alimentos na sessão se não existir
    alimentos = session.get('alimentos', [])
    # Calcula o total de calorias
    total = sum(item.get('calorias', 0) for item in alimentos)
    return render_template('index.html', alimentos=alimentos, total=total)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome', '').strip()
    calorias_raw = request.form.get('calorias', '').strip()

    if not nome or not calorias_raw:
        flash('Preencha nome e calorias.')
        return redirect(url_for('index'))

    try:
        calorias = float(calorias_raw)
        if calorias < 0:
            raise ValueError()
    except ValueError:
        flash('Calorias inválidas. Use um número positivo.')
        return redirect(url_for('index'))

    # Recupera a lista, adiciona o novo alimento e reatribui na sessão
    alimentos = session.get('alimentos', [])
    alimentos.append({'nome': nome, 'calorias': calorias})
    session['alimentos'] = alimentos  # reatribuir garante que a sessão seja atualizada

    flash(f'{nome} adicionado ({calorias} kcal).')
    return redirect(url_for('index'))

@app.route('/zerar', methods=['GET'])
def zerar():
    session.pop('alimentos', None)  # remove apenas os alimentos; se quiser limpar tudo use session.clear()
    flash('Dia zerado — todas as anotações removidas.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
