import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def web (self, x, xx, path, variaveis):
    try:
        webScraping(x)
        tabela = pd.read_csv(f"{path}statusinvest-busca-avancada.csv", sep=";")

        if xx == "yes":
            tabela_filtrada = apply_specific_filters(x, tabela)
        else:
            tabela_filtrada = apply_custom_filters(x, variaveis, tabela)

        save_datas(path, tabela_filtrada)

    except Exception as e:
        print("Ocorreu um erro inesperado na execução do web", e)

def webScraping(x):
    driver = webdriver.Chrome()

    try:
        if x == "ação":
            driver.get('https://statusinvest.com.br/acoes/busca-avancada')
        else:
            driver.get('https://statusinvest.com.br/fundos-imobiliarios/busca-avancada')

        time.sleep(2)

        button_element = wait_for_clickable(driver, '.find.waves-effect.waves-light.btn.btn-large.btn-main.fw-700.fs-3.pl-2.pr-2.pl-sm-3.pr-sm-3.tooltipped')
        button_element.click()
        time.sleep(2)

        download_element = wait_for_clickable(driver, 'a.btn-download.btn.btn-main-green.btn-small.waves-effect.waves-light')
        download_element.click()
        time.sleep(2)

    except Exception as e:
        print("Ocorreu um erro inesperado na execução do webScraping", e)

    finally:
        driver.quit()


def wait_for_clickable(driver, selector, timeout=8):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))


def apply_specific_filters( x, tabela):
    try:
        if x == "ação":
            # Removendo colunas não necessárias
            tabela = tabela.drop(["P/ATIVOS", "PSR", "P/CAP. GIRO", "P/EBIT", "P. AT CIR. LIQ.", "MARGEM EBIT", "DIVIDA LIQUIDA / EBIT", "PASSIVOS / ATIVOS", "MARGEM BRUTA", "MARG. LIQUIDA", " VPA", " LPA", "GIRO ATIVOS"], axis=1)
            indicadores = ["DY", "P/L", "P/VP", "ROIC", "CAGR RECEITAS 5 ANOS", "EV/EBIT", "DIV. LIQ. / PATRI."]

            for indicador in indicadores:
                tabela[f"{indicador}"] = tabela[f"{indicador}"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)

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

        else:
            tabela = tabela
            indicadores = ["DY", "CAGR DIVIDENDOS 3 ANOS", "P/VP", " CAGR VALOR CORA 3 ANOS"]

            for indicador in indicadores:
                tabela[f"{indicador}"] = tabela[f"{indicador}"].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)

            tabela = tabela[(tabela["DY"] >= 8) & (tabela["DY"] <=20)]
            tabela = tabela[tabela["P/VP"] <=1.6]
            tabela = tabela[tabela["CAGR DIVIDENDOS 3 ANOS"] >=6]

    except Exception as e:
        print("Ocorreu um erro inesperado na execução do apply_specific_filters", e)

    return tabela



def apply_custom_filters(x, variaveis, tabela):
    try:
        if x == "ação":
            tabela = tabela.drop(["PSR",   "P. AT CIR. LIQ.",  "DIVIDA LIQUIDA / EBIT",  "MARGEM BRUTA",  " VPA", " LPA", "GIRO ATIVOS"], axis=1)
            indicadores = ["DY", "P/L", "P/VP", "MARGEM EBIT", "MARG. LIQUIDA", "P/EBIT", "P/CAP. GIRO", "DIV. LIQ. / PATRI.", "ROE", "ROA", "ROIC", "P/ATIVOS", "PASSIVOS / ATIVOS", "CAGR RECEITAS 5 ANOS", "CAGR LUCROS 5 ANOS", " LIQUIDEZ MEDIA DIARIA", " PEG Ratio", " VALOR DE MERCADO"]

            for i in range(len(variaveis)):
                variaveis[i][0] = indicadores[i]

            # Loop para percorrer a matriz variaveis
            for indicador, minValue, maxValue in variaveis:
                tabela[indicador] = tabela[indicador].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
                if minValue and maxValue:
                    tabela = tabela[(tabela[indicador] >= float(minValue)) & (tabela[indicador] <= float(maxValue))]
                elif minValue:
                    tabela = tabela[(tabela[indicador] >= float(minValue))]
                elif maxValue:
                    tabela = tabela[(tabela[indicador] <= float(maxValue))]

            # Retirando tickers diferentes da mesma empresa
            tabela["Ticker"] = tabela["TICKER"].str.extract(r'([A-Z]{4})')
            duplicatas = tabela.duplicated(subset=["Ticker"], keep=False)
            tabela = tabela[~duplicatas]
            tabela = tabela.drop("Ticker", axis=1)

        else:
            tabela = tabela.copy()
            indicadores = ["DY", " N COTAS", "CAGR DIVIDENDOS 3 ANOS", "LIQUIDEZ MEDIA DIARIA", "P/VP", "ULTIMO DIVIDENDO", " CAGR VALOR CORA 3 ANOS", "VALOR PATRIMONIAL COTA"]

            for i in range(len(variaveis)):
                variaveis[i][0] = indicadores[i]

            # Loop para percorrer a matriz variaveis
            for indicador, minValue, maxValue in variaveis:
                tabela[indicador] = tabela[indicador].str.replace(".", "", regex=True).str.replace(",", ".").astype(float)
                if minValue and maxValue:
                    tabela = tabela[(tabela[indicador] >= float(minValue)) & (tabela[indicador] <= float(maxValue))]
                elif minValue:
                    tabela = tabela[(tabela[indicador] >= float(minValue))]
                elif maxValue:
                    tabela = tabela[(tabela[indicador] <= float(maxValue))]

    except Exception as e:
        print("Ocorreu um erro inesperado na execução do apply_custom_filters", e)

    return tabela


def save_datas(path, tabela):
    tabela.to_csv("Indicadores atualizados.csv", index=False, sep=";", decimal=',')

    if os.path.exists(f"{path}statusinvest-busca-avancada.csv"):
        os.remove(f"{path}statusinvest-busca-avancada.csv")
        print("Arquivo removido com sucesso.")
    else:
        print("O arquivo não existe.")

