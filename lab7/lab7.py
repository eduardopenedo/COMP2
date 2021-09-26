# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

import math
import numpy as np

def senoPositivo(a,b,n):
    """
    Retorna os elementos x de n pontos no intervalo de a até b
    :param a: int
    :param b: int
    :param n: int
    :return: np.ndarray
    """
    x = np.linspace(a,b,n)
    sin = np.sin(x)
    zero = np.zeros(x.shape)
    return x[sin>0]


def polinomio(arr, z):
    """
    Calcula o resultado de um polinômio do somatório dos elementos do array com k inicial igua a 0, que é definido por ak * z **k
    :param arr: np.ndarray
    :param z: int
    :return: float
    """
    contagem = np.linspace(0,len(arr)-1,len(arr))
    elevado = z ** contagem
    return sum(np.cumprod([arr,elevado],axis=0)[1])

def ortogonal(matriz):
    """
    Retorna True se a matriz inversa é igual a matriz transposta, caso ocorra erro ou as matrizes sejam diferentes, retorna False
    :param matriz: np.ndarray
    :return: bool
    """
    try:
        matriz_transp = np.transpose(matriz)
        matriz_inv = np.linalg.inv(matriz)
        return np.allclose(matriz_transp,matriz_inv)
    except:
        return False

print(senoPositivo(0,3*np.pi,6))
print(a(np.array([3,4]),7))
print(ortogonal(np.eye(N = 2, M =3)))
print(ortogonal(1/3*np.array([[2,-2,1],[1,2,2],[2,1,-2]])))