nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
frutaFavorita = input("Digite seu fruta favorita: ")

print(f"Ola {nome}, voce tem {idade} anos de idade, e sua fruta favorita é {frutaFavorita}")
print(f"daqui 5 anos voce tera {idade + 5} anos de idade")
print(type(idade))

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

porcoes = 15
print(f"voce tem {porcoes} porcoes de peixe, deseja usar quantos por dia?")
usoDiario = int(input())
print(f"este produto ira durar {int(porcoes / usoDiario)} dias")
print(f"este produto ira durar {(porcoes / usoDiario):.0f} dias")#.0f quantas casas decimais vai mostrar apos a virgula
