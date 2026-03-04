animal = ["cachorro", "gato"]
print("lista inicial:", animal)
animal = ["cachorro", "gato"]
animal.append("pato")
print("lista atualizada:", animal) 
animal.insert(1,"coelho") # adiciona em uma posição especifica
print("lista atualizada:", animal)
animal.extend(["macaco", "leão"]) #adiciona mais um dado
print("lista atualizada:", animal)

animal.remove("leão")
print(animal)

removido = animal.pop()
print(f"removido:{removido}")
print("após pop()", animal)

removido2 = animal.pop(1)
print(f"removido do índice 1 {removido2}")
print("após pop(1):", animal)

del animal[0]
print("após o del", animal)
animal.clear()
print(animal)

