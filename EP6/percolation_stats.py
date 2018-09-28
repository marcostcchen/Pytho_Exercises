# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
# ------------------------------------------------------------------

'''

    Nome: Marcos Tan Chi Chen
    NUSP: 9833065

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
from percolation import Percolation
import random
import math

class PercolationStats:
    '''Classe utilizada para estimar o limiar de percolação.
    '''
    def __init__(self,n,T):
        self.n = n
        self.T = T
        self.x = []

        while T > 0:
            percolation = Percolation(n)
            while percolation.percolates() == False:
                randomx = random.randint(0, self.n - 1)
                randomy = random.randint(0 , self.n - 1)
                percolation.open(randomx, randomy)
            p = percolation.no_open()/(self.n*self.n)
            self.x.append(p)
            T = T - 1

    def mean(self):
        soma = 0
        aux = self.x[:]
        for i in range (len(aux)):
            soma = soma + aux[i]
        return soma/self.T

    def stddev(self):
        aux = self.x[:]
        soma_quadrados = 0
        for i in range(len(aux)):
            soma_quadrados = soma_quadrados + (self.x[i] - self.mean())*(self.x[i] - self.mean())
        s2 = soma_quadrados/(self.T - 1)
        return s2 ** (1/2)

    def confidenceLow(self):
        return self.mean() - (1.96*self.stddev()/(self.T ** (1/2)))

    def confidenceHigh(self):
        return self.mean() + (1.96*self.stddev()/(self.T ** (1/2)))

