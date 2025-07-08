from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1' : randint(1,6),
         'jogador2' : randint(1,6),
         'jogador3' : randint(1,6),
         'jogador4' : randint(1,6) }
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou = {v}')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print('='*30)
print(f'{'Por colocações':^30}')
print('='*30)
# Enfase que aqui essa função transforma o dicionário em uma lista com tuplas por dentro
for i, v in enumerate(ranking):
    sleep(1)
    print(f'O {i+1} lugar: com {v[0]} que tirou {v[1]}')