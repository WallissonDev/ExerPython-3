#def fatorial(num = 1): # Caso o pârametro não receba valor, por padrão recebe 1
#    f = 1 # Escopo Local
#    for c in range(num, 0, -1):
#       f *= c
#    return f # Aqui determinamos que, o valor retornado pode ser atribuido a novas variáveis, como abaixo.

# Graças ao return f, atribuimos novas variáveis com o valor que a função gera
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f'Os resultados são {f1}, {f2} e {f3}')
#
def par(n=0): # Aqui criamos uma função que dizemos se o input é par
    if n % 2 == 0:
        return True # Se for, minha variável assume o valor de True.
    else:
        return False # Se não for, assume valor de False.

num = int(input('Digite um valor: '))
if par(num):
    print('É par')
else:
    print('Não é par!')



#num = int(input('Digite um número: ')) # Digito o valor
#print(par(num)) # Se for Par, aparece True

