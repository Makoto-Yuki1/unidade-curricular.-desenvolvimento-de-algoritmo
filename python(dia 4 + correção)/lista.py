#listas


nome1 = "ANA"
nome2 = "BRUNO"
nome3 = "CARLOS"

nomes = ["Arthur", "João", "Maria"]
print(nomes)

dados = ["Gabriel", 0, 1.60, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

alunos = ["Adriano", "Bárbara", "Camila"]

print("Primeiro", alunos[0])
print("Primeiro", alunos[1])
print("Primeiro", len(alunos))
print("Primeiro", alunos[2])
print("Primeiro", [len(alunos) - 1])

nomes = ["Ana", "Bruno", "Caio"]
print("original", nomes)
nomes.append("Daniel")
print("Atualizado:", nomes)
