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
# constantes
BLOCKED = 0
OPEN    = 1
FULL    = 2

class Percolation:
    '''
    Representa uma grade n x n com todos os sítios inicialmente bloqueados.
    o parâmetro n representa a dimensão da grade.
    '''

    def __init__(self, n = -1):
        if n == -1:
            print("Erro! Percolation precisa de um valor positivo n!")
            return None
        else:
            self.grade = []
            self.n = n
            self.NumeroOpen = 0
            self.percolou = False
            self.filaPercolada = []
            self.ja_percolou = 0

            for i in range(n):
                linha = []
                for j in range(n):
                    linha.append(0)
                self.grade.append(linha)

    def __str__(self):
        s = ''
        divisoria = ''
        for i in range(self.n):
            if i < self.n - 1:
                divisoria = divisoria + '+---'
            else:
                divisoria = divisoria + '+---+'


        s = s + divisoria + '\n'
        for i in range(self.n):
            for j in range(self.n):
                if self.grade[i][j] == 0:
                    s = s + '|   '
                elif self.grade[i][j] == 1:
                    s = s + '| o '
                else:
                    s = s + '| X '
                if j == self.n - 1:
                    s = s + '|\n'
            s = s + divisoria + '\n'

        s = s + 'Grade de dimensão %dx%d'%(self.n, self.n) + '\n'
        s = s + 'Numero de sitios abertos: %d'%(self.NumeroOpen) + '\n'
        s = s + 'Percolou: %s'%(self.percolou)
        return s

    def __len__(self):
        return self.n

    def is_open(self, lin, col):
        if self.grade[lin][col] == 1:
            return True
        else:
            return False

    def is_full(self, lin, col):
        if self.grade[lin][col] == 2:
            return True
        else:
            return False

    def no_open(self):
        return self.NumeroOpen

    def open(self, lin, col):
        self.filaPercolada = []
        if lin >= self.n or col >= self.n:
            print('Posição [%d][%d] está fora da grade'%(lin,col))
        if lin < self.n  and col < self.n and self.grade[lin][col] == 0:
            if self.grade[lin][col] == 0:
                self.grade[lin][col] = 1
                self.NumeroOpen += 1

        # voltando tudo para open
        for i in range(self.n):
            for j in range(self.n):
                if self.is_full(i,j):
                    self.grade[i][j] = 1

        cabecas = 0
        for i in range(self.n):
            if self.is_open(0,i):
                cabecas += 1

        # Primeiro Nó Full
        while (cabecas != 0):
            cabecas -= 1
            i = 0
            while self.filaPercolada == [] and i < self.n:
                if self.is_open(0, i):
                    self.filaPercolada.append([0, i])
                    self.grade[0][i] = 2
                i += 1

            if self.filaPercolada != [] and self.filaPercolada[0][0] == self.n - 1:
                self.percolou = True

            # Para os outros Nós Full
            while self.filaPercolada != []:
                no_atual = self.filaPercolada.pop(0)
                no_atual_lin, no_atual_col = no_atual[0], no_atual[1]
                if no_atual_lin == self.n - 1:
                    self.percolou = True

                # Analisando a direita
                if no_atual_col < self.n - 1:
                    if self.is_open(no_atual_lin, no_atual_col + 1):
                        self.filaPercolada.append([no_atual_lin, no_atual_col + 1])
                        self.grade[no_atual_lin][no_atual_col + 1] = 2

                # Analisando a esquerda
                if no_atual_col > 0:
                    if self.is_open(no_atual_lin, no_atual_col - 1):
                        self.filaPercolada.append([no_atual_lin, no_atual_col - 1])
                        self.grade[no_atual_lin][no_atual_col - 1] = 2

                # Analisando para baixo
                if no_atual_lin < self.n - 1:
                    if self.is_open(no_atual_lin + 1, no_atual_col):
                        self.filaPercolada.append([no_atual_lin + 1, no_atual_col])
                        self.grade[no_atual_lin + 1][no_atual_col] = 2

                # Analisando para cima
                if no_atual_lin > 0:
                    if self.is_open(no_atual_lin - 1, no_atual_col):
                        self.filaPercolada.append([no_atual_lin - 1, no_atual_col])
                        self.grade[no_atual_lin - 1][no_atual_col] = 2
    def percolates(self):
        return self.percolou

    def get_grid(self):
        grid = []
        for i in range(self.n):
            linha = []
            for j in range(self.n):
                linha.append(self.grade[i][j])
            grid.append(linha)
        return grid