from flask import Flask, render_template

app = Flask(__name__)


@app.route('/pizzaria/<saBOR>')
def pizzaria(saBOR):
  if saBOR == "calabresa":
   return render_template("calabresa.html")
  
  
  elif saBOR == "margherita" or "margerita":
        return render_template("margherita.html")

  elif saBOR == "portuguesa":
        return render_template("portuguesa.html")

  elif saBOR == "frango" or "frango e catupiry" or "frango com catupiry" or "frango e catupiri" or "frango com catupiri":
   return render_template("franguinho.html")

  elif saBOR == "abacaxi":
   return render_template("abacaxi.html")
 
  elif saBOR == "4 queijos" or "4queijos" or "four chesses":
   return render_template("4queijos.html")
 
  elif saBOR == "nordestina" or "nooorrrdestiina":
   return render_template("nordestina.html")
 
  






if __name__ == '__main__':
    app.run()