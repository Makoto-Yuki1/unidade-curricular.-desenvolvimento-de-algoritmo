def notas(nota1, nota2):
 nota1 = float(input("Digite a primeira nota: "))
 nota2 = float(input("Digite a segunda nota: "))

 resultado1 = nota1 + nota2

 resultado2 = (nota1 + nota2)/2
 
 resultado3 = max(notas)
 
 resultado4 = min(notas)
 
 return resultado1, resultado2, resultado3, resultado4
 
 print("analise das notas")
 print("1 - Soma: {resultado1}")
 print("2 - média: {resultado2}")
 print("3 - maior nota: {resultado3}")
 print("4 - menor nota: {resultado4}")
 
notas(9.2, 2.5)



