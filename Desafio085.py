numeros = list()
pares = list()
impares = list()
for c in range(0,8):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
if len(pares) > 0:
    numeros.append(pares[:])
    print(f'Os números pares são: {numeros[0]}')
else:
    print('Não tem pares.')
if len(impares) > 0:
    numeros.append(impares[:])
    print(f'Os números impares são: {numeros[1]}')
else:
    print('Não tem impares.')
