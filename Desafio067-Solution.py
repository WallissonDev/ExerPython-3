while True:
    num = int(input('Digite um valor: '))
    print('-' * 30)
    if num < 0:
        break
    for i in range(1,11):
        mult = num * i
        print(f'{num} X {i} = {mult}')
    print('-' * 30)
print('Até mais!')