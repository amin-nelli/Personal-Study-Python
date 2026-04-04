estoque = ['Virtus','Civic','City','Azera']
pesquisa_carro = input("Digite o nome do carro que esteja procurando: ")

if pesquisa_carro in estoque:
    print('O carro esta disponivel em estoque')
else:
    print('O carro não esta disponivel em estoque')