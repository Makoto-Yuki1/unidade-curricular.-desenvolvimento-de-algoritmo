

nome = input("qual o seu nome:")
matricula = int(input("qual a senha da sua matricula:"))
prova1 = float(input("qual a nota da sua primeira prova:"))
prova2 = float(input("qual a nota da sua segunda prova:"))
print("Olá", nome, "sua matricula é", matricula)
print("sua nota da primeira prova é de:", prova1)
print("sua nota da segunda prova é de:", prova2)
media = (prova1 + prova2) / 2
if media >= 7:
    print("você foi aprovado, parabêns!")
if media >= 5:
    print("você ficou de recuperação")
else:
    print("você foi reprovado, muito burro lkkkkkkkkkkk")