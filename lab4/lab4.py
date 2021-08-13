# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

# Questão 1
def contatos(lista_dicts):
    """Recebe uma lista de dicionários como parâmetro, botando as chaves e valores(em uma lista) dentro de um dicionario

    Quando há chaves repetidas na lista de dicionários, o valor é uma lista com todos os valores

    list< dict<str,int> > -> dict<str,int>"""

    result = {}

    for dictionary in lista_dicts:
        for item in dictionary.items():
            item_key = item[0]
            item_value = item[1]
            if item_key not in result.keys():
                result[item_key] = [item_value]
            else:
                result[item_key].append(item_value)
    return result

# Questão 2
def piano(teclas):
    """Calcula as frequências das teclas de um piano

    str -> list<int>"""
    freq_base = {"C": 262, "D" : 294, "E": 330, "F": 349, "G": 392, "A": 440, "B": 494}
    
    freq_teclas = []
    for index in range(len(teclas)):
        if index %2 == 0:
            nota = teclas[index]
            num_nota = int(teclas[index +1])

            freq = freq_base[nota] * 2 ** (num_nota-3) 
            freq_teclas.append(freq)
    return freq_teclas

# Questão 3
def rezistor(faixa_1, faixa_2 , faixa_3):
    """Calcula a resistencia de um resistor

    str, str, str -> int"""
    cores = {"Preto": 0, "Marrom": 1, "Vermelho":2, "Laranja":3, "Amarelo":4}   
    
    resistencia = (cores[faixa_1] * 10 + (cores[faixa_2]*(10** cores[faixa_3])))
     
    return resistencia

if __name__ =="__main__":
    print(rezistor("Preto", "Marrom", "Vermelho"))
    print(rezistor("Vermelho", "Laranja", "Amarelo"))


if __name__ == "__main__":
    cont = [ 
    {"batata" : 1 , "tomate" : 2},  
    {"tomate" :  1 , "tomate" : 3},
    ]
    print(contatos(cont))


    teclas = "C1A2D3B4G3"
    print(piano(teclas))

    print(rezistor("Preto", "Marrom", "Vermelho"))
    print(rezistor("Vermelho", "Preto", "Amarelo"))