from operator import itemgetter
from rich import print
from rich.panel import Panel
from random import randint


def dict_to_list(dicionario:dict)->list:
    lista = []
    sublista = []
    for k, v in dicionario.items():
        sublista.append(k)
        sublista.append(v)
        lista.append(sublista.copy())
        sublista.clear()
    return lista


def list_to_dict(lista:list, retornar_varios_dicionario=False):
    dicionario = {}
    if not retornar_varios_dicionario:
        for c in range(0,len(lista)-1,2):
            dicionario[lista[c]] = lista[c+1]
        return dicionario
    else:
        lista0 = []
        subdicionario = {}
        for c in range(0,len(lista), 2):
            subdicionario[lista[c]] = lista[c+1]
            lista0.append(subdicionario.copy())
            subdicionario.clear()
        return lista0

def pergunta(string:str):
    while True:
        i = input(string)
        try:
            i = int(i)
            return i
        except ValueError:
            continue

class SuperLista:
    def __init__(self, list0):
        self.lista = list0
    def super_sort(self, reverse= False):
        slista = []
        lista = []
        for c in self.lista:
            for k, v in c.items():
                slista.append(k)
                slista.append(v)
                lista.append(slista.copy())
                slista.clear()
        self.lista.clear()
        self.lista = sorted(lista, key=itemgetter(1), reverse=reverse)
        lista0 = []
        for c in self.lista:
            a = list_to_dict(c)
            lista0.append(a)
        return lista0

class Competidores:
    def __init__(self, nome, ponto=0):
        self.nome = nome
        self.ponto = ponto
    def dicionarios(self):
        dici = {self.nome: self.ponto}
        return dici
    def add_ponto(self):
        self.ponto += 1



class Ranking:
    def __init__(self,*competidores:Competidores):
        self.competidores = []
        for c in competidores:
            self.competidores.append(c)

    def add_competidores(self,competidor):
        competidor = Competidores(competidor).dicionarios()
        self.competidores.append(competidor.copy())

    def retornador(self):
        return  self.competidores

    def rank(self, painel_b:bool = False):
        self.competidores = SuperLista(self.competidores).super_sort(True)
        conteudo = ''
        for p, c in enumerate(self.competidores):
            for k, v in c.items():
                lista = ['blue', 'purple', 'red', 'cyan']
                cor = lista[randint(0,3)]
                conteudo += f'[{cor}]{p+1}° {k:<30}{v}[/]\n'
        conteudo = conteudo[0:len(conteudo)-1]
        painel = Panel(conteudo, expand=False)
        if not painel_b:
            print(painel)
            return None
        else:
            return painel



class Resumo:
    def __init__(self, classe:Ranking):
        self.classe = classe
        self.cla = classe.retornador()
    def lista_votar(self):
        for p,c in enumerate(self.cla):
            print(f'{p+1}° {c}')
        while True:
            num = pergunta('Você irá votar no número?: ')
            if not (num > len(self.cla) or num < 1):
                di = self.classe.retornador()[num-1]
                for k,v in di.items():
                    di[k] = v+1
                break