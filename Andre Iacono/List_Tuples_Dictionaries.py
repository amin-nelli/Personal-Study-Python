frutas = [] #lista
diasSemana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo') #Tuplas
usuario = {
    'nome' = 'Kirito'
    'idade' = 22
    'cidade' = 'Aincrad'
}

frutas.append(input("digite um fruta: "))
frutas.append(input("digite outra fruta: "))
frutas.append(input("digite outra fruta: "))

print('==== As Frutas Que Voce Listou Sao ===')
for fruta in frutas:
    print(fruta)


for diaSemana in diasSemana:
    print(diaSemana)
