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

        Utilizei o site do stackOverFlow para entender melhor o funcionamento de matrizes https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
        pois aprendi a materia anterior usando C, ainda estou com um pouco de dificuldades para entender o python

'''

#--------------------------------------------------------------------------
def crie_imagem(nlin, ncol, valor):
    ''' (int, int, obj) -> list

    # Recebe dois inteiros nlin e ncol e um valor.
    # Cria e retorna uma imagem de dimensão nlin x ncol com valor em cada
    # posição.
    #
    # Exemplos:
    # >>> t = crie_imagem(3,4,-1)
    # >>> t
    # [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
    # >>> tt = crie_imagem(3,3,0)
    # >>> tt
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # >>>
    # '''
    Matrix = [[0 for x in range(ncol)] for y in range(nlin)]
    for i in range(nlin):
        for j in range(ncol):
            Matrix[i][j] = valor
    return Matrix

#--------------------------------------------------------------------------
def copie_imagem(dest, orig):
    ''' (list, list) -> None

    Recebe duas imagens de mesma dimensão e copia o conteúdo de orig para dest.

    Exemplo:

    # >>> t = [[12, -122, 3],[1, 2, 3]]
    # >>> tt = [[11, 22, 33],[44, 55, 66]]
    # >>> copie_imagem(tt, t)
    # >>> t
    # [[12, -122, 3], [1, 2, 3]]
    # >>> tt
    # [[12, -122, 3], [1, 2, 3]]
    # >>> tt[0][0] = 777
    # >>> t
    # [[12, -122, 3], [1, 2, 3]]
    # >>> tt
    # [[777, -122, 3], [1, 2, 3]]
    # '''
    for i in range(len(orig[0]) - 1):
        dest[i] = orig[i][:]

#--------------------------------------------------------------------------
def clone_imagem(imagem):
    ''' (list) -> list

    Recebe uma imagem e retorna uma cópia/clone da imagem

    Exemplo:
    # >>> t = [[12, -122, 3],[1, 2, 3]]
    # >>> tt = clone_imagem(t)
    # >>> t
    # [[12, -122, 3], [1, 2, 3]]
    # >>> tt
    # [[12, -122, 3], [1, 2, 3]]
    # >>> tt[0][0] = 111111
    # >>> t
    # [[12, -122, 3], [1, 2, 3]]
    # >>> tt
    # [[111111, -122, 3], [1, 2, 3]]
    # >>>
    # '''
    matriz = [[0 for x in range(len(imagem[0]))] for y in range(len(imagem))]
    for i in range(len(imagem[0]) - 1):
        matriz[i] = imagem[i][:]
    return matriz

#--------------------------------------------------------------------------
def recorte_imagem(imagem, tlx, tly, brx, bry):
    ''' (list, int, int, int, int) -> list

    Recebe uma imagem e as coordenadas (tlx, tly) do ponto TL (Top-Left)
    e (brx, bry) do ponto BR (Bottom-Right), representando um retângulo
    de cantos TL e BR. A função cria e retorna uma imagem de dimensão
    (brx-tlx) x (bry-tly), com conteúdo igual ao do retângulo TLxBR.
    Observe que os pontos na linha brx e coluna bry não fazem parte do retângulo.

    # Exemplo:
    # >>> crop_image([[1, 2, 3, 4, 5],
    #                 [1, 2, 3, 4, 5],
    #                 [1, 2, 3, 4, 5],
    #                 [1, 2, 3, 4, 5] ], 0, 1, 3, 4)
    # [[2,3,4], [2,3,4], [2,3,4]]
    # >>> crop_image([[1, 2, 3, 4, 5],
    #                 [6, 7, 8, 9, 0],
    #                 [0, 9, 8, 7, 6],
    #                 [1, 2, 3, 4, 5] ], 1, 1, 3, 3)
    # [[7,8], [9,8]]
    # '''
    matriz = [[0 for x in range(brx - tlx + 1)] for y in range(bry - tly + 1)]
    auxi, auxj = 0,0
    for i in range(tly, bry + 1):
        auxj = 0
        for j in range(tlx, brx + 1):
            matriz[auxi][auxj] = imagem[i][j]
            auxj += 1
        auxi += 1
    return matriz

#--------------------------------------------------------------------------

def main():
    t = crie_imagem(4, 4, -1)
    aux = recorte_imagem(t,2,0,3,3)
    print(aux)

if __name__ == "__main__":
    main()