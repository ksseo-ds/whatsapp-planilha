from mensagemwpp import *
from mensagemwpp import Navegador
import pandas as pd
import openpyxl
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


print(ChromeDriverManager().install())

publico_df = pd.read_excel('Agenda.xlsx')
publico_df['mensagem'] = publico_df['mensagem'].astype("object")


############################## Mensagem e envio pela classe ################################
msg = """ 

teste

"""


service = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(service=service, options=options)
navegador.implicitly_wait(20)
naveg = Navegador(navegador)

naveg.modulo_wpp()

envios, erros = naveg.enviar_mensagens(publico_df,msg) #inclui o instanciamento para tentar o retorno dos erros e dos envios

envios
erros