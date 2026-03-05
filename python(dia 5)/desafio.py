
import random
lista = [68, 7, 4, 90, 29, 59]
print("lista oficial:", lista)

#sort crescente
lista.sort()
print("após ordem crescente:", lista)

#sort decrescente
lista.sort(reverse=True)
print("após ordem decrescente", lista)

dados = [68, 7, 4, 90, 29, 59]
random.shuffle(dados)
print("embaralhar:", dados)
