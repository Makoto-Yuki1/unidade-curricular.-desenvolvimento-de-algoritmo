alimentação = input("qual o valor da sua alimentação")
transporte = input("qual o valor do seu transporte")
lazer = input("qual o valor do seu lazer")
mesada = input("qual o valor da sua mesada")
gastos = alimentação + transporte + lazer
if gastos > mesada:
    print(mesada)
    print(gastos)
    print("seu gasto é muito alto")
elif gastos < mesada:
    print(mesada)
    print(gastos)
    print("sobrou dinheiro, está indo bém")







