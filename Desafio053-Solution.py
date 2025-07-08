PHRASE = str(input('Write a Phrase: ')).upper().strip()
ORDER = PHRASE.split()
FIX = ''.join(ORDER)
INVERTED_PHRASE = ''
for LETTERS in range(len(FIX) -1, -1, -1):
    INVERTED_PHRASE += FIX[LETTERS]
if INVERTED_PHRASE == FIX:
    print('É um palindromo')
    print(f'O inverso de = {FIX} é = {INVERTED_PHRASE}')
else:
    print('Não é um palindromo')
    print(f'O inverso de = {FIX} é = {INVERTED_PHRASE}')

