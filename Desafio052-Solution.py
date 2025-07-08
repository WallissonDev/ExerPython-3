DIVISION_COUNT = 0
COUNT = 0
NUM = int(input('Write a number: '))
for i in range(1,NUM+1):
    if NUM % i == 0:
        print('\033[1;32m',end = ' ')
        DIVISION_COUNT += 1
    else:
        print('\033[0;31m',end = ' ')
    print(i,end = '')
if DIVISION_COUNT == 2:
    print('\n \033[0mÉ primo', end = ' ')
    print(f'\n \033[0mO número {NUM} foi dividido {DIVISION_COUNT} vezes')
else:
    print('\n \033[0mNão é primo')
    print(f'\n \033[0mO número {NUM} foi divido {DIVISION_COUNT} vezes')






