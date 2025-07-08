TOTAL = 0 # Variável que vai assumir valor da soma dos pares
COUNT = 0 # Variável que vai contar quantos números foram somados
for i in range(1,7): # Algoritmo de Loop de 1 a 6 para linha de comando a baixo
    NUMBER = int(input('Write a number: ')) # Valor atribuida pelo usuário
    if NUMBER % 2 == 0: # Se o resto da divisão por 2 for igual a 0 é par
        TOTAL += NUMBER # Se for par, soma esses valores dentro da variável TOTAL
        COUNT += 1 # Vai contar quantos pares foram digitados e somados.
print(TOTAL) # Apresenta o valor total da soma dos pares
print(COUNT) # Apresenta o valor total de quantos números foram somados.