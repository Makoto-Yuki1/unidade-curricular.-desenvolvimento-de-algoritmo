nome = input("digite uma frase:")
vogais = "a" "e" "i" "o" "u" "A" "E" "I" "O" "U"
contador = sum(1 for letra in nome if letra in vogais)

print("Número de vogais:", contador)


