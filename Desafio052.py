DIVISION_COUNT = 0
n = int(input('Digite um Número: '))
for i in range (1,n+1):
    if n % i == 0:
        DIVISION_COUNT += 1
if DIVISION_COUNT == 2:
    print(f'O número {n} é Primo, pois só é divisível por 1 e {n}.')
else:
    print(f'O número {n} não é primo, pois é divisível em mais do que duas vezes.')
