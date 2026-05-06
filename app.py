from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
   return render_template('jjk.html')

@app.route('/contato')
def contato():
    nome = "Gaby"
    return render_template('jjk.html', title = 'página inicial',nome = nome )


@app.route('/usuario')
def usuario():
 usuario = {'nome', 'Gaby', 'email:' 'cortezyasmin@gmail.com'}
 return render_template('jjk.html', title = 'página inicial', usuario = usuario )

@app.route('/dados', defaults={"nome":"usuário comum"})
@app.route('/dados/<nome>')
def dados(nome): 
  return f'olá, {nome}!'


@app.route('/semestre/<int:x>')
def semestre(x):
   return 'estamos no semestre' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
 return 'você pagou:' + str(valor)

@app.route('/arearestrita/<id>')
def arearestrita(valor):
 if (valor == 1):
  return 'você está livre' 
 else:
  return 'você foi bloqueado'

if __name__ == '__main__':
    app.run()