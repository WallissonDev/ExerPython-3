#def soma(a,b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma A + B = {s}')


# Programa Principal
#soma(b=4,a=5) # Podemos alterar a ordem de def dos valore utilizando as variáveis, como a = 5 e b = 4
#
# Outra possibilidade é a utilização do DESEMPACOTAR, representado por *
# Por exemplo, quando não sabemos quantos pârametros serão passados, utilizamos o DESEMPACOTAR:
#
#def contador (*num): # Enfase que essa linha cria uma tupla com os valores que contador recebe.
#    for valor in num:
#        print(valor, end ='')
#    print(' Fim')

#contador(2, 1, 7)
#contador(8, 0)
#contador( 4, 4, 7, 6, 2)
#
#def contador(*num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam}')


#contador(2, 1, 7)
#contador(8, 0)
#contador(2, 3 , 4)
#
# Aqui vamos criar uma função que dobra os valores dentro de uma lista:
#def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1


#valores = [6, 3, 9, 1, 0, 2]
#dobra(valores)
# print(valores)
# Sendo que, definimos a função dobra que rfecebe um parametro (lst)
# E entao quando passamos o valor de parametro sendo uma lista, ele executa o algoritmo.
#
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somano os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
