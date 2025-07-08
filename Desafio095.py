jgols = list()
lista = list()
total = 0
while True:
    jogador = str(input('Nome do Jogador: '))
    partidas = int(input('Quantas partidas ele jogou: '))
    for c in range (1, partidas+1):
        gols = int(input(f'Quantos Gols na partida {c}: '))
        jgols.append(gols)
        total += gols
    status = { 'Jogador' : jogador,
                'Gols' : jgols[:],
               'Total' : total
               }
    lista.append(status.copy())
    jgols.clear()
    total = 0
    while True:
        continuar = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
        if continuar in 'NnSs':
            break
    print('-' * 40)
    if continuar in 'Nn':
        break
print(f'{'COD':<5}{'NOME':^10}{'GOLS':^20}{'TOTAL':>5}')
print('-='*30)
for p, e in enumerate(lista):
    print(f'{p:<5}{lista[p]['Jogador']:^10}{str(lista[p]['Gols']):^20}{lista[p]['Total']:>5}')
while True:
    print('=' * 30)
    selecionar = int(input('Mostrar dados de qual jogador? Digite a posição: [999 p/ parar]: '))
    if selecionar == 999:
        break
    print(f'O jogador => {lista[selecionar]['Jogador']}')
    for p, v in enumerate(lista[selecionar]['Gols']):
        print(f'Na partida {p+1} -> {v}')
    print(f'O total de gols foi -> {lista[selecionar]['Total']}')
    print('=' * 30)
