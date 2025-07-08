from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    print('-=' * 12)
    if idade < 18:
        return print(f'Com {idade} não pode votar.')
    elif idade >= 65:
        return print(f'Com {idade} é opcional votar.')
    else:
        return print(f'Com {idade} é obrigatório votar.')


r1 = int(input('Digite o ano de Nascimento: '))
voto(r1)