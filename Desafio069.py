maior = 0
homens = 0
mulheres = 0
menores = 0
c = 0
continuar = ''
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Qual a idade da pessoa? '))
    if idade < 18:
        maior += 1
    while True:
        sexo = str(input('Qual o sexo da pessoa? [M/F]')).upper().strip()[0]
        if sexo == 'M' or sexo == 'F':
            if sexo == 'M':
                homens += 1
                break
            if sexo == 'F' and idade < 20:
                menores += 1
                break
    continuar = str(input('Quer continuar? [S/N]:  ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O número de pessoas maiores de idade é : {maior}')
print(f'O número de homens cadastrados é : {homens}')
print(f'O número de mulheres menores de 20 é : {menores}')

