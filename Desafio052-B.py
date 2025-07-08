total = 0
num = int(input('Digite um Número: '))
for b in range (1,num+1):
    if num % b == 0:
        total += 1
if total == 2:
    print('É primo')
else:
    print('Não é primo')