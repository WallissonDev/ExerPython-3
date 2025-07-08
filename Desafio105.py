def notas(*n, sit = False):
    """
    notas(*n, sit = False)
       -> Recebe notas de Alunos, número de notas, maior e menor, media e situação
       :param n: Um x de parametros, sendo um dicionário com as notas e respectivas colocações
       :param sit: Opcional, para mostrar a situação da turma
       :return: Atribui a um dicionário.
    """
    maior = menor = 0
    boletim = dict()
    for p, v in enumerate(n):
        if p == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
    boletim['Total'] = len(n)
    boletim['Maior'] = maior
    boletim['Menor'] = menor
    boletim['Media'] = f'{sum(n)/len(n):.1f}'
    if sit:
        if boletim['Media'] >= '6':
            boletim['Situação'] = f'{boletim['Media']} = Aprovados'
        else:
            boletim['Situação'] = f'{boletim['Media']} = Reprovados'
    return boletim

turma1 = notas(3, 2, 1, 3, sit = False ) # Não mostra situação
turma2 = notas(10, 5, 9, 4, sit = True ) # Mostra a situação
turma3 = notas(5.4, 3.2, 9.5, 8.2, 6.9, sit = True) # Mostra Situação - Float
turma4 = notas(2.4, 3.2, 5.5, 3.2, 6.9, sit = True) # Mostra Situação - Float
print(f'Notas da Turma 1 : {turma1}')
print(f'Notas da Turma 2 : {turma2}')
print(f'Notas da Turma 3 : {turma3}')
print(f'Notas da Turma 4 : {turma4}')
help(notas)