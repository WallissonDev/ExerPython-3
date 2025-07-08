def notas(*n, sit=False):
    """"
    notas(*n, sit=False):
        -> Função que mostra notas dos alunos e avalia.
    :param *n: Dicionário com notas, médias e situação
    :param sit=False: Por padrão não mostra a situação
    :return boletim: Atribui a linha de código ao dicionário
    """
    boletim = dict()
    boletim['Total'] = len(n)
    boletim['Maior'] = max(n)
    boletim['Menor'] = min(n)
    boletim['Media'] = sum(n) / len(n)
    if sit:
        if boletim['Media'] >= 7:
            boletim['Situação'] = 'Boa'
        elif boletim['Media'] >= 5:
            boletim['Situação'] = 'Razoavel'
        else:
            boletim['Situação']= 'Ruim'
    return boletim


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit = True)
print(resp)