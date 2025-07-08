def fatorial(num = 1, show = False):
    """"
    Fatorial(num = 1, show = False)
        -> Função que calcula Fatorial
        :parametro num: O número a ser calculado
        :parametro show: opcional mostrar ou não a expressão
        :return: O valor do fatorial
    """
    f = 1
    expressao = ''
    for c in range(num, 0, -1):
        f *= c
        expressao += f'{c}'
        if c > 1:
            expressao += f'x'
        elif c == 1:
            expressao += ' = '
    if show:
        print(f'Fatorial de {num}! = {expressao} = {f}')
    else:
        print(f'Fatorial de {num}! = {f}')
    return


valor_fatorial = int(input('Qual valor deseja ver o fatorial ? '))
mostrar_expressao = str(input('Quer ver a expressão? [S/N]: ')).upper().strip()[0]
if mostrar_expressao in 'S':
    mostrar_expressao = True
else:
    mostrar_expressao = False
fatorial(valor_fatorial, mostrar_expressao)