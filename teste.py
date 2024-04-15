import tkinter as tk
from tkinter import messagebox
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import datetime




def fazer_login_automatico():
    # Verifica o horário atual
    # agora = datetime.now().time()

    # Converte os horários de início e fim para objetos de tempo
    # hora_inicio = datetime.strptime(hora_inicio_entrada.get(), "%H:%M").time()
    #almoco_inicio = datetime.strptime(almoco_inicio, "%H:%M").time()
    #almoco_fim = datetime.strptime(almoco_fim, "%H:%M").time()
    #hora_fim = datetime.strptime(hora_fim, "%H:%M").time()
    login = login_entrada.get()
    senha = senha_entrada.get()
    hora_inicio = hora_inicio_entrada.get()
    print(url, login, senha, hora_inicio)
    print(xpath_campo_login, xpath_campo_senha, xpath_botao_login)


    # Verifica se está no intervalo de horário de login
    # if hora_inicio == agora:
        # Realiza o login automaticamente
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service)
    navegador.get(url)
    navegador.find_element("xpath",xpath_campo_login).send_keys(login)
    navegador.find_element("xpath",xpath_campo_senha).send_keys(senha)


    sleep(5)
    navegador.find_element("xpath",xpath_botao_login).click()




    # elif almoco_inicio <= agora <= almoco_fim:
    #     # Se estiver no horário do almoço, faça algo
    #     print("É hora do almoço!")
    # else:
    #     # Fora do horário de trabalho
    #     print("Não é hora de fazer login.")

#variaveis
url = "https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium"
xpath_campo_login = '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input'
xpath_campo_senha = '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input'
xpath_botao_login = '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button'


login = "Bruno Kobi Valadares de Amorim"
senha = ""
hora_inicio = "22:49"
almoco_inicio = "20:00"
almoco_fim = "20:30"
hora_fim = "22:00"


# Criando a janela principal
janela = tk.Tk()
janela.title("Ponto automático")

# Criando os elementos da interface

# Label e Entry para o login
login_label = tk.Label(janela, text="Login:")
login_label.grid(row=0, column=0)
login_entrada = tk.Entry(janela, width=50)
login_entrada.grid(row=0, column=1)

# Label e Entry para a senha
senha_label = tk.Label(janela, text="Senha:")
senha_label.grid(row=1, column=0)
senha_entrada = tk.Entry(janela, width=50)
senha_entrada.grid(row=1, column=1)

# Label e Entry para a hora de início
hora_inicio = tk.Label(janela, text="Hora de início:")
hora_inicio.grid(row=2, column=0)
hora_inicio_entrada = tk.Entry(janela, width=50)
hora_inicio_entrada.grid(row=2, column=1)

# Label e Entry para a hora de início do almoço
almoco_inicio = tk.Label(janela, text="Hora de início do almoço:")
almoco_inicio.grid(row=3, column=0)
almoco_inicio_entrada = tk.Entry(janela, width=50)
almoco_inicio_entrada.grid(row=3, column=1)

# Label e Entry para a hora de fim do almoço
almoco_fim = tk.Label(janela, text="Hora de fim do almoço:")
almoco_fim.grid(row=4, column=0)
almoco_fim_entrada = tk.Entry(janela, width=50)
almoco_fim_entrada.grid(row=4, column=1)

# Label e Entry para a hora de fim
hora_fim = tk.Label(janela, text="Hora de fim:")
hora_fim.grid(row=5, column=0)
hora_fim_entrada = tk.Entry(janela, width=50)
hora_fim_entrada.grid(row=5, column=1)


botao_enviar = tk.Button(janela, text="OK", command=fazer_login_automatico)
botao_enviar.grid(row=7, columnspan=2)

# Iniciando o loop principal da interface
janela.mainloop()


