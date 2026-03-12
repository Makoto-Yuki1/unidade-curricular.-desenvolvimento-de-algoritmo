#sem função
print("olá, mundo!")
print("olá, mundo!")
print("olá, mundo!")

#com função
def exibirMensagem():
   print("olá, mundo!")

exibirMensagem()
exibirMensagem()
exibirMensagem()

#função com parametro
def saudar(nome):
    print(f"olá {nome}!")

saudar("Júlio")
def exibirBoasVindas(pessoa, mensagem):
    print(f"{mensagem}, {pessoa}")

exibirBoasVindas("ana", "Bom dia")

def exibirBoasMensagens(mensagem = "olá", pessoa = "jõao"):
   print("f{mensagem}, {pessoa}")



#função que retorna um valor
def calcularMedia(nota1, nota2):
    media = (nota1 + nota2)/2 
    return media
resultado = calcularMedia(8.0, 9.0)
print(f"média: {resultado}")

#função que retorna multiplos valores
def obterMaiorMenor(a, b, c):
    maior = max(a, b, c)
    menor = min(a, b, c)
    return maior, menor

maxValor, minValor = obterMaiorMenor(10,5,8)
print(f"maior: {maxValor} e menor: {minValor}")

