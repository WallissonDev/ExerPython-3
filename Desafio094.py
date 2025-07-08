pessoas = dict()
lista = list()
mulheres = list()
acima = list()
media = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    pessoas['Idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    pessoas.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if continuar in 'NnSs':
            break
    if continuar in 'Nn':
        break
print('-'*40)
print(f'O número de pessoas cadastradas foi {len(lista)}')
print('-'*40)
for p, c in enumerate(lista):
    media += lista[p]['Idade']
print(f'A média de idade é : {media/len(lista):.1f}')
print('-'*40)
for k, v in enumerate(lista):
    if v['Sexo'] in 'F':
        mulheres.append(v['Nome'])
print(f'Mulheres: {mulheres}')
print('-'*40)
for p, c in enumerate(lista):
    if c['Idade'] >= media/len(lista):
        acima.append(c['Nome'])
print(f'Pessoas com idade acima da média: {acima}')
