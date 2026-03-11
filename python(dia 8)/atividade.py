aluno = {}

aluno["nome"] = input("qual o seu nome:")
aluno["prova1"] = int(input("qual a nota da sua primeira prova:"))
aluno["prova2"] = float(input("qual a nota da sua segunda prova:"))


media = aluno["prova1"] + aluno["prova2"]/2

aluno["media"] = media

print("\n dados")
print("nome:", aluno["nome"])
print("nota da primeira prova:",aluno["prova1"])
print("nota da segunda prova:", aluno["prova2"])
print("altura:", aluno["altura"])
print("media:", round(aluno["media"],2))
if media >= 7:
    print("você foi aprovado, parabêns!")
if media >= 5 
    print("você foi aprovado, parabêns!")