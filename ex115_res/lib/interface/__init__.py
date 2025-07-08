def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mTivemos um dado inválido, somente números Inteiros.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[32mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            return num


def linha(tam = 42):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c} - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua Opcão: ')
    return opc


