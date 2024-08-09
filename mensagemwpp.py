from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.parse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from random import randint

class Navegador:
    def __init__(self, navegador):
        self.navegador = navegador

    def modulo_wpp(self): 
        time.sleep(3)
        self.navegador.get("https://web.whatsapp.com/")
        return self.navegador
        
    def enviar_mensagens(self, contatos_df, mensagem):   
        contatos_df.reset_index(drop=True, inplace=True)
        enviados = []
        erros = []
        for i, cod_cliente in enumerate(contatos_df['codigo']):
            try:
                sleeprange = randint(19,33)
                pessoa = contatos_df.loc[i, "nome"]
                numero = contatos_df.loc[i, "telefone"]
                texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
                link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"

                self.navegador.get(link)
                time.sleep(sleeprange)

                # Aguarde até que o campo de entrada de mensagem seja visível
                mensagem_input = WebDriverWait(self.navegador, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'))
                )
                mensagem_input.send_keys(Keys.ENTER)
                enviados.append(cod_cliente)  # Corrigido: Cod_Cliente para cod_cliente
                time.sleep(3)
                
            except Exception as e:
                erros.append(cod_cliente)  # Corrigido: Cod_Cliente para cod_cliente
                print(f"Erro ao enviar mensagem para {pessoa}: {str(e)}")
                continue
        return enviados, erros
    
    def teste(self):
        link = 'https://www.google.com'
        self.navegador.get(link)
