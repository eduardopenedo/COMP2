# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

def absoluto(param):
    """
    Calcula o valor absoluto de um número ou texto (se conversão for possível)
    :param param: str|int|float
    :return: float|str
    """
    import math
    try:
        return math.fabs(float(param))
    except ValueError:
        return (f"ValueError para ’{param}’")
    except TypeError:
        return(f"TypeError para {type(param)}")
    except :
        return("Erro")

class Loja:
    def __init__(self,nome,produtos):
        """
        Inicia umm objeto do tipo Loja

        :param nome: str
        :param produtos: dict
        """
        self.nome = nome
        self.produtos = produtos

    def adicionarProduto(self, categoria, marca):
        """
        Adiciona uma marca em uma categoria do dicionário produtos

        :param categoria: str
        :param marca: str
        :return: none
        """
        if categoria not in self.produtos:
            self.produtos[categoria] = set()
        self.produtos[categoria].add(marca)

    def verCategoria(self, categoria):
        """
        Retorna as marcas de uma categoria

        :param categoria: str
        :return: str
        """
        try:
            return self.produtos[categoria]
        except KeyError:
            return "Categoria sabão não catalogada."

    def removerMarca(self,marca):
        """
        Remove uma marca de todas as categorias de produto

        :param marca: str
        :return: nane
        """
        try:
            for item in self.produtos.items():
                item[1].remove(marca)
        except:
            pass



if __name__ == "__main__":
    # 1
    print(absoluto("-0.98"))
    print(absoluto(12))
    print(absoluto([1,2]))
    print(absoluto("a"))

    #2

    #a
    beleza1 = Loja("Beleza", {"esmalte": {"Colorama", "Max Factor"}, "desodorante": {"Nivea","Dove"}})
    print(beleza1.produtos)

    #b
    beleza1.adicionarProduto("xampu", "TRESemmé")
    print(beleza1.produtos)

    #c
    print(beleza1.verCategoria("esmalte"))
    print(beleza1.verCategoria("sabão"))

    #d
    beleza1.removerMarca("Colorama")
    print(beleza1.produtos)