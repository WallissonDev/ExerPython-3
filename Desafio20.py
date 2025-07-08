# Forma 1 - sem usar o form
#import random
#n1 = str(input('Nome 1: '))
#n2 = str(input('Nome 2: '))
#n3 = str(input('Nome 3: '))
#n4 = str(input('Nome 4: '))
#p = [n1,n2,n3,n4]
#random.shuffle(p)
#print(p)
# Forma 2 - Com o form para simplificar
from random import shuffle
n1 = str(input('Nome 1 : '))
n2 = str(input('Nome 2 : '))
n3 = str(input('Nome 3 : '))
n4 = str(input('Nome 4 : '))
l = [n1,n2,n3,n4]
shuffle(l)
print('A ordem é: ')
print(l)