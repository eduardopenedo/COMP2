# Nome : Eduardo Rodrigues Penedo
# DRE : 120043223

class VeiculoAutomotor():
    def __init__(self, dono, placa, combustivel):
        """ 
            object, string, string, string -> none
            
            Inicia um objeto VeiculoAutomotor
        """
        self.dono = dono
        self.placa = placa
        self.combustivel = combustivel

    def __str__(self):
        """
            object -> string

            Informa os dados de um Veiculo
        """
        return "Dono: {}, placa: {}, combustível: {}".format(self.dono, self.placa, self.combustivel)

    def trocarDono(self,novo_dono):
        """ 
            object, string -> none
            
            Troca o dono de um Veiculo  
        """
        self.dono = novo_dono

   
class Automovel(VeiculoAutomotor):
    def __init__(self,dono, placa, combustivel, lugares,portas,ano) :
        """ 
            object, string, string, string, int, int, int -> none

            Inicia um tipo de VeiculoAutomovel chamado Automovel 
        """
        super().__init__(dono, placa, combustivel)
        self.lugares = lugares
        self.portas = portas
        self.ano = ano
       
    def __str__(self):
        """
            object -> string

            Informa os dados de um Automovel
        """
        return super().__str__() + ", lugares: {}, portas: {}, ano: {}".format(self.lugares,self.portas,self.ano)

class Caminhao(VeiculoAutomotor):
    def __init__(self, dono, placa, combustivel, cargaMax):
        """ 
            object, string, string, string, int -> none
            
            Inicia um tipo de VeiculoAutomovel chamado Caminhao 
        """
        super().__init__(dono, placa, combustivel)
        self.cargaMax = cargaMax

    def __str__(self):
        """
            object -> string

            Informa os dados de um Caminhao
        """
        return super().__str__() + ", carga máxima: {} toneladas".format(self.cargaMax)

if __name__ == "__main__":
    fusca = Automovel("Lea", "XYZ111","eletricidade", 5, 3, 1940)
    print(fusca)
    fusca.trocarDono("Mia")
    print(fusca)
    camionete = Caminhao("Emile", "ABC123", "gás", 4)
    print(camionete)