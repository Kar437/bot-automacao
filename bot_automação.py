# Cria um bot para automação de tarefas
''' Passo 1: Entrar no sistema
    Passo 2: Fazer login
    Passo 3: Importar base de dados
    Passo 4: Cadastrar produtos'''

import pyautogui
from time import sleep
import pandas

pyautogui.PAUSE = 0.5 # Define uma pausa entre cada comando do PyautoGUI

# Dados
link = 'https://kar437.github.io/Site/pagina-cadastro/login.html'
email = 'teste@gmail.com'
senha = '12345678'
time = 3

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')


sleep(time)

# Maximiza a janela
pyautogui.hotkey('alt', 'space')
pyautogui.press('x')

# Entra no sistema
pyautogui.write(link)
pyautogui.press('enter')

sleep(time)

# Faz login
pyautogui.click(x=926, y=308)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('tab')
pyautogui.press('enter')

# Importar base de dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Cadastrar produtos
for linha in tabela.index:

    pyautogui.click(x=900, y=272)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
        pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)
    sleep(0.3)
