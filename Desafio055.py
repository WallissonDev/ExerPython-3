LOW_WEIGHT = 0 # Vai guardar a informação de quem pesa menos
HIGH_WEIGHT = 0 # Vai guardar a informação de quem pesa mais
for i in range(1,6): # O i iterador, vai repetir de 1 a 5 os algoritmos
    WEIGHT = float(input('Write you Weight: ')) # Atribuirá pelo usuário valor de peso 5 vezes na variável
    if i == 1: # Assim que o iterador estiver na posição 1 ele executá a linha abaixo
        HIGH_WEIGHT = WEIGHT # Vai gravar a informação de WEIGHT na primeira vez que for digitado
        LOW_WEIGHT = WEIGHT # Vai gravar a informação de WEIGHT na primeira vez que for digitado
    else: # Assim que o iterador estiver na posição 2, o else ativa.
        if WEIGHT > HIGH_WEIGHT: # se o iterador da posição 1 (HIGH_WEIGHT) que agora possuí o peso da posição 1, for menor que o da posição 2
            HIGH_WEIGHT = WEIGHT # Então o iterador da posição 2 recebe o peso
        if WEIGHT < LOW_WEIGHT: # o inverso de acima
            LOW_WEIGH = WEIGHT # Atribui o menor valor
print(f'{LOW_WEIGHT}')  # Apresenta o menor peso
print(f'{HIGH_WEIGHT}') # Apresenta o maior peso