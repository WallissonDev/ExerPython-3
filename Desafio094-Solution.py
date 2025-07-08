galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('Erro! Digite somente M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer conmtijnaur ? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadsatradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p['Nome']}')
print(f'D) Lista das pessoas que estão acima da média: ', end = '')
for p in galera:
    if p['Idade'] >= media:
        print(f' ', end = '')
        for k, v in p.items():
            print(f'{k} = {v} ')
print('<< ENCERRADO >>')