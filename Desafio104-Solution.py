def leiaint(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Valor Inválido!\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um Número: ')
print(f'Você digitou o número : {n}')