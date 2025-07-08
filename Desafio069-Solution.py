t = m = f = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M][F]:')).upper().strip()[0]
    if idade > 18:
        t += 1
    if sexo == 'M':
        m += 1
    if idade < 20 and sexo == 'F':
        f += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S][N]')).upper().strip()[0]
    if continuar in 'Nn':
        break
