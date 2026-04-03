class livro:
    def __init__(self, nome):
        self.nome = nome

class biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro_dummy):
        self.livros.append(livro_dummy)

    def mostrar_livros(self):
        for livro in self.livros:
            print(livro.nome)

livro1 = livro('Constelacoes')
livro2 = livro('Bestiario')
livro3 = livro('Zodiaco')

biblioteca1 = biblioteca('Biblioteca1')

biblioteca1.adicionar_livro(livro1)
biblioteca1.adicionar_livro(livro2)
biblioteca1.adicionar_livro(livro3)

biblioteca1.mostrar_livros()
