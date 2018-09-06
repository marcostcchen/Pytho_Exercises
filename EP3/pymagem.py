# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

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
#--------------------------------------------------------------------------

class Pymagem:
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito
    no enunciado.
    '''

    def __init__(self, nlins, ncols, valor=0):
        self.nlins = nlins
        self.ncols = ncols
        self.valor = valor
        self.Matrix = [[0 for x in range(ncols)] for y in range(nlins)]
        for i in range(nlins):
            for j in range(ncols):
                self.Matrix[i][j] = valor

    def __str__(self):
        s = str()
        for i in range(self.nlins):
            for j in range(self.ncols):
                if type(self.Matrix[0][0]) == int:
                    if j == self.ncols - 1:
                        s += '%d\n' % (self.Matrix[i][j])
                    else:
                        s += '%d, ' % (self.Matrix[i][j])
                else:
                    if j == self.ncols - 1:
                        s += '%.1f\n' % (self.Matrix[i][j])
                    else:
                        s += '%.1f, ' % (self.Matrix[i][j])
        return s

    def size(self):
        return self.nlins, self.ncols

    def get(self, lin, col):
        return self.Matrix[lin][col]

    def put(self, lin, col, value):
        self.Matrix[lin][col] = value

    def crop(self, tlx=0, tly=0, brx=-1, bry=-1):
        if brx == -1 and bry == -1 and tlx == 0 and tly == 0:
            clone = Pymagem(self.nlins, self.ncols)
            for i in range(self.nlins):
                for j in range(self.ncols):
                    clone.Matrix[i] = self.Matrix[i][:]
        else:
            clone = Pymagem(brx - tlx, bry - tly)
            auxi, auxj = 0, 0
            for i in range(tlx, brx):
                auxj = 0
                for j in range(tly, bry):
                    clone.Matrix[auxi][auxj] = self.Matrix[i][j]
                    auxj += 1
                auxi += 1
        return clone

    # escreva aqui os métodos da classe Pymagem
    def __add__(self, other):
        res = Pymagem(self.nlins, self.ncols)
        for i in range (self.nlins):
            for j in range (self.ncols):
                res.Matrix[i][j] = self.Matrix[i][j] + other.Matrix[i][j]
        return res

    def __mul__(self, alfa):
        res = Pymagem(self.nlins, self.ncols)
        for i in range (self.nlins):
            for j in range (self.ncols):
                res.Matrix[i][j] = self.Matrix[i][j]*alfa
        return res

    def paste (self, other, tlin, tcol):
        linha = tlin
        for i in range (other.nlins):
            coluna = tcol
            for j in range (other.ncols):
                self.Matrix[linha][coluna] = other.Matrix[i][j]
                coluna += 1
            linha += 1

    def pinte_disco (self, lin, col , raio, val):
        for i in range (self.nlins):
            for j in range(self.ncols):
                dist = (lin - i)*(lin - i) + (col - j)*(col - j)
                if dist < raio*raio :
                    self.Matrix[i][j] = val

    def pinte_retangulo (self, TLx, TLy, BRx, BRy, val):
        for i in range(TLx, BRx):
            for j in range(TLy, BRy):
                self.Matrix[i][j] = val
