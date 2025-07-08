numfac = int(input('Qual numero do fatorial que deseja? '))
print('-'*30)
count = numfac - 1
basic = numfac
soma = 0
print(numfac, end='! = ')
while count != 0:
    soma = basic * count
    basic = soma
    print(f'x {count} ', end='')
    count -= 1
print(f'= {soma}')
print('-'*30)
print(f'O Fatorial de {numfac} é {soma}')