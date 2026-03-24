class Carro:
    def __init__(self,cor,ano):
        self.cor = cor
        self.ano = ano
        self.ligado = False
        self.seta = None

    def informacoes(self):
        print(self.cor)
        print(self.ano)
        print(self.ligado)

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Carro foi ligado")
        else:
            print("Carro ja esta ligado")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Carro foi desligado")
        else:
            print("Carro ja esta desligado")

    def ligar_seta(self,direcao):
        if self.ligado:
            self.seta = direcao
            print(f"seta ligada para {self.seta}")
        else:
            print("Ligue o carro para poder sair")


carro1 = Carro("cor",1)
carro1.informacoes()
carro1.ligar()