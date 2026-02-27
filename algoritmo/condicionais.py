estatura = float(input("digite sua altura: "))
estatura = estatura * 100
#em python, f strings são usadas para inserir textos traduzidos diretamente em uma frase

print(f"altura é de{estatura}")

nome = input("digite seu nome:")
idade:23

texto = "meu nome é {} e tenho {} anos".format(nome, idade)
texto = "meu nome é {n} e tenho {i} anos".format(n=nome,i=idade)
exto = "meu nome é %s e tenho %d anos" % (nome, idade)
print(texto)