import pandas as pd


def carregar_dados(caminho):
    dados = pd.read_csv(caminho, sep=";", encoding="utf-8")
    return dados
