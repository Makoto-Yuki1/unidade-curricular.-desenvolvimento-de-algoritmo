idade = print(int(input("qual a sua idade?:")))
if idade < 12:
    print("você é infantil")
if idade < 18 and idade >= 12:
    print("você é juvenil")
if idade < 60 and idade >= 18:
    print("você é adulto")
else:
    print("você é idoso")

