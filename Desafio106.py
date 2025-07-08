cores = {'Rosa' : '\033[0;30;45m',
         'Limpa' : '\033[0m',
         'Verde' : '\033[0;30;42m',
         'Branco' : '\033[0;30;46m'
         }


def visualPanel(msg):
    print(f'{cores['Rosa']}-{cores['Limpa']}'*len(msg))
    print((f'{cores['Rosa']}{msg}{cores['Limpa']}'))
    print(f'{cores['Rosa']}-{cores['Limpa']}'*len(msg))


visualPanel('  Bem-Vindo ao PyHELP!  ')
user = ''
while True:
    user = str(input(f'{cores['Verde']}Digite o comando que deseja saber o DOC: [FIM p/ Parar]: {cores['Limpa']}')).lower().strip()
    if user == 'fim':
        visualPanel('  Até Logo!  ')
        break
    visualPanel(f'  Acessando manual de >{user}<  ')
    print(cores['Branco'])
    print(help(user))
    print(cores['Limpa'])