from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os


app = Flask(__name__)

app.secret_key = "chave_secreta_cantina"


DATA_FILE = "app.json"

# BANCO DE DADOS JSON

def criar_dados_iniciais():
    return {
        "users": [],

        "menu": [
            {
                "id": 1,
                "nome": "Sanduíche de frango",
                "descricao": "Pão integral com frango grelhado, alface e tomate.",
                "ingredientes": [
                    "frango",
                    "pão integral",
                    "alface",
                    "tomate"
                ],
                "restricoes": [
                    "sem lactose"
                ],
                "tipo": "proteína",
                "preco": 15.0
            },

            {
                "id": 2,
                "nome": "Salada vegetariana",
                "descricao": "Mix de folhas, cenoura ralada e grão-de-bico.",
                "ingredientes": [
                    "alface",
                    "cenoura",
                    "grão-de-bico",
                    "molho de ervas"
                ],
                "restricoes": [
                    "vegetariano",
                    "vegano",
                    "sem glúten",
                    "sem lactose"
                ],
                "tipo": "vegetariano",
                "preco": 12.0
            },

            {
                "id": 3,
                "nome": "Wrap sem glúten",
                "descricao": "Wrap leve com frango, queijo branco e legumes.",
                "ingredientes": [
                    "frango",
                    "tortilla sem glúten",
                    "queijo branco",
                    "legumes"
                ],
                "restricoes": [
                    "sem glúten"
                ],
                "tipo": "prato leve",
                "preco": 18.0
            },

            {
                "id": 4,
                "nome": "Hambúrguer de grão-de-bico",
                "descricao": "Hambúrguer vegano com molho especial e salada.",
                "ingredientes": [
                    "grão-de-bico",
                    "aveia",
                    "alface",
                    "tomate"
                ],
                "restricoes": [
                    "vegetariano",
                    "vegano",
                    "sem lactose"
                ],
                "tipo": "vegano",
                "preco": 16.5
            },

            {
                "id": 5,
                "nome": "Suco natural",
                "descricao": "Suco de laranja com cenoura sem açúcar.",
                "ingredientes": [
                    "laranja",
                    "cenoura",
                    "água"
                ],
                "restricoes": [
                    "vegano",
                    "sem glúten",
                    "sem lactose",
                    "sem açúcar"
                ],
                "tipo": "bebida",
                "preco": 8.0
                
            }
            
        ],
   
        "orders": [],

        "next_order_id": 1
    }



def load_data():

    if not os.path.exists(DATA_FILE):

        data = criar_dados_iniciais()

        save_data(data)

        return data


    with open(DATA_FILE, "r", encoding="utf-8") as arquivo:

        return json.load(arquivo)

def save_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as arquivo:

        json.dump(
            data,
            arquivo,
            ensure_ascii=False,
            indent=4
        )



# =========================
# FUNÇÕES AUXILIARES
# =========================
def current_user():

    return session.get("username")

def get_user(username, data):

    for user in data["users"]:

        if user["username"] == username:

            return user

    return None

def get_user_orders(username, data):

    return [
        pedido
        for pedido in data["orders"]
        if pedido["username"] == username
    ]                                                                                                                                                                                                                                         # =========================
# FILTRO DO CARDÁPIO

def filter_menu(menu, restricoes, preferencia):

    resultado = []

    for item in menu:

        if restricoes:

            tags = [
                r.lower()
                for r in item.get("restricoes", [])
            ]

            possui_todas = all(
                r.lower() in tags
                for r in restricoes
            )

            if not possui_todas:
                continue


        resultado.append(item)

    if preferencia:

        termo = preferencia.lower()


        resultado.sort(
            key=lambda item:
            0
            if (
                termo in item["nome"].lower()
                or termo in item["descricao"].lower()
                or any(
                    termo in ingrediente.lower()
                    for ingrediente in item["ingredientes"]
                )
            )
            else 1
        )


    return resultado



# =========================
# LOGIN PRINCIPAL
# =========================

@app.route("/")
def home():

    return redirect(
        url_for("")
    )



@app.route("/index", methods=["GET", "POST"])
def login():

    data = load_data()

    mensagem = ""


    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()


        password = request.form.get(
            "password",
            ""
        ).strip()



        if not username or not password:

            mensagem = "Informe usuário e senha."


        else:

            user = get_user(
                username,
                data
            )


            if user:

                if user["password"] != password:

                    mensagem = "Senha incorreta."


                else:

                    session["username"] = username

                    return redirect(
                        url_for("cardapio")
                    )

            else:

                novo_usuario = {

                    "username": username,

                    "password": password,

                    "restricoes": [],

                    "preferencias": []
                }


                data["users"].append(
                    novo_usuario
                )


                save_data(data)


                session["username"] = username


                return redirect(
                    url_for("cardapio")
                )



    return render_template(

        "index.html",

        login_message=mensagem,

        username=current_user(),

        menu=[],

        orders=[],

        restricoes=[],

        preferencia=""

    )



@app.route("/logout")
def logout():

    session.pop(
        "username",
        None
    )


    session.pop(
        "turma",
        None
    )


    return redirect(
        url_for("cardapio")
    )



# =========================
# CARDÁPIO
# =========================

@app.route("/cardapio")
def cardapio():

    data = load_data()


    username = current_user()


    restricoes = request.args.getlist(
        "restricao"
    )


    preferencia = request.args.get(
        "preferencia",
        ""
    )



    menu = filter_menu(

        data["menu"],

        restricoes,

        preferencia

    )



    pedidos = []


    if username:

        pedidos = get_user_orders(

            username,

            data

        )

    if request.args.get("format") == "json":

        return jsonify(menu)

    return render_template(

        "cardapio.html",

        username=username,

        menu=menu,

        orders=pedidos,

        restricoes=restricoes,

        preferencia=preferencia,

        login_message="",

        edit_order=None

    )



# =========================
# LOGIN DO ALUNO
# =========================

@app.route("/entrar", methods=["GET", "POST"])
def entrar():

    mensagem = ""


    if request.method == "POST":

        nome = request.form.get(
            "nome",
            ""
        ).strip()


        turma = request.form.get(
            "turma",
            ""
        ).strip()



        if not nome:

            mensagem = "Informe o nome do aluno."


        else:

            session["username"] = nome

            session["turma"] = turma


            return redirect(
                url_for("cardapio")
            )



    return render_template(

        "login_student.html",

        message=mensagem,

        username=current_user()

    )                                                                                                                                                                                                                                                                        # =========================
# PÁGINA DE FAZER PEDIDO
# =========================

@app.route("/pedido", methods=["GET"])
def pedido_page():

    username = current_user()


    if not username:

        return redirect(
            url_for("entrar")
        )


    data = load_data()


    item_id = request.args.get(
        "item_id",
        type=int
    )


    return render_template(

        "pedido.html",

        username=username,

        turma=session.get("turma"),

        menu=data["menu"],

        selected_id=item_id

    )



# =========================
# CRIAR PEDIDO
# =========================

@app.route("/pedido", methods=["POST"])
def criar_pedido():

    username = current_user()


    if not username:

        return redirect(
            url_for("entrar")
        )


    data = load_data()


    nome_aluno = request.form.get(
        "nome",
        ""
    ).strip()


    turma = request.form.get(
        "turma",
        ""
    ).strip()



    if not turma:

        turma = session.get(
            "turma",
            ""
        )



    item_id = request.form.get(
        "item_id"
    )


    try:

        quantidade = int(
            request.form.get(
                "quantidade",
                1
            )
        )

    except ValueError:

        quantidade = 1



    observacao = request.form.get(
        "observacao",
        ""
    ).strip()



    item = None


    for produto in data["menu"]:

        if str(produto["id"]) == str(item_id):

            item = produto

            break



    if not item or quantidade < 1:

    return redirect(
        url_for("confirmacao")
         )



    pedido = {


        "id": data["next_order_id"],


        "username": username,


        "nome_aluno": nome_aluno,


        "turma": turma,


        "itens": [

            {

                "id": item["id"],

                "nome": item["nome"],

                "quantidade": quantidade

            }

        ],


        "observacao": observacao

    }



    data["orders"].append(
        pedido
    )


    data["next_order_id"] += 1



    save_data(data)



    return redirect(
        url_for("cardapio")
    )



# =========================
# HISTÓRICO DE PEDIDOS
# =========================

@app.route("/pedidos")
def meus_pedidos():

    username = current_user()


    if not username:

        return redirect(
            url_for("entrar")
        )


    data = load_data()


    pedidos = get_user_orders(

        username,

        data

    )



    return render_template(

        "historicodepedidos.html",

        username=username,

        orders=pedidos

    )
# =======================
# CONFIRMAÇÃO DO PEDIDO
# =======================
@app.route("/confirmacao")
def confirmacao():
    username = current_user()
    return render_template("confirmacao.html", username=username)
    

# =========================
# EDITAR PEDIDO
# =========================

@app.route(
    "/pedido/<int:order_id>/editar",
    methods=["GET", "POST"]
)
def editar_pedido(order_id):

    username = current_user()



    if not username:

        return redirect(
            url_for("entrar")
        )



    data = load_data()



    pedido = None



    for item in data["orders"]:

        if (
            item["id"] == order_id
            and item["username"] == username
        ):

            pedido = item

            break



    if not pedido:

        return "Pedido não encontrado", 404



    if request.method == "POST":


        try:

            quantidade = int(
                request.form.get(
                    "quantidade",
                    1
                )
            )


        except ValueError:

            quantidade = 1



        observacao = request.form.get(
            "observacao",
            ""
        ).strip()



        if quantidade < 1:

            data["orders"] = [

                p

                for p in data["orders"]

                if p["id"] != order_id

            ]


        else:

            pedido["itens"][0]["quantidade"] = quantidade

            pedido["observacao"] = observacao



        save_data(data)



        return redirect(
            url_for("cardapio")
        )



    return render_template(

        "editarpedido.html",

        username=username,

        pedido=pedido

    )                                                                                                                                                                                                                                          # =========================
# API CARDÁPIO
# =========================

@app.route("/api/cardapio")
def api_cardapio():

    data = load_data()


    restricoes = request.args.getlist(
        "restricao"
    )


    preferencia = request.args.get(
        "preferencia",
        ""
    )



    menu = filter_menu(

        data["menu"],

        restricoes,

        preferencia

    )



    return jsonify(menu)



# =========================
# API PEDIDOS
# =========================

@app.route("/api/pedidos")
def api_pedidos():

    username = current_user()



    if not username:

        return jsonify(
            {
                "erro": "Usuário não autenticado."
            }
        ), 401



    data = load_data()



    pedidos = get_user_orders(

        username,

        data

    )



    return jsonify(pedidos)



# =========================
# API USUÁRIO
# =========================

@app.route("/api/usuario")
def api_usuario():

    username = current_user()



    if not username:

        return jsonify(
            {
                "logado": False
            }
        )



    data = load_data()



    user = get_user(

        username,

        data

    )



    return jsonify(

        {

            "logado": True,

            "usuario": user

        }

    )



# =========================
# ERRO 404
# =========================

@app.errorhandler(404)
def pagina_nao_encontrada(error):

    return render_template(

        "404.html"

    ), 404



# =========================
# INICIAR SERVIDOR
# =========================

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )
