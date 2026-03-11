compra = float(input("digite o valor da compra: "))
if(compra < 100):
    print("compra sem desconto")
if(compra >= 100 and compra < 500):
    desconto = compra * 0.05
    valorfinal = compra - desconto
    print("compra com 5% de desconto, valor final: R$", valorfinal)
if(compra >= 500 and compra < 1000):
    desconto = compra * 0.10
    valorfinal = compra - desconto
    print("compra com 10% de desconto, valor final: R$", valorfinal)
elif(compra >= 1000):
    desconto = compra * 0.15
    valorfinal = compra - desconto
    print("compra com 15% de desconto, valor final: R$", valorfinal)

