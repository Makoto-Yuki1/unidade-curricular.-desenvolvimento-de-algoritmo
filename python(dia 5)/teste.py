import random


numeros = [45, 12, 78, 23, 56]
print("lista oficial:", numeros)

#sort crescente
numeros.sort()
print("após sort():", numeros)

#sort decrescente
numeros.sort(reverse=True)
print("após sort()", numeros)

dados = [1, 2, 3, 4, 5]
random.shuffle(dados)
print("embaralhar:", dados)

