numeros = ('Zero','Um','Dois','Três','Quatro'
           ,'Cinco','Seis','Sete','Oito'
           ,'Nove','Dez','Onze','Doze',
           'Treze','Catorze','Quinze',
           'Dezesseis','Dezessete','Dezoito',
           'Dezenovo','Vinte')
while True:
    user = int(input('Digite um número de 0 a 20: '))
    if 0 <= user <= 20:
        break
    else:
        print('Valor inválido.')
print(f'Você digitou o número: {numeros[user]}')
