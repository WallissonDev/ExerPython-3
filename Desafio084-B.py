pessoas = list()
pesadas = list()
leves = list()
maior = menor = c = contagem = 0
while True:
    nome = str(input('NOME: '))
    peso = int(input('PESO: '))
    pessoas.append(nome)
    pessoas.append(peso)
    contagem += 1
    if c == 0:
        maior = peso
        menor = peso
        leves.append(pessoas[0])
        pesadas.append(pessoas[0])
        pessoas.clear()
        c += 1
    elif peso == maior:
        pesadas.append(pessoas[0])
        pessoas.clear()
    elif peso > maior:
        pesadas.clear()
        maior = peso
        pesadas.append(pessoas[0])
        pessoas.clear()
    elif peso < menor:
        leves.clear()
        menor = peso
        leves.append(pessoas[0])
        pessoas.clear()
    elif peso == menor:
        leves.append(pessoas[0])
        pessoas.clear()
    else:
        pessoas.clear()
    while True:
        continuar = str(input('Quer continuar ? [S:N] '))
        if continuar in 'NnSs':
            break
    if continuar in 'Nn':
        break
print(f'O número de pessoas na lista é {contagem}')
print(f'As pessoas mais pesadas são: {pesadas} que pesam {maior}KGs')
print(f'As pessoas mais leves são: {leves} que pesam {menor}KGs')