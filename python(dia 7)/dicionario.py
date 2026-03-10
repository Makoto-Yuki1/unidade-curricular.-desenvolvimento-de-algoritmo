matricula1 = 2026001
nome1 = "ana silva"
telefone1 = "9999-8888"

#com dicionario
aluno = {
      "matricula": 2026001,
       "nome": "ana silva",
       "telefone":  "9999-8888"}

print(aluno)
contato = {
    "@camila": "camila",
    "@paola":  "paola",
    "@sheron":  "sheron",
    "@bruna":   "bruna"

}
print(contato)
print(type(contato))


#acesso direto ao dicionario
print(contato["@camila"])
#acesso seguro com get()
print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente","não encontrado"))

print("Original:", contato)#acessando a lista original

#add novo elemento
contato["@rekka vtnc"] = "rekka"
print("após add", contato)
#atualiza elemento existente
contato["@paola"] = "paola Oliveira"
print("após add:", contato)

contato.update(
    {
        "@bruna": "bruna marquezine",
        "@camila": "camila Q."
    }
)
print("após atualização:", contato)
#pop: remove e retorna
removido = contato.pop("@sheron")
print(f"removido: {removido}")
print("após o pop:", contato)


#del remove sem retornar
del contato["@paola"]
print("após o del:", contato)

#clear = esvaziar tudo
copia = dict(contato)
contato.clear()
print("após clear:", contato)
print("cópia:", copia)

print("número de contato:", len(contato))
contato.pop("@camila")
print("após remover um:", len(contato))

#verificar existência
if "@joao" in contato:
 print(f"encontrado: {contato['@joao']}")
if "@inexistente" in contato:
    print("existe")
else:
   print("não existe.")




#dicionario vazio
vazio={}

dados = {
    "nome": "joão",
    "idade": 25,
    "altura": 1.70,
    "ativo": True
}

print

("vazio:", vazio)
print("vazio:", dados)



