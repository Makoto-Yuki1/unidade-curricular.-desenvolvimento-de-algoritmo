
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

 print(f"livro  '{titulo}' adicionado com sucesso")
 return True

adicionarLivro ("L001", "robert martin", "codigo limpo" 2)







