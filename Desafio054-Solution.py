from datetime import date
CURRENT_YEAR = date.today().year
AGGED = 0
MINOR = 0
for i in range (1,8):
    BIRTH_YEAR = int(input(f'Birth Year of {i} Person: '))
    AGE = CURRENT_YEAR - BIRTH_YEAR
    if AGE >= 18:
        AGGED += 1
    elif AGE < 18:
        MINOR += 1
print(f'Total of people above or equal 18 is {AGGED}')
print(f'Total of people under 18 is {MINOR}')