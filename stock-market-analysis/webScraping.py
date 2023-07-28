# Indicando o caminho da pasta download, ou da pasta em que os arquivos web são baixados em seu computado.
global caminho
caminho = "D:\\User\\Downloads\\"

# Baixando todas as bibliotecas usadas no código
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Baixando database bruta da web
navegador = webdriver.Chrome()
navegador.get('https://statusinvest.com.br/acoes/busca-avancada')

button_selector = '.find.waves-effect.waves-light.btn.btn-large.btn-main.fw-700.fs-3.pl-2.pr-2.pl-sm-3.pr-sm-3.tooltipped'
wait = WebDriverWait(navegador, 8)
button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
button_element.click()
time.sleep(2)
button_selector = 'a.btn-download.btn.btn-main-green.btn-small.waves-effect.waves-light'
wait = WebDriverWait(navegador, 5)
button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
button_element.click()

time.sleep(2)

navegador.close()

# Abrindo database no código
tabela = pd.read_csv(f"{caminho}statusinvest-busca-avancada.csv", sep=";")
#tabela = tabela.drop("CustomerID", axis=1)          #drop exclui uma linha ou coluna da tabela, axis = 0 para linha, axis = 1 para coluna.
#display(tabela)

# Removendo colunas não necessárias
tabela = tabela.drop(["P/ATIVOS", "PSR", "P/CAP. GIRO", "P/EBIT", "P. AT CIR. LIQ.", "MARGEM EBIT", "DIVIDA LIQUIDA / EBIT", "PASSIVOS / ATIVOS", "MARGEM BRUTA", "MARG. LIQUIDA", " VPA", " LPA", "GIRO ATIVOS"], axis=1)
#display(tabela.info())

# FILTROS - Nessa parte o usuário pode editar e filtrar os indicadores conforme seu perfil de investimento

tabela["DY"] = tabela["DY"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
tabela["P/L"] = tabela["P/L"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
tabela["P/VP"] = tabela["P/VP"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
tabela["EV/EBIT"] = tabela["EV/EBIT"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
tabela["ROIC"] = tabela["ROIC"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
tabela["DIV. LIQ. / PATRI."] = tabela["DIV. LIQ. / PATRI."].str.replace(",", ".").astype(float)
tabela["CAGR RECEITAS 5 ANOS"] = tabela["CAGR RECEITAS 5 ANOS"].str.replace(",", ".").astype(float)

tabela = tabela[(tabela["DY"] >= 4) & (tabela["DY"] <=16)]
tabela = tabela[(tabela["P/L"] >= 3) & (tabela["P/L"] <=20)]
tabela = tabela[tabela["P/VP"] <=5]
tabela = tabela[tabela["EV/EBIT"] <=12]
tabela = tabela[tabela["ROIC"] >= 12]
tabela = tabela[tabela["DIV. LIQ. / PATRI."] <= 6]

# Retirando tickers diferentes da mesma empresa
tabela["Ticker"] = tabela["TICKER"].str.extract(r'([A-Z]{4})')
duplicatas = tabela.duplicated(subset=["Ticker"], keep=False)
tabela = tabela[~duplicatas]

tabela = tabela.drop("Ticker", axis=1)
print("Número de linhas:", len(tabela))
#display(tabela)

# Salva em um arquivo.csv para melhor análise do usuário
tabela.to_csv("Indicadores atualizados.csv", index=False, sep=";")

# Exclui a database original para não dar erro quando for rodar novamente
if os.path.exists(f"{caminho}statusinvest-busca-avancada.csv"):
    os.remove(f"{caminho}statusinvest-busca-avancada.csv")
    print("Arquivo removido com sucesso.")
else:
    print("O arquivo não existe.")

