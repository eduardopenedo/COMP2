# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223


# AULA 2
from datetime import * 
class Aluno:
    def __init__(self, nome, DRE, matricula = "ativa"):
        """Cria um objeto da classe Aluno com atributos nome, DRE, matricula"""
        self.nome = nome
        self.DRE = DRE       
        self.matricula = matricula

    def alterarMatricula(self, matricula):
        """Altera a matricula"""
        if self.matricula == matricula:
            print("A matrícula já está " + matricula)
        else:
            self.matricula = matricula
            print("A matrícula foi alterada para " + matricula)
            
    def dados(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)

    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, str(self.DRE), self.matricula)

        
#=======================================

class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, vagas = 0):
        """Cria um objeto da classe com atributos nome, vagas, alunos"""
        self.nome = nome
        self.vagas = vagas
        self.alunos = [] # self.alunos é um atributo global criado automaticamente

    def __add__(self, other):
        """Junta duas disciplinas se o nome delas for idêntico"""
        if self.nome == other.nome:
            return Disciplina(self.nome, self.vagas + other.vagas)
        else:
            print("Não foi possível juntar as turmas")
    
    def __str__(self):
        """ Retorna string com dados da disciplina e de alunos inscritos nela"""
        if len(self.alunos) == 0:
            return "{}, sem alunos inscritos.".format(self.nome)
        else:
            alunos_dados = ""
            for i in range(len(self.alunos)):
                alunos_dados += "{} {} matrícula {}\n".format(self.alunos[i].nome, self.alunos[i].DRE, self.alunos[i].matricula)

            return "{}, alunos inscritos:\n{}{}".format(self.nome, alunos_dados, self.consultarVagas(),0 )


    def inscreverAluno(self, aluno):
        """Inscreve um objeto da classe Aluno na disciplina se tiver
        vagas livres ou o Aluno não for ainda inscrito na disciplina"""
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("aluno {} já está inscrito na disciplina".format(aluno.nome))
        else:
            print("Vagas esgotadas")
    
    def consultarVagas(self):
        """ Retorna quantidade de vagas totais e vagas livres ( vagas totais - vagas ocupadas por objetos da classe Aluno )"""
        vagasDisponiveis = self.vagas - len(self.alunos)
        return "Vagas totais:{} Vagas livres:{}".format(self.vagas,vagasDisponiveis)

#=======================================

class Pessoa:
    def __init__(self, nome, dataNascimento, nomeDeMae, nomeDePai):
       """ Inicia um objeto do tipo Pessoa a partir dos parâmetros nome, dataNascimento, nomeDeMae, nomeDePai"""
       self.nome = nome
       self.dataNascimento = dataNascimento
       self.nomeDeMae =nomeDeMae
       self.nomeDePai = nomeDePai
    
    def __str__(self):
        """Retorna string com dados de um objeto Pessoa"""
        return "Nome: {} Idade: {} Mãe: {} Pai: {}".format(self.nome, self.idade(), self.nomeDeMae, self.nomeDePai)

    def idade(self, data = date.today().strftime("%d/%m/%Y")):
        """ Retorna a quantidade de anos entre a data atual e a data de nascimento """
        dia_nasc = int(self.dataNascimento[:2])
        mes_nasc = int(self.dataNascimento[3:5])
        ano_nasc = int(self.dataNascimento[6:])
        

        if date.today().month < mes_nasc:
            return (date.today().year - ano_nasc) -1
        elif date.today().month == mes_nasc:
            if date.today().day < dia_nasc:
                return date.today().year - ano_nasc -1
            else:
                return date.today().year - ano_nasc
        else:
            return date.today().year - ano_nasc
