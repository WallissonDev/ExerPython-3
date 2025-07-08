num = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite o último valor: ')))
print(f'Os números são : {num}')
print(f'O número 9 aparece: {num.count(9)}')
if 3 in num:
    print(f'O número 3 aparece primerio na posição: {num.index(3,1)+1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares são: ')
for c in num:
    if c % 2 == 0:
        print(f'{c}', end = ' ')