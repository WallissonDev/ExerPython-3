from time import sleep
def maior(*num):
    print('-='*15)
    print('Analisando os valores passados...')
    sleep(0.2)
    max = 0
    for k, v in enumerate(num):
        sleep(0.37)
        print(v, end = ' ')
        if k == 0:
            max = v
        else:
            if v > max:
                max = v
    print(f'Foram informados ao todo {len(num)} números.')
    print(f'O maior valor informado foi : {max}')
    print('-='*15)


maior(9, 4, 5, 7, 2, 1, 12)
maior(2, 1, 5 , 20, 8)
maior()