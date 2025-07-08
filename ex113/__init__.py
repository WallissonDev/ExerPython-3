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
            print(f'Você digitou o número {num}')
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mTivemos um dado inválido, somente números Floats ou Inteiros.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[32mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            print(f'Você digitou o número {num}')
            return num