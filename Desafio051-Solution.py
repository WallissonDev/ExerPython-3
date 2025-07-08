print('='*20)
print('10 PA TERMS')
print('='*20)
PA = int(input('First term of PA: ')) # Primeiro termo de uma Progressão Aritmética PA
RA = int(input('Ratio of arithmetic: ')) # Razão de uma PA
for i in range(PA,PA+(RA*10),RA): # Basicamente, inicia pela minha PA, vai até 10 termos a frente da minha PA, com uma Razão.
    print(f'{i}', end = ' -> ') # Apresenta Esse algoritmo
print('END')
#
# PA = int(input('First Term of PA: ')
# RA = int(input('Ratio of PA: ')
# TEN_PROGRESS = PA + ( RA * 10 )
# or
# TEN_PROGRESS = PA + ( 10 - 1 ) * RAX
# for i in range (PA, TEN_PROGRESS, RA)
# or
# for i in range (PA, TEN_PROGRESS + RA, RA)
#    print(f'{i}', end = ' -> ')
#print('END')