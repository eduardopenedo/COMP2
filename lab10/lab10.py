# Nome: Eduardo Rodrigues Penedo
# DRE : 120043223

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")
def suites(freq):
    """
    Recebe um objeto Series com as frequencias e plota um gráfico de pizza delas, retorna um objeto Series de frequencias
    :param freq: Series
    :return: Series
    """
    fig,ax = plt.subplots()
    freq.plot.pie(ax= ax,autopct=r"%1.1f%%", startangle=0)
    plt.show()
    return freq


def area():
    """
    Plota as areas dos aparteamentos e retorna os dados dos imóveis com área igual à maior
    :return: DataFrame
    """
    fig, ax = plt.subplots()
    areas = dados["area"]
    areas.plot.hist(ax=ax, bins =20, color='green')
    plt.show()
    return dados[areas==areas.max()]

def procura(preco,area,condominio):
    """
    Plota os apartamentos com area maior, preço menor e condominio menor que os passados como parâmetro e retorna a frequencia
    dos bairros na listagem desses apartamentos.
    :param preco: int
    :param area: int
    :param condominio: int
    :return: Series
    """
    fig, ax = plt.subplots()

    areas = dados['area'] >= area
    precos = dados['preco'] <= preco
    condominios = dados['condominio'] <= condominio

    freq= dados[precos & areas & condominios]['bairro'].value_counts()

    freq.plot.bar(ax=ax, color='orange',rot=0)

    plt.show()
    return freq

freq = dados["suites"].value_counts()
print(type(freq))
print(suites(freq))
print(area())
print(procura(800000,60,1000))
