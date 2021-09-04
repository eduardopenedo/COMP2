# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223
def escreverNoArquivo(file_name, data):
    """
    Escreve os elemento de uma lista data em cada linha de um arquivo de nome file_name e retorna o número de caracteres escritos no arquivo

    :param file_name: str
    :param data: list
    :return: int
    """
    text_content = list()
    try:
        file = open(file_name,"w")
        try:
            for item_data in data:
                text_content.append(str(item_data))
            lines = file.write("\n".join(text_content))
            file.close()
            return lines
        except:
            print("Não foi possível escrever no arquivo {}".format(file_name))
            file.close()
            return 0

    except OSError:
        print("Não foi possível abrir/criar o aquivo {}".format(file_name))
        return 0

def retornarLista(str_list):
    """
    Transforma uma string ( da forma "['A',1,]" ) em uma lista com elementos do tipo float ou string

    :param str_list: list
    :return: list
    """
    list = str.split(str_list[1:-1],",")
    for index in range(len(list)):
        try:
            list[index] = float(list[index])
        except:
            try:
                list[index] = list[index][list[index].index("'")+1: list[index].rindex("'")]
            except:
                print("Não foi possível transformar o elemento da lista em float ou string")
    return list

def lerArquivo(file_name):
    """
    Transforma os dados de um arquivo em uma lista com elementos do tipo lista, float ou string

    :param file_name: str
    :return: list
    """
    file = open(file_name,"r")
    content = file.read().split("\n")
    for index in range(len(content)):
        try:
            content[index] = float(content[index])
        except:
            try:
                if content[index][0] == "[":
                    content[index] = retornarLista(content[index])
                else:
                    content[index] = str(content[index])
            except:
                print("Não é possivel tranformar o dado em float, string ou lista")
    return content

if __name__ == '__main__':
    print(escreverNoArquivo("arq.txt",[-3.5, 9, [12.0, '@900#', 9.8], 'abece', 'k']))
    print(retornarLista("[12.0, '@900#', 'a', 9.8]"))
    print(lerArquivo("arq.txt"))