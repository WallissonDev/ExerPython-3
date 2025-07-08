TOTAL = 0 # Variável que atribui o total das somas
COUNT = 0 # Variável que conta quantos valores foram somados
for i in range(1,501, 2): # De 1 a 500, pulando os pares
    if i % 3 == 0: # Se o resto da divisão por 3 ( multiplo de 3 ) for 0, então:
        TOTAL += i # Soma os números
        COUNT += 1 # Soma 1 pra cada valor somado anteriormente
print(TOTAL) # Apresenta o total da soma dos números impares multiplos de 3
print(COUNT) # Apresenta quantas somas foram