#atividade 4
nome = input("digite seu nome:")
senhacorreta = "123456"
tentativa = 3
while tentativa > 0:
   senha = input("digite sua senha:")
if senha == senhacorreta:
    print(f"olá {nome}! seja bem-vindo!")
    

else:
    tentativa -= 1

if tentativa == 2:
    print("senha incorreta! você tem 2 tentativas")
elif tentativa == 1:
    print("senha incorreta! você tem 1 tentativa")
else:
    print("senha bloqueada")