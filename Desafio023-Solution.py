Num = int(input('Digite um Número: '))
U = Num // 1 % 10
D = Num // 10 % 10
C = Num // 100 % 10
M = Num // 1000 % 10
print(f'Analisando o Número: {Num}')
print('Unidade: ', U )
print('Dezena: ', D )
print('Centena: ', C )
print('Milha: ', M )