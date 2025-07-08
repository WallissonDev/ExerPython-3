#Forma 1 de fazer
#import random
#n1 = str(input('Nome do Aluno 1: '))
#n2 = str(input('Nome do Aluno 2: '))
#n3 = str(input('Nome do Aluno 3: '))
#n4 = str(input('Nome do Aluno 4: '))
#lista = random.choice[n1,n2,n3,n4]
#print(f'O aluno sorteado é {lista}')
# Observe que usamos pela primeira vez os [] para apontar os objetos que farão parte do sorteio
# Forma 2 de fazer
import random
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1,n2,n3,n4]
escolha = random.choice(lista)
print(f'O escolhido foi {escolha}')
