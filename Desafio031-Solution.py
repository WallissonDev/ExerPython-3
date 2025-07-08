#dist = int(input('Digite a distância em km: '))
#kmShort = dist*0.5
#kmLong = dist*0.45
#if dist <= 200:
#    print(f'O preço da sua viagem é de R$ {kmShort}')
#else:
#    print(f'O preço da sua viagem é de R$ {kmLong}')
#
# Forma 2
#
distance = float(input('Qual é a distância da sua viagem: '))
print(f'Você está prestes a começar uma viagem de {distance:.2f}km')
price = distance * 0.50 if distance <= 200 else distance * 0.45
print(f'E o preço da sua passagem será de R${price:.2f}')
