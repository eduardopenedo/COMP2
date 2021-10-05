# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

def alturas(n):
    """
    Plota o gráfico de alturas em um histograma, salva a imagem e retorna o ndarray das alturas.
    Parameters
    ----------
    n int

    Returns np.ndarray
    -------

    """
    fig, ax = plt.subplots()
    ax.set_title("Alturas")
    alturas = st.norm.rvs(loc = 1.7, scale = 0.08, size = n)
    ax.hist(alturas, bins =20)

    plt.savefig("alturas.png")
    plt.show()
    return alturas


def pesos(m):
    """
    Plota o gráfico de pesos em um histograma, salva a imagem e retorna o ndarray de pesos.
    Parameters
    ----------
    m np.ndarray

    Returns np.ndarray
    -------

    """
    fig, ax = plt.subplots()
    ax.set_title("Pesos")
    imc = st.norm.rvs(loc = 24.5, scale = 4.3, size = len(m))
    peso = imc * m ** 2

    ax.hist(peso, bins =20, facecolor='m')

    plt.savefig("pesos.png")
    plt.show()
    return peso

def regressaoLinearl(altura, peso):
    """
    Plota o grafico de regressão linear
    Parameters
    ----------
    altura np.ndarray
    peso np.ndarray

    Returns None
    -------

    """
    fig, ax = plt.subplots()
    plt.scatter(altura,peso,marker='o')


    a,b = st.linregress(altura, peso)
    y = a * altura + b
    ax.plot(altura,y,'r-')

    ax.set_title("Altura vs Peso")
    plt.xlabel("Alturas")
    plt.ylabel("Pesos")

    plt.savefig("regressao.png")
    plt.show()

altura = alturas(100)
peso = pesos(altura)
regressaoLinearl(altura, peso)