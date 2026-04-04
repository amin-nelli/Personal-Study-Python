print("Quantos Litros tem o balde")
Litros = int(input())
print("Qual o rendimento da lata? por favor apenas numeros")
Rendimento = int(input())
print("Quantos metros quadrados pretende pintar? pore favor apenas numeros")
MetrosParede = int(input())

def calculo(MetrosParede,Rendimento):
    resultado = MetrosParede/Rendimento
    return resultado

resultado = calculo(MetrosParede,Rendimento)
print(f"Voce precisara de {resultado:.1f} Balde(s) de tinta")
