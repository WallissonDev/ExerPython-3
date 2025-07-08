from time import sleep
c = ('\033[m', # 0 - Sem Cores,
     '\033[0;30;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - Verde
     '\033[0;30;43m', # 3 - Amarelo
     '\033[0;30;44m', # 4 - Azul
     '\033[0;30;45m', # 5 - Roxo
     '\033[7;30m'     # 6 - Preto
     )


def ajuda(com):
    título(f'Acessando Manual de \'{com}\'', 4)
    print(c[5], end = '')
    help(com)
    print(c[0], end = '')
    sleep(2)


def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print("~" * tam)
    print(f'  {msg}')
    print("~" * tam)
    print(c[0], end = '')
    sleep(1)


#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input("Função ou Biblioteca -> "))
    if comando.upper() == 'Fim':
        break
    else:
        ajuda(comando)
título('Até logo!', 1)