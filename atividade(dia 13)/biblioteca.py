
#armazenar
catalogo = {}
#emprestimos ativos
emprestimosAtivos = {}
#histórico
historico = []

def adicionarLivro(codigo, titulo, autor, quantidade):
   if codigo in catalogo:
      print(f"erro: livro com codigo {codigo} já existe")
      return False
   catalogo[codigo] = {
      "titulo": titulo,
      "autor": autor,
      "quantidade": quantidade,
   }

   print(f"livro '{titulo}' adicionado com sucesso")
   return True

adicionarLivro("L001", "robert martin", "codigo limpo" ,2)



def empresta_livro(codigo, nome_aluno):
   if codigo not in catalogo:
    print(f"erro: livro com codigo {codigo} não encontrado!")
    return False
livros_do_aluno = conta_livros_aluno(nome_aluno)
print(f"erro: {nome_aluno} já pegou este livro!")
return False


   if codigo in emprestaAtivo and nome_aluno in emprestimosAtivo[codigo]:
    print(f"erro: {nome_aluno} já pegou este livro")
return False

if codigo not in emprestimosAtivo:
   emprestimosAtivo[codigo] = []

emprestaAtivo[codigo].append(nome_aluno)

catalogo[codigo]["quantidade"] -= 1

historico.append({
  "tipo": "emprestimo",
  "codigo": codigo,
  "titulo": catalogo[codigo]["titulo"],
  "aluno": nome_aluno
})
 print(f"{nome_aluno} pegou '{catalogo[codigo]['titulo']} com sucesso!")
 return True

def devolve_livro(codigo, nome_aluno):
  
   if codigo not in emprestimoAtivo or nome_aluno not in emprestimosAtivo[codigo]:

def conta_livros_aluno(nome_aluno):
        contador = 0
   
        for codigo, alunos in emprestimoAtivo.items():
            if nome_aluno in alunos:
               contador += 1
        return contador


def lista_emprestimos():
   print("\n" + "="*60)
   print("livros emprestados no momento")
   print("="*60)
   

   if not emprestimosAtivo:
       print("nenhum livro emprestado.")
       return

for codigo, alunos in emprestimosAtivo,items():
 titulo = catalogo[codigo]["titulo"]
 print(f"\n {titulo} ({codigo})")

for aluno in alunos:
 print(f" emprestado para: {aluno}")



print("\n--- adicionando livros ao catalogo ---")
adicionarLivro("L001", "clean code", "robert martin", 2)
adicionarLivro("L002", "python fluente", "luciano ramalho", 1)
adicionarLivro("L003", "algoritmos", "thomas cormen", 3)




print("\n--- alunos pegando livros ---")
empresta_livro("L001", "ana")
empresta_livro("L001", "bruno")
empresta_livro("L002", "ana")
empresta_livro("L003", "carlos")

print("\n--- tentando emprestar novamente ---")
empresta_livro("L001", "ana")
empresta_livro("L002", "ana")

print("\n--- listando emprestimos ativos ---")
lista_emprestimos()




