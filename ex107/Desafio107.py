from utilidadesCeV.moedas import moedas

num = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {num} é {moedas.metade(num)}')
print(f'O dobro de R$ {num} é {moedas.dobro(num)}')
print(f'Aumentando 10%, temos {moedas.aumentar(num, 10)}')
print(f'Reduzindo 13%, temos  {moedas.diminuir(num, 13)}')