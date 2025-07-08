times = ('Palmeiras', 'Santos', 'Flamengo',
         'Corinthians', 'São Paulo', 'Cruzeiro',
         'Fluminense','Vasco', 'Internacional',
         'Atletico','Botafogo','Bahia','Grêmio',
         'Coritiba','Chapecoense','Guarani')
print('='*20)
print(f'Os 5 primeiros times: {times[0:5]}')
print('='*20)
print(f'Os 4 ultimos times: {times[-4:]}')
print('='*20)
print(f'Ordem alfabética: {sorted(times)}')
print('='*20)
print(f'O Chapecoense está na posição: {times.index('Chapecoense')+1}')
print('='*20)