#n1 = int(input('Digite um valor'))
#print(f'O dobro de {n1} é {n1*2}')
#print(f'O triplo de {n1} é {n1*3}')
#print(f'A raiz quadrade de {n1}é {n1**(1/2)}')

n1 = int(input('Digite um valor:'))
n2 = n1*2
n3 = n1*3
n4 = n1**(1/2)
n5 = pow(n1,(1/2))
# o n4 e n5 tem o mesmo resultados, são apenas duas maneiras de fazer potência
print(f'O dobro de {n1} é: {n2}')
print(f'O triplo de {n1} é: {n3}')
print(f'A raiz quadrada de {n1} é: {n4:.2f}')
print(f'A raiz quadrada com cod pow é: {n5:.2f}')

