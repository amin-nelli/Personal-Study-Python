#from Functions_box import saudacoes
#saudacoes("julio")

import Functions_box
Functions_box.saudacoes("julio")

minha_idade = int(input("Digiti sua idade: "))

if Functions_box.verificar_maioridade(minha_idade):
    print("Voce é maior de idade :)")
else:
    print("Voce é menor de idade :(")

