travel = float(input('Qual a distância da viagem: '))
kmShort = 0.5*travel
kmLong = 0.45*travel
if travel <= 200:
    print(f'Sua viagem custará: R$ {kmShort}')
else:
    print(f'Sua viagem custará: R$ {kmLong}')