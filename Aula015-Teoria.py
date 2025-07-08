# cont = 1
# while cont True:
#    print(cont, '...', end = ' ')
#    cont += 1
# print('Acabou')
#n = 0
#while n != 999: # Esse 999 é o flag, ou seja a condição de parada.
#    n = int(input('Digite um número: '))
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}') 