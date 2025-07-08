pessoas = list()
pesadas = list()
leves = list()
contagem = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso KG: ')))
    contagem += 1
    if pessoas[1] >= 100:
        pesadas.append(pessoas[:])
        pessoas.clear()
    elif pessoas[1] <= 70:
        leves.append(pessoas[:])
        pessoas.clear()
    while True:
        resp = str(input('Quer continuar? [S:N]')).upper().strip()[0]
        if resp in 'NnSs':
            break
    if resp == 'N':
        break
print(f'A lista de pessoas leves é : {leves} que pesam {leves[1][1]}')
print(f'A lista de pessoas pesadas é: {pesadas[0]} que pesam {pesadas[1][1]}KG')
print(f'Número de Pessoas Cadastradas é: {contagem}')