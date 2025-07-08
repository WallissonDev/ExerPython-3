print('\033[31mOlá Mundo!')
print('\033[30;41mOlá Mundo!')
print('\033[1;30;45mOlá Mundo!')
print('\033[1:30:45mOláMundo!\033[m') #Usamos no final o \033[m pra voltar ao padrão do terminal
print('\033[4;30;45mOlá, Mundo!\33[m')
print('\033[7;30;47mOlá Mundo!\033[m')
print('\033[1;29;40mOlá mundo!\033[m')
print('\033[7;40mOlá mundo!\033[m')
print('\033[7;40mOlá mundo!\033[m')
print('\033[0;33;44mOlá mundo!\033[m')
print('\033[7;33;44mOlá mundo!\033[m')
# Linha 10 e 11 sendo invertida de cores
#a = 3
#b = 5
#print(f'Os valores são \033[32m{a}\033[m e \33[31m{b}')
#nome = 'Guanabara'
#print(f'Olá muito prazer em te conhecer, {'\033[4;34m',nome,'\033[m'}!!!')
nome = 'wally'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print(f'Olá! muito prazer em te conhecer {cores['azul']}{nome}')
