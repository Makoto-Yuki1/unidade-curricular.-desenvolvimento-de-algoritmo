nome = input("digite seu nome")
if len(nome) > 20:
  print("seu nome é grande, ele possui mais de 20 letras")
print(f"ele possui{len(nome)} caracteres")


valor= int(input("digite seu número:"))
if valor % 2 == 0:
  print("o número é par")
else:
  print("o número é impar")
   
nota = float(input("digite sua nota"))
if nota >= 10:
     print("passou")
elif nota == 7:
    print("pode melhorar")
    # o elif serve para ser um "se se não", um meio entre if e else
else:
    if nota == 7:
     print("pode melhorar")
    else:
     print("recuperação")

idade = int(input)(("digite a idade:"))

if idade >= 16 and idade <= 69:
    print("faixa permitida")
else:
    print("fora da faixa")