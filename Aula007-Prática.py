#nome = input('Qual seu nome')
#print(f'Prazer em te conhecer {nome:=^20}!')
n1 = int(input('Digite um valor'))
n2 = int(input('Diigite outro valor:'))
s = n1 + n2
s2 = n1 - n2
s3 = n1 / n2
s4 = n1 * n2
s5 = n1 ** n2
s6 = n1 // n2
s7 = n1 % n2
print(f'A soma é {s} \n a subtração é {s2} \n o produto {s3:.2f} \n o resto de {s4:.2f}', end=' >>> ')
print(f'O resultado da potência: {s5:.2f} o resultado da divisão inteira: {s6:.2f}', end= ' >>> ')
print(f'O resto da divisão:{s7:.2f}')
# Eu só devo usar outra variável se eu precisar do resultado para depois
# os vários s2 são essas outras variáveis que eu vou querer o resultado posterior
# posso usar a , e o comando end=' ' para juntar duas prints
# posso usar a contrabarra \n para quebrar a linha no meio
# também posso usar o :.2f ou outro valor pra nunca mostrar todos os decimais
# ponto a constar é que .2f vai fazer com que seja float em vez de int
# no end posso colocar simbolos entre as '' para simbolizar como quero a quebra de linha