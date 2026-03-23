num1 = int(input("Qual sua idade atual?"))
carteira = input("Voce possue carteira?")

if num1 < 18 :
    print("Voce nao pode dirigir um carro pois é menor de idade")
elif carteira != "sim":
    print("Voce nao pode dirigir um carro pois nao tem carteira")
else:
    print("Voce pode dirigir um carro pois é maior de idade e possui carteira")

for repetir in range(5):
    print(repetir)
