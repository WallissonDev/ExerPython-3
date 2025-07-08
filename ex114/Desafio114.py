import webbrowser
from webbrowser import open_new_tab, open

url = 'https://www.pudim.com.br'
try:
    open_new_tab(url)
except webbrowser.Error:
    print('Erro Para acessar!')
else:
    print('Site acessado com sucesso!')