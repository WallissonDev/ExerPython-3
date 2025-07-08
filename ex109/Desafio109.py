from utilidadesCeV.moedas import moedas

num = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {num} é {moedas.metade(num, True)}')
print(f'O dobro de R$ {num} é {moedas.dobro(num, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(num, 10, True)}')
print(f'Reduzindo 13%, temos  {moedas.diminuir(num, 13, True)}')