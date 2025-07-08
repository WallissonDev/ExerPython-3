pt = int(input('Digite o Primeiro Termo da PA : '))
ra = int(input('Digite a Razão da PA: '))
termos = 10
dez = pt + ra * termos
i = pt
proximo = 0
soma = 0
mais = 0
while mais != 1:
    proximo = i + ra
    i = proximo
    print(i)
    if i == dez + (ra * mais):
        mais = int(input('Termos: '))
        termos = + mais
        if mais == 0:
            exit()

















