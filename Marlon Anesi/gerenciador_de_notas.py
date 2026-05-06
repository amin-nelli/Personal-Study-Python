def adicionar_nota(titulo, conteudo):
    with open("notas.txt", "a") as arquivo:
        arquivo.write(f"{titulo} \n {conteudo}\n\n")

def visualizar_nota():
    with open("notas.txt", "r") as arquivo:
        notas = arquivo.read()
        print(notas)

while True:
    opcao = input(f'Escolha uma opção (adicionar/visualizar/sair): ')
    opcao = str(opcao).lower()

    if opcao == 'sair':
        break
    elif opcao == 'adicionar':
        titulo = input('Digite o titulo da nota: ')
        conteudo = input('Digite o conteudo da nota: ')
        adicionar_nota(titulo, conteudo)
    elif opcao == 'visualizar':
        visualizar_nota()
    else:
        print(f'Valor invalido. Tente novamente')

