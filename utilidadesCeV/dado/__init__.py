def leiadinheiro(a):
    from utilidadesCeV.moedas import moedas
    while True:
        b = a
        a = input(a)
        moedas.moeda(a)
        if a.isnumeric():
            return float(a)
        else:
            print(f'ERRO! >{a}< é um preço inválido!')
            a = b
