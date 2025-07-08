#num = [2,5,9,1]
#num[2] = 3
#num.append(7) # adiciona o elemento 7 na lista
#num.sort(reverse = True) # Sort organiza em ordem, reverse = True inverte a ordem
#num.insert(2,0) # Na posição 2, adiciona o 0, podendo substituir o elemento presente
#num.pop(2) # somente pop(), elimina o ultimo elemento, se eu colocar pop(2) remove o 2
#num.remove(2) # Elimina o 2 que aparece pela primeira vez
#if 5 in num: # Se na minha lista tiver o elemento 5
#    num.remove(5) # Então ele remove.
#else:
#    print('Não achei o número 4')
#print(num)
#print(f'Essa lista tem {len(num)} elementos')
#valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)
#for v in valores:
    #print(f'{v}...', end = '')
#for cont in range(0,5):
#    valores.append(int(input('Digite um valor: ')) # Vai adicionar o elemento que o usuário inserir a lista, pra cada repetição
#for c, v in enumerate(valores): # Me mostra a posição do index e o elemento, sendo 'c' o index e 'v' o elemento.
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Final')
a = [2,3,4,7]
#b = a # Isso mantém as listas iguais, pois é uma ligação entre as listas
b = a[:] # Diferente daqui, onde b recebe todos os elementos da lista de a, não é uma ligação!, é uma cópia!
b[2] = 8 # Isso altera ambas as listas, exceto se não tiver ligação usando a[:]
print(f'Lista A {a}')
print(f'Lista B {b}')