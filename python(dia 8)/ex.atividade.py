paciente = {}

paciente["nome"] = input("qual o seu nome:")
paciente["idade"] = int(input("quantos anos você tem:"))
paciente["peso"] = float(input("digite seu peso(kg):"))
paciente["altura"] = float(input("digite sua altura(m):"))

imc = paciente["peso"] / (paciente)

paciente["imc"] = imc

print("\n dados")
print("nome:", paciente["nome"])
print("idade:", paciente["idade"])
print("peso:", paciente["peso"])
print("altura:", paciente["altura"])
print("imc:", round(paciente["altura"],2))

