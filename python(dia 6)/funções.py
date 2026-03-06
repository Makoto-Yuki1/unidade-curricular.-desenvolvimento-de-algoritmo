notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("notas:", notas)


print("menor nota:", min(notas))
print("menor nota:", max(notas))
print("soma:", sum(notas))
print("média:", sum(notas)/ len(notas))



nomes = ["adriana", "barbara", "carla", "daniel"]

print("usando FOR simples:")

for nome in nomes:
   print(f"olá,{nome}")

   print(f"enumerate:")

for indice, nome in enumerate:
   print(f"posição {indice}: {nome}")


#clonagem e manipulação de listas
original = ["A", "B", "C"]
copia = list(original)

print("original:", original)
print("copia:", copia)
print("são iguais:", original == copia)

copia.append("D")
print("original:", original)
print("copia:", copia)
print("são iguais:", original == copia)



