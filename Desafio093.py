jogador = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))
jgols = list()
total = 0
for c in range (1, partidas+1):
    gols = int(input(f'Quantos Gols na partida {c}: '))
    jgols.append(gols)
    total += gols
status = { 'Jogador' : jogador,
            'Gols' : jgols[:],
           'Total' : total
           }
print('='*30)
print(status)
print('='*30)
for k, v in status.items():
    print(f'O campo {k} tem o valor {v}')
print('='*30)
print(f'O jogador {status['Jogador']} jogou {partidas} partidas.') # Poderia usar apenas a variável jogador pra puxar o nome, porém o foco é treinar o uso de dicionário
for p, g in enumerate(jgols):
    print(f'      => Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {total} gols.')