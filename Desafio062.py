primeiro = int(input('Primeiro termo da PA: '))
ra = int(input('Razão da PA: '))
soma = 0
dezt = primeiro + ra * 10
for i in range(primeiro, dezt, ra):
    print(i)
    soma += ra
    if soma == ra*10:
        mais = int(input('Mais termos ou 0 para finalizar: '))
        proximo = 0
        junto = 0
        primeiro_termo = primeiro
        total = dezt + ra * mais
        if mais != 0:
            while proximo != total:
                proximo = primeiro_termo + ra
                primeiro_termo = proximo
                proximo += ra
                print(proximo+ra)
        elif mais == 0:
             exit()







