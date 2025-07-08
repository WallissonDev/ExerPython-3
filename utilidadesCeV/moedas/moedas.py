def aumentar(valor, porc = 1, form = True):
    """
    :param valor: Valor a ser calculado
    :param porc: Porcentagem do valor
    :return s: Resultado da Porcentagem do Valor + Valor
    """
    if form:
        a = valor * porc / 100
        s = valor + a
        c = 'R$ ' + str(s)
        return c
    else:
        a = valor * porc / 100
        s = valor + a
        return s


def diminuir(valor,porc = 1, form = False):
    """
    :param valor: Valor a ser calculado
    :param porc: Porcentagem do valor
    :return s: Resultado da Porcentagem do Valor - Valor
    """
    if form:
        a = valor * porc / 100
        s = valor - a
        b = 'R$ ' + (str(s))
        return b
    else:
        a = valor * porc / 100
        s = valor - a
        return s


def metade(valor, form = False):
    if form:
        s = valor / 2
        b = 'R$ ' + (str(s))
        return b
    else:
        s = valor / 2
        return s

def dobro(valor, form = False):
    if form:
        s = valor * 2
        b = 'R$ ' + (str(s))
        return b
    else:
        s = valor * 2
        return s


def moeda (valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')

def resumo(valor, porcam = 0, porrd = 0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: R$ {valor}')
    a = valor * 2
    print(f'Dobro do preço: R$ {a}')
    b = valor / 2
    print(f'Metade do Preço: R$ {b}')
    if porcam > 0:
        c = ((valor * porcam) / 100 ) + valor
        print(f'{porcam}% de aumento: R${c}')
    else:
        print(f'{porcam}% de aumento: R${valor}')
    if porrd > 0:
        d = valor - ((valor * porrd) / 100)
        print(f'{porrd}% de redução: R$ {d}')
    else:
        print(f'{porrd}% de redução: R$ {valor}')
    print('-'*30)
    return valor, porcam, porrd