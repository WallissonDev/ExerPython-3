c = ('\033[m', # 0 - Sem Cores,
     '\033[1;31m', # 1 - Vermelho
     '\033[1;32m', # 2 - Verde
     '\033[1;33m', # 3 - Amarelo
     '\033[1;34m', # 4 - Azul
     '\033[1;35m', # 5 - Roxo
     '\033[7;30m'  # 6 - Preto
     )


def menu(mensagem):
    print(f'{c[1]}={c[0]}'*30)
    print(f'{c[1]}{mensagem.center(30)}{c[0]}')
    print(f'{c[1]}={c[0]}'*30)
    print(f'{c[3]}1 - Ver Pessoas Cadastradas{c[0]}')
    print(f'{c[3]}2 - Cadastrar Novas Pessoas{c[0]}')
    print(f'{c[3]}3 - Sair do Sistema{c[0]}')
    return mensagem


def escolhaMenu():
    from time import sleep
    lista = list()
    while True:
        menu('Menu Principal')
        sleep(0.5)
        try:
            selecione = int(input(f'{c[4]}Sua opção: {c[0]}'))
            sleep(0.5)
        except (ValueError, TypeError, UnboundLocalError):
            print(f'Valor Inválido!')
        if selecione == 1:
            print(lista)
        if selecione == 2:
            pessoa = str(input('Nome para cadastro: '))
            lista.append(pessoa)
            print(f'{c[1]}Cadastro de {pessoa} realizado com Sucesso!{c[0]}')
        if selecione == 3:
            break


escolhaMenu()