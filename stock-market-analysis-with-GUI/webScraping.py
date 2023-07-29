import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def web (self, x, xx, path):
# Baixando database bruta da web
    navegador = webdriver.Chrome()

    if x == "ação":
        navegador.get('https://statusinvest.com.br/acoes/busca-avancada')
    else:
        navegador.get('https://statusinvest.com.br/fundos-imobiliarios/busca-avancada')

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
    tabela = pd.read_csv(f"{path}statusinvest-busca-avancada.csv", sep=";")

# Aplicando filtros
    if x == "ação":
        if xx == "yes":
            # Removendo colunas não necessárias
            tabela = tabela.drop(["P/ATIVOS", "PSR", "P/CAP. GIRO", "P/EBIT", "P. AT CIR. LIQ.", "MARGEM EBIT", "DIVIDA LIQUIDA / EBIT", "PASSIVOS / ATIVOS", "MARGEM BRUTA", "MARG. LIQUIDA", " VPA", " LPA", "GIRO ATIVOS"], axis=1)
            # Filtros
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
        else:
            print("pass, no")

        # Retirando tickers diferentes da mesma empresa
        tabela["Ticker"] = tabela["TICKER"].str.extract(r'([A-Z]{4})')
        duplicatas = tabela.duplicated(subset=["Ticker"], keep=False)
        tabela = tabela[~duplicatas]
        tabela = tabela.drop("Ticker", axis=1)



    else:
        print("fiis")
        if xx == "yes":
            tabela = tabela.drop([" N COTAS", "N COTISTAS", "PERCENTUAL EM CAIXA", "ULTIMO DIVIDENDO", " CAGR VALOR CORA 3 ANOS"], axis=1)
            tabela["DY"] = tabela["DY"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
            tabela["P/VP"] = tabela["P/VP"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
            tabela["CAGR DIVIDENDOS 3 ANOS"] = tabela["CAGR DIVIDENDOS 3 ANOS"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
            tabela = tabela[(tabela["DY"] >= 8) & (tabela["DY"] <=20)]
            tabela = tabela[tabela["P/VP"] <=1.6]
            tabela = tabela[tabela["CAGR DIVIDENDOS 3 ANOS"] >=6]
#            tabela["DY"] = tabela["DY"].replace(".", ",")
#            tabela["P/VP"] = tabela["P/VP"].replace(".", ",")
            print("yes")
        else:
            print("no")


    # Salva em um arquivo.csv para melhor análise do usuário
    print(12)
    tabela.to_csv("Indicadores atualizados.csv", index=False, sep=";")

    # Exclui a database original para não dar erro quando for rodar novamente
    if os.path.exists(f"{path}statusinvest-busca-avancada.csv"):
        os.remove(f"{path}statusinvest-busca-avancada.csv")
        print("Arquivo removido com sucesso.")
    else:
        print("O arquivo não existe.")

