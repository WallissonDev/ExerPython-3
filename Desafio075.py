tupla = () # Aqui eu defino que a variável tupla é uma tupla
tupla_par = () # Aqui eu defino que a variável tupla é uma tupla
for i in range(1,5): # Estrutura de Repetição com Variável de Controle
    valor = int(input('Digite um valor: ')) # 4x - Usuário insere um valor integro a cada iteração
    tupla += valor, # Junta todos os valores digitados dentro de tupla, utilizando a , podemos criar a tupla.
for c in tupla: # C representa cada elemento da iteração dentro da tupla
    if c % 2 == 0: # se o elemento dentro da tupla, localizado no indice pelo C, tiver o resto da divisão por 2 igual a 0 é par
        tupla_par += c, # Se isso acontecer, soma na variável tupla_par
a = tupla.count(9) # Conta quantas vezes o valor 9 aparece ( enfase que valor e número são diferentes )
c = tupla_par # Apenas para facilitar a visualização, basicamente uma variável repetida.
if 3 in tupla: # Se tiver 3 na minha tupla
    b = tupla.index(3) # Me mostra em que posição está o meu elemento 3 pela primeira vez
    print(f'O valor 3 está na posição: {b+1}') # E apresenta a posição do elemento.
else: # Se não
    print('O número 3 não apareceu!') # Apresenta que não apareceu.
print(f'O valor 9 apareceu : {a}')
print(f'Os números pares foram: {c}')
t = tupla.count(3) # Conta quantas vezes o 3 aparece na tupla
if t >= 1: # Se for igual ou maior que 1, ele mostra a posição.
    print(f'O valor 3 está na posição: {tupla.index(3)+1}') # o +1 é apenas pra mostrar uma posição mais real, em vez de partir do 0 vai partir do 1.
else: # Se não, ele avisa que não aparece.
    print(f'O valor 3 não aparece.')