frase = str(input('Digite um Frase: ')).upper().strip()
frase1 = frase.replace('á','A')
print(f'A letra A aparece na frase {frase.count('A')+1}')
print(f'Aparece na primeira vez: {frase1.find('A')+1}')
print(f'Aparece na ultima vez: {frase.rfind('A')+1}')
# Guanabara utilizou +1 pra corrigir a posição do Python pra que ele desconidere o inicio por 0
