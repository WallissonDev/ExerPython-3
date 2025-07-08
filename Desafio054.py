from datetime import date
OF_AGE = 0
UNDER_AGE = 0
CURRENT_YEAR = date.today().year # Função que considera o ano atual.
for i in range (1,8): # De 1 a 7, vai perguntar ano de nascimento da pessoa.
    YEAR_BORN = int(input('Write the year of birth: ')) # O usuário digitará 7 anos de nascimento.
    if CURRENT_YEAR - YEAR_BORN >= 18: # Se o usuário tiver 18 ou mais, ele é maior de idade
        OF_AGE += 1 # E aqui ele acrescenta um contador, pra cada 1 que for maior de idade.
    elif CURRENT_YEAR - YEAR_BORN < 18: # Se o usuário tiver menos de 18, ele é menor de idade.
        UNDER_AGE += 1 # E aqui ele acrescenta um contador, pra cada 1 que for menor de idade.
print(f'Total of people of age: {OF_AGE}') # Mostra Quantos são maiores
print(f'Total of people under age: {UNDER_AGE}') # Mostra quantos são menores.
