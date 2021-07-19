# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

# Questão 1
# Recebe duas strings s1 e s2 e dois números m e n, retorna a string s1 a partir da posição m e s2 com os n últimos caracteres removidos
# string, string, int, int  -> string
def concatena(s1, s2, m, n):
    return s1[m:] + s2[0:-n]

# Questão 2
# Recebe uma lista de numeros e retorna uma lista apenas com os números que são maiores que m e menores que n 
# list<int>, int, int -> list<int>
def sublista(lista_numeros, m, n):
    res = list()
    for i in range(len(lista_numeros)):
        if (lista_numeros[i] > m) and (lista_numeros[i] < n):
            res.append(lista_numeros[i])
    return res

# Questão 3
# Recebe uma string palavra e uma lista de string, retorna a concatenação da string palavra e da lista lista_palavras com os elementos separados por um espaço em branco
# string, list<string> -> string
def fun(palavra, lista_palavras):
    return palavra + " " + " ".join(lista_palavras)


import math

# Questão 4a
# recebe um inteiro n e retorna o resultado do calculo do número de euler, que é dado pela fórmula ( 1/0! + 1/1! + 1/2! + ... + 1/n!)  
# int -> float
def numeroEuler(n):
    
    euler = 0

    for i in range(n+1):
        euler += (1/math.factorial(i))
    return euler

# Questão 4b
# Recebe um float erro_max e devolve o indice de n que faz com que a diferença entre o número de euler e o calculado pela função numeroEuler, seja o maior possível e menor que o erro_max
# float -> int
def precisaoEuler(erro_max):
    n=0
    while (math.e - numeroEuler(n)) > erro_max:
        n+=1
    return n

# Questão 4c
# Não recebe nenhum parâmetro,pergunta e recebe o erro_max desejado pelo usuário e calcula o indice que faz com que a diferença entre o número de euler e o calculado pela função numeroEuler, seja o maior possível e menor que o erro_max, atráves da chamada da função precisaoEuler
# none -> none
def main():
    erro_max = float(input("Por favor insira o erro máximo tolerado: "))
    print(precisaoEuler(erro_max))

if __name__ == "__main__":
    main()