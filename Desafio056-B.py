YOUNG_WOMANS = 0 # Variável que assume valor de 0
AGE_GROUP_MEDIAN = 0 # Variável que assume valor de 0
YOUNG_MAN = 0 # Variável que assume valor de 0
OLDER_MAN_NAME = 0 # Variável que assume valor de 0
OLDER_MAN_AGE = 0 # Variável que assume valor de 0
for i in range (1,3): # Iterador i contará de 1 a 4, atribuindo valores as variáveis abaixo:
    NAME = str(input('Write your name: ')) # Nome do indivíduo
    AGE = int(input('Write your age: ')) # Idade do indivíduo
    SEX = str(input('Write your sex: ')).upper().strip() # Sexo do indivíduo
    AGE_GROUP_MEDIAN += AGE # Toda vez que um valor for atribuido a AGE, somará na variável
    if SEX == 'WOMAN' and AGE < 20: # Se o SEX for 'WOMAN' e a AGE abaixo de 20
        YOUNG_WOMANS += 1 # Então a Variável YOUNG_WOMANS ganha +1]
    if SEX == 'MAN': # Se o SEX for 'MAN'
        if AGE > OLDER_MAN_AGE: # Se a AGE for maior que OLDER_MAN_AGE então:
            OLDER_MAN_AGE = AGE # OLDER_MAN_AGE recebe a AGE nova e maior, ou mantém se já for.
            OLDER_MAN_NAME = NAME # OLDER_MAN_NAME recebe o NAME do mais velho ou mantém se já for.
print(f'The name of older man is: {OLDER_MAN_NAME}') # Escreve o NAME do homem mais velho
print(f'The age of older man is: {OLDER_MAN_AGE}') # Escreve a AGE do homem mais velho
print(f'The Group Median Age is: {AGE_GROUP_MEDIAN/2:.2f}') # Após dividir todas AGE por 2 pega a média de AGE do AGE_GROUP_MEDIAN
print(f'There is a {YOUNG_WOMANS} Young Woman less then 20 years.') # Escreve quantas WOMAN tem menos de 20 anos





