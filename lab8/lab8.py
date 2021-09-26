# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

import numpy as np
import matplotlib.pyplot as plt

def racional(n):
    """
    Plota os gráficos de 1/x e 1/x^2 no intervalo [0.1,2.0] dividido em n partes
    :param n: int
    :return: None
    """
    x = np.linspace(0.1,2,n)
    y = 1/x
    z = 1/(x**2)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_title("Funções racionais")

    ax.plot(x,y,'c-s', linewidth=2, label=r'$y=\frac{1}{x^{2}}$')
    ax.plot(x, z, 'm-o', linewidth=2, label=r'y=$\frac{1}{x}$')
    ax.legend(loc=1)
    ax.set_xticks([0,1,2])
    plt.show()


def polinomios(grau_max):
    """
    Plota os gráficos x**i, onde 1<i<grau_max e x está no intervalo [-1,1] dividido em 100 partes
    :param grau_max: int
    :return: None
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.set_xticks([-1,0,1])
    ax.set_yticks([-1,0,1])

    x = np.linspace(-1,1,100)
    i = np.linspace(1,grau_max,grau_max)

    for exp in i:
        ax.plot(x,x**exp,'-', linewidth=2, label=f"$x**{int(exp)}$")
        ax.legend(loc=4)

    plt.show()

def fun(a,b,n):
    """
    Plota o gráfico de 1/sin(x), onde sin(x)>0 e que estão entre o intervalo [-20,20]. Retorna os pontos em que o y é descontínuo
    :param a:int
    :param b:int
    :param n:int
    :return: list
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    x = np.linspace(a,b,n)
    x1 = x[np.sin(x)!=0]
    cossec = 1/np.sin(x1)
    x2 = x1[cossec<20]
    cossec1 = cossec[cossec<20]
    x3 = x2[cossec1 >-20]
    cossec2 = cossec1[cossec1>-20]

    pos = np.where(np.abs(np.diff(cossec2)) >= 1.0)[0]
    # x = np.insert(x3,pos,np.nan)
    # y = np.insert(cossec2,pos,np.nan)

    x3[pos] = np.nan
    cossec2[pos] = np.nan

    ax.plot(x3, cossec2, '-co',label=r'y=$\frac{1}{\sin(x}$')
    ax.legend(loc=9)
    plt.show()
    return pos


racional(5)
racional(30)
polinomios(5)
print(fun(0,10,100))