import datetime
ano = datetime.date.today().year
clt = dict()
clt['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
clt['Idade'] = ano - nascimento
clt['Carteira'] = int(input('Carteira de Trabalho: '))
if clt['Carteira'] == 0:
    print(clt)
    for k, v in clt.items():
        print(f'O {k} é :  {v}')
else:
    clt['Contratação'] = int(input('Ano de Contratação: '))
    clt['Salário'] = float(input('Salário R$: '))
    clt['Aposentadoria'] = (35 - (ano - clt['Contratação'])) + clt['Idade']
    for k, v in clt.items():
        if k == 'Salário':
            print(f'O {k} foi de R$ {v}')
        else:
            print(f'{k} tem valor de {v}')