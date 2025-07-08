def fatorial(n = 0, show = False):
    """"
   Fatorial(n = 1, show = False)
       -> Função que calcula Fatorial
       :parametro n: O número a ser calculado
       :parametro show: opcional mostrar ou não a expressão
       :return: O valor do fatorial de um número n.
    """
    f = 1
    print(f' {n}! = ', end = '')
    for c in range(n, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(f' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

# Programa Principal
print(fatorial(5, show = True))