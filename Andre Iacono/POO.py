class Casa:
    def __init__(self, cor, quartos, banheiros, pessoas):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.pessoas = pessoas

    def mostrar_cor(self):
        print(self.cor)
    def mostrar_banheiros(self):
        print(self.banheiros)
    def mostrar_pessoas(self):
        print(self.pessoas)
    def mostrar_quartos(self):
        print(self.quartos)

casa1 = Casa("amarelo",4,2,4)
casa2 = Casa("azul",2,1,2)

print("\nCasa 1")
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.mostrar_pessoas()

print("\nCasa 2")
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.mostrar_pessoas()

