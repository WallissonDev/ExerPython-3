house = float(input('Valor da Casa: R$ '))
payment = float(input('Seu salário: R$ '))
time = float(input('Quantos anos de financiamento: '))
prestation = house / ( time * 12)
min = payment * 30 / 100
if prestation <= min:
    print(f'Aprovado: Mensalidade - R$ {prestation}, 30% - Salário Mensal R$ {min}')
elif prestation > min:
    print(f'Empréstimo Negado! Mensalidade - R$ {prestation} - 30% Salário Mensal - R$ {min}')
