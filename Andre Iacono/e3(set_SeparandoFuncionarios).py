
funcionarios = ['Antonio','Marcos','Rosa','Maria','Claro','Sophia','Melissa']
turno_dia = ['Antonio','Marcos','Rosa','Melissa']
turno_noite = ['Maria','Claro','Sophia']
tem_carro = ['Marcos','Rosa','Maria','Melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)   