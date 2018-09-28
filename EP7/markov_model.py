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

class MarkovModel:
    def __init__(self, k, corpus):
        self.dicio = {}
        self.k = k

        # Separando corpus
        i = 0
        n = len(corpus)
        while n > k - 1:
            item = ""
            for y in range(i, i + k, 1):
                item = item + corpus[y]
            self.put(item)
            i += 1
            n -= 1

        # Pegando os ultimos termos se restarem
        for j in range(k - 1):
            item = ""
            aux = 0
            for y in range(i, i + k, 1):
                if y >= len(corpus):
                    item = item + corpus[aux]
                    aux += 1
                else:
                    item = item + corpus[y]
            self.put(item)
            i += 1


        # Agora faremos o mesmo processo para K+1
        # Separando corpus
        i = 0
        k = k + 1
        n = len(corpus)
        while n > k - 1:
            item = ""
            for y in range(i, i + k, 1):
                item = item + corpus[y]
            self.put(item)
            i += 1
            n -= 1

        # Pegando os ultimos termos se restarem
        for j in range(k - 1):
            item = ""
            aux = 0
            for y in range(i, i + k, 1):
                if y >= len(corpus):
                    item = item + corpus[aux]
                    aux += 1
                else:
                    item = item + corpus[y]
            self.put(item)
            i += 1

    def put(self, string):
        if self.dicio.get(string) == None:
            self.dicio[string] = 1
        else:
            self.dicio[string] = self.dicio.pop(string) + 1

    def __str__(self):
        s = ""
        for key in self.dicio:
            if len(key) == self.k:
                s = s + "%s   %s\n"%(key, self.dicio[key])
            else:
                s = s + "%s  %s\n"%(key, self.dicio[key])
        return s

corpus2 = "babababaabababaabaabaaaaaababaaaab"
modelo2 = MarkovModel(4, corpus2)
print(modelo2)
