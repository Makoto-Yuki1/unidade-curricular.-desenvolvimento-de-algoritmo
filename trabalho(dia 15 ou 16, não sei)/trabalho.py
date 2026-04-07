import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("maior")
    elif palpite > numero_secreto:
        print("menor")
    else:
        print("Acertou!")
        print(f"Você precisou de {tentativas} tentativas.")
        break


numeros = []

print("\nDigite 8 números:")

for i in range(8):
    n = int(input(f"{i+1}º número: "))
    numeros.append(n)

contagem = {}

for num in numeros:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

print("\nNúmeros repetidos:")

if_repetido = False
for num, qtd in contagem.items():
    if qtd > 1:
        print(f"O número {num} apareceu {qtd} vezes.")
        if_repetido = True

if not if_repetido:
    print("Nenhum número foi repetido.")


















































































