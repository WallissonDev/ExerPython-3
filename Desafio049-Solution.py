wwwwwwwwwwwwwwwwwwwNUMBER = int(input('Write a Number: ')) # Usuário atribui um valor integer a variável NUMBER
for i in range(1,11): # Iterador fará operação de 1 a 10.
    TABLE = i*NUMBER # Variável opcional, deixa o código mais compreensível
    print(f'{i}x{NUMBER} = {TABLE}') # Escreve a operação do iterador multiplicado pelo valor atribuido pelo usuário
# Podemos também eliminar a variável table, colocando diretamente dentro do format {i*NUMBER}


