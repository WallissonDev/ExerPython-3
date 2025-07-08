from random import randint
# Solução 1
#pc = randint(0,5)
#pc2 = randint(0,5)
#pc3 = randint(0,5)
#pc4 = randint(0,5)
#pc5 = randint(0,5)
#b = pc,pc2,pc3,pc4,pc5
#c = sorted(b)
#print(f'A lista aleatória: {b}')
#print(f'A lista ordenada: {c}')
#print(f'o menor valor : {min(c)}')
#print(f'o maior valor : {max(c)}')
#
listagem = ()
for i in range (1,6):
    pc = randint(0,10)
    listagem += pc,
# Forma 1 de encontrar o menor:maior
# Assim meu primeiro elemento na indice vai ser o meu menor e o último maior
ordenada = sorted(listagem)
print(f'A lista: {ordenada}')
print(f'O menor elemento nela: {ordenada[0]}')
print(f'O maior elemento nela: {ordenada[-1]}')
# Forma 2 de encontrar o menor:maior
#min(listagem)
#max(listagem)