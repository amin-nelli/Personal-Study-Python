def adicionar_nota(titulo, conteudo):
    with open("notas.txt", "a") as arquivo:
        arquivo.write(f"{titulo} \n {conteudo}\n\n")

def visualizar_nota():
    with open("notas.txt", "r") as arquivo:
        notas = arquivo.read()
        print(notas)

def excluir_nota(titulo):
    all_notas = ""
    with open("notas.txt", "r") as arquivo:
        notas = arquivo.read()
        notas2 = notas.split('\n\n')

    for i,dummy in enumerate(notas2):
        if titulo in dummy:
            notas2.pop(i)
            break
    print(notas2)
    for i,nota in enumerate(notas2):
        if nota != "":
            all_notas += nota + "\n\n"

    with open("notas.txt", "w") as arquivo:
        arquivo.write(f"{all_notas}")

while True:
    opcao = input(f'Escolha uma opção (adicionar/visualizar/excluir/sair): ')
    opcao = str(opcao).lower()

    if opcao == 'sair':
        break
    elif opcao == 'adicionar':
        titulo = input('Digite o titulo da nota: ')
        conteudo = input('Digite o conteudo da nota: ')
        adicionar_nota(titulo, conteudo)
    elif opcao == 'visualizar':
        visualizar_nota()
    elif opcao == 'excluir':
        titulo = input('Digite o titulo da nota: ')
        excluir_nota(titulo)
    else:
        print(f'Valor invalido. Tente novamente')

