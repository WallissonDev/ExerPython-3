from time import sleep
def contador(inicio, fim, passo):
    print('-='*15)
    for c in range(inicio, fim, passo):
        sleep(0.38)
        print(c, end = ' ')
    sleep(0.38)
    print('FIM!',end = ' ')
    print()


contador(1,11,1)
contador(10,-1,-2)
print('-='*15)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
if c == 0:
    c = 1
if a > b and c > 0:
    contador(a, b-c, -c)
elif a < b and c > 0:
    contador(a, b+c, c)
elif a > b and c < 0:
    contador(a, b+c, c)
