PHRASE = str(input('Digite uma Frase: ')).strip().upper() # Variable recive phrase in upper case, eliminate spaces.
NO_S_PHRASE = PHRASE.replace(' ', '') # Remove the spaces between words and letters.
FRONT_PHRASE = NO_S_PHRASE[0:] # Not Necessary, just for comparasion, shows the PHRASAE in correct form.
INVERTED_PHRASE = NO_S_PHRASE[::-1] # Make the PHRASE inverted.
for i in range(len(NO_S_PHRASE)): # i is a counter, current making every letter to be comparated, in PHRASE original form and inverted.
    if FRONT_PHRASE[i] == INVERTED_PHRASE[i]: # if every letter is equal in every position, normal and inverted PHRASE
        print(f'A frase >{PHRASE}< ao contrário fica >{PHRASE[::-1]}<')
        print(f'Sem espaço >{NO_S_PHRASE}< invertida sem espaço >{NO_S_PHRASE[::-1]}<')
        print('Portanto é um Polindromo.')
        exit()
    else:
        print(f'A frase >{PHRASE}< invertida fica >{PHRASE[::-1]}<') # if's it not everthying equal.
        print('Portanto não é um Polindromo.')
        exit()


