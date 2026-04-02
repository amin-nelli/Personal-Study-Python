class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Aventureiro(pessoa):
    def procurar_aventura(self):
        print(f'{self.nome} esta olhando o painel de quests da guilda')
class Administrador(pessoa):
    def averiguar_registros(self):
        print(f'{self.nome} esta olhando os arquivos da guilda atras de inconsistencias')

class Guilda:
    aventureiros = []
    administradores = []

    def __init__(self, nome):
        self.nome = nome
    def adicionar_adiministrador(self, administrador_dummy):
        self.administradores.append(Administrador(administrador_dummy.nome, administrador_dummy.idade))
    def adicionar_aventureiro(self, aventureiro_dummy):
        self.aventureiros.append(Aventureiro(aventureiro_dummy.nome, aventureiro_dummy.idade))
    def mostrar_aventureiros(self):
        for aventureiro_dummy in self.aventureiros:
            print('========== AVENTUREIROS DA GUILDA ==========')
            print(aventureiro_dummy.nome)
    def mostrar_administradores(self):
        for administrador_dummy in self.administradores:
            print('========== ADMINISTRADORES DA GUILDA ==========')
            print(administrador_dummy.nome)



pessoas_list = []
pessoas_list.append(pessoa('pedro',17))
pessoas_list.append(pessoa('maria',23))
guild_list = []
guild_list.append(Guilda('Aincrad'))
guild_list[0].adicionar_adiministrador(pessoas_list[0])
guild_list[0].adicionar_aventureiro(pessoas_list[1])
guild_list[0].mostrar_aventureiros()
guild_list[0].mostrar_administradores()
guild_list[0].aventureiros[0].procurar_aventura()
guild_list[0].administradores[0].averiguar_registros()
