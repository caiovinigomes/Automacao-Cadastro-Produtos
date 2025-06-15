# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa, consideramos o endereço abaixo (criado para fins didáticos)
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pygetwindow as gw # Importando a biblioteca para interagir com janelas
from pyautogui import FailSafeException # Importa a exceção de segurança do pyautogui

pyautogui.PAUSE = 0.5

# abrir o navegador
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
time.sleep(1)

chrome_window = None
try:
    windows = gw.getWindowsWithTitle('Chrome')
    if windows: # Verifica se alguma janela foi encontrada
        chrome_window = windows[0] # Pega a primeira janela encontrada

        if chrome_window.isMaximized:
            pass          
        else:
            print("A janela do Chrome não está maximizada. Maximizando agora...")
            pyautogui.hotkey('win', 'up') # Atalho para maximizar a janela
            time.sleep(0.4) # Pequena pausa para a maximização ocorrer
except Exception: # Captura qualquer erro que ocorra no bloco try
    pass

# entrar no link
pyautogui.click(x=523, y=76)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') # site desenvolvido com fins didáticos e pode não estar mais disponível, conforme orientação no README do projeto
time.sleep(3.2)

# Passo 2: Fazer login
# selecionar o campo de email

pyautogui.press('tab')
pyautogui.write("teste@teste.com")
pyautogui.press('tab')
pyautogui.write('Suasenhaaqui')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(0.7)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("1. Projeto Automacao com PHYTON/produtos.csv")# Aqui coloque o endereço da pasta produtos

print(tabela)

# clicar no campo de código
pyautogui.press('tab')

# Passo 4: Cadastrar um produto Mouse
# O loop de cadastro está dentro de um bloco try-except para capturar interrupções
try:
    for linha in tabela.index: 
        pyautogui.click(x=851, y=315)
 
        # pegar da tabela o valor do campo que a gente quer preencher
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(codigo)

        pyautogui.press('tab')
        marca = tabela.loc[linha, "marca"]
        pyautogui.write(marca)

        pyautogui.press('tab')
        tipo = tabela.loc[linha, "tipo"]
        pyautogui.write(tipo)

        pyautogui.press('tab')
        categoria = str(tabela.loc[linha, "categoria"])
        pyautogui.write(categoria)

        pyautogui.press('tab')
        preco_unitario = str(tabela.loc[linha, "preco_unitario"])
        pyautogui.write(preco_unitario)

        pyautogui.press('tab')
        custo = str(tabela.loc[linha, "custo"])
        pyautogui.write(custo)
    
        pyautogui.press('tab')
        obs = str((tabela.loc[linha, "obs"]))

        if obs != "nan":
            pyautogui.write(str(tabela.loc[linha, "obs"]))
        
        pyautogui.press("tab")
        pyautogui.press("enter") # cadastra o produto (botao enviar)
        # dar scroll de tudo pra cima
        pyautogui.scroll(10000)
        # Passo 5: Repetir o processo de cadastro até o fim

except FailSafeException:
    # Esta exceção é levantada quando o usuário move o mouse para o canto superior esquerdo da tela (0,0)
    print("\nERRO: Você interrompeu o processo de cadastro do robô!")