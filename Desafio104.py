def leiaInt(num):
    while True:
        a = input('Digite um num: ')
        if a.isnumeric():
            return a
        else:
            print(f'\033[0;31mERRO! Digíte um número inteiro válido.\033[0m')


n = leiaInt('Digite um Num: ')
print(f'O número digitado foi {n}')