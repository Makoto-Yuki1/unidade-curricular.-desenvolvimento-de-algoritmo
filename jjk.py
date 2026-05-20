from flask import Flask, render_template

app = Flask(__name__)


@app.route('/FoodExpress/<menu>')
def FoodExpress(menu):
  if menu == "cardapio":
   return render_template("cardapio.html")
  
  
  elif menu == "cliente":
        return render_template("cliente.html")

  elif menu == "contato":
        return render_template("contato.html")

  elif menu == "inicio" or "tela inicial" or "menu":
   return render_template("index.html")

  elif menu == "lanche" or "comida" or "rango" or "almoço" or "janta":
   return render_template("lanche.html")
 
  elif menu == "pedido":
   return render_template("pedidos.html")
 
  if __name__ == '__main__':
    app.run()