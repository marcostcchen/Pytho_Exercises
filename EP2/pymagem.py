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

    # escreva aqui os métodos da classe Pymagem

    def __init__(self, nlins, ncols, valor = 0):
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
                if j == self.ncols - 1:
                    s += '%d\n'%(self.Matrix[i][j])
                else:
                    s += '%d, '%(self.Matrix[i][j])
        return s

    def size(self):
        return self.nlins, self.ncols

    def get(self, lin, col):
        return self.Matrix[lin][col]

    def put(self, lin, col, value):
        self.Matrix[lin][col] = value

    def crop(self, tlx = 0, tly = 0, brx = -1, bry = -1):
        if brx == -1 and bry == -1:
            clone = Pymagem(self.nlins, self.ncols)
            auxi, auxj = 0, 0
            for i in range(tly, bry + 1):
                auxj = 0
                for j in range(tlx, brx + 1):
                    clone[auxi][auxj] = self.Matrix[i][j]
                    auxj += 1
                auxi += 1
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


img1 = Pymagem(4, 5)
img2 = Pymagem(3, 3, 88)

print("\nChamadas da função print()")
print("Conteúdo de img1:")
print(img1)
print("Conteúdo de img2:")
print(img2)

print("\nChamadas da função size()")
lins1, cols1 = img1.size()
print("Resolução de img1: %d x %d"%(lins1, cols1))
lins2, cols2 = img2.size()
print("Resolução de img2: %d x %d"%(lins2, cols2))

print("\nChamadas do método crop")
img3 = img1.crop() ## cria uma cópia
print("Conteúdo de img3:")
print(img3)
img4 = img2.crop(0, 1, lins2-1, cols2)
print("Conteúdo de img4:")
print(img4)

print("\nChamadas de put e get")
col = 2
img1.put(0, col, 11)
for lin in range(1, lins1):
     img1.put(lin, col, img1.get(lin-1, col) + 10)
print("Conteúdo de img1:")
print(img1)
# não deve alterar img3
print("Conteúdo de img3:")
print(img3)

# modifica a linha 1 de img2
lin = 1
for col in range(0, cols2):
    img2.put(lin, col, 11)
print("Conteúdo de img2:")
print(img2)
# não deve alterar img4
print("Conteúdo de img4:")
print(img4)

# mais testes
print("Outro crop")
print(img1.crop(1,1,3,4))