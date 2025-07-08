# Ensinando a utilização de interactive help
#help(print) # Mostra as funções que print podem exercer.
#print(input.__doc__) # Outra maneira de mostrar as informações de uma função
#
# Isso tem utilidade quando queremos criar um DOCSTRING para uma função que nós mesmos criamos ou de outra pessoa.
# Para garantir que exista um manual da função criada.
#
# A DOSCTRING É CRIADA ENTRE """"""
#def contador(i, f, p):
#    """""
#    -> Faz uma contagem e mostra na tela.
#    :parametro i : inicio da contagem
#    :parametro f: fim da contagem
#    :parametro p: passo da contagem
#    :return: sem retorno
#    Função Criada por Wallisson durante o estudo de Python.
#   """
#    c = i
#    while c <= f:
#        print(f'{c}', end = '')
#        c += p
#    print('FIM!')
#
#
#help(contador) # Agora criamos acima um manual da função que nós mesmos criamos para contador()
# E dentro da própria função criamos uma DOCSTRING explicando para que ela serve e como usa-lá
#
# PARAMETROS OPICIONAIS
#
# Caso uma função criada receba numero x de parametros, ele vai necessitar que
# Quando executada a função, o número x de parametors sejam preenchidos de maneira proporcional ao de informações recebidas
# Porém, podemos determinar um valor padrão para um parametro, caso ele não venha receber a quantidade esperada de informações ele vai preencher com o valor padrão
#
#def somar(a = 0, b = 0, c = 0):
#    s = a + b + c
#    print(f'A soma é {s}')

#somar(3, 2, 5)
#somar(5, 1)
#somar()
#
# ESCOPO DE VARIÁVEIS
#
# Escopo = Local onde uma variável vai existir ou deixar de existir.
#
#
# ESCOPO GLOBAL = EXISTE EM TODA A LINHA
#def teste():
#    x = 8 # X tem um ESCOPO LOCAL só existe na função
#    print(f'Na função teste, n vale {n}')
#    print(f'Na função teste, x vale {x}')
#
#
# PROGRAMA PRINCIPAL
#n = 2
#print(f'No Programa principal, n vale {n}')
#teste()
#print(f'No programa principal, x vale {x}') # Aqui vai apresentar um erro, pois X só existe na função, chamamos isso de ESCOBO LOCAL, quando existe em ambas, ESCOBO GLOBAL, como N.
#
#
# Dentro da Função n1 vai ter o valor de 4 ou seja ESCOPO LOCAL
# Fora dela N1 vai ter o valor de 2 ou seja ESCOPO GLOBAL
#def função():
#    n1 = 4
#    print(f'N1 dentro vale {n1}')
#
#
#n1 = 2
#função()
#print(f'N1 fora vale {n1}')
#
# RETORNO DE VALORES
#
# return = s, Determina que o resultado da minha soma, possa ser atribuido a outras variáveis
# por exemplo r1 = 10 -> nova variável, quando quiser referir somente a resposta de r1, posso utiliza-lá isoladamente agora.
# r2 = 4 -> podendo ser utilizada isoladamente
# r3 = 6 -> podendo ser utilizada isoladamente
#
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1  = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')