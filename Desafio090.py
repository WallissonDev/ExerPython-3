aluno = dict()
aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Nota 1'] = float(input('Nota 1: '))
aluno['Nota 2'] = float(input('Nota 2: '))
aluno['Media'] = (aluno['Nota 1'] + aluno['Nota 2']) / 2
if aluno['Media'] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno ['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a = {v}')
