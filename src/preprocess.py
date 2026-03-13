import pandas as pd


def limpar_dados(dados, target):
    dados = dados.dropna()

    x = dados.drop(target, axis=1)
    y = dados[target]

    return x, y
