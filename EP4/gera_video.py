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

from EP4.pymagem import Pymagem
from EP4.pilutil import mostre_animacao
from EP4.pilutil import salve_animacao

import random

# Escreva aqui outras constantes que desejar
ALTURA = 120
LARGURA = 160

BLACK = 0
WHITE = 255


# --------------------------------------------------------------------------

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo com 900 Pymagens.

    O código abaixo serve para ilustrar como usar a função mostre_animacao().
    Remova ou altere o código para gerar o seu próprio vídeo.
    '''

    video = []

    cor, centrox, centroy, raio = [], [], [], []

    #Bolas Random
    for j in range(20):
        if j == 0:
            numero_bolas = random.randint(7, 15)
            imagem = Pymagem(ALTURA, LARGURA, WHITE)
            for i in range (numero_bolas):
                cor.append(255)
                raio.append(random.randint(3, 10))
                centrox.append(random.randint(raio[i], ALTURA - raio[i]))
                centroy.append(random.randint(raio[i], LARGURA - raio[i]))
                imagem.pinte_disco(centrox[i],centroy[i],raio[i],cor[i])
            video.append(imagem)

        else:
            imagem_seguida = imagem.crop()
            for i in range(numero_bolas):
                cor[i] = cor[i] - 10
                imagem.pinte_disco(centrox[i],centroy[i],raio[i],cor[i])
                video.append(imagem_seguida)
                imagem = imagem_seguida

    for z in range (3):
        #Primeiro Quadrado Abrindo
        for j in range(20):
            imagem_seguida = imagem.crop()
            if j == 1:
                imagem_seguida.pinte_retangulo(ALTURA//2 - 2, LARGURA//2 - 2, ALTURA//2 + 2, LARGURA//2 + 2, random.randint(5, 255))
                video.append(imagem_seguida)
            else:
                imagem_seguida.pinte_retangulo(ALTURA//2 - 2 - j*2, LARGURA//2 - 2 - j*2, ALTURA//2 + 2 + j*2, LARGURA//2 + 2 + j*2, random.randint(5,255))
                video.append(imagem_seguida)
            imagem = imagem_seguida

        #Segundo Quadrado Abrindo
        for j in range(20):
            imagem_seguida = imagem.crop()
            if j == 1:
                imagem_seguida.pinte_retangulo(ALTURA//2 - 2, LARGURA//2 - 2, ALTURA//2 + 2, LARGURA//2 + 2, 110)
                video.append(imagem_seguida)
            else:
                imagem_seguida.pinte_retangulo(ALTURA//2 - 2 - j*2, LARGURA//2 - 2 - j*2, ALTURA//2 + 2 + j*2, LARGURA//2 + 2 + j*2, 110 + 3*j)
                video.append(imagem_seguida)
            imagem = imagem_seguida

        #Terceiro Quadrado Abrindo
        for j in range(20):
            imagem_seguida = imagem.crop()
            imagem_seguida.pinte_retangulo(ALTURA//2 - 2 - j*2, LARGURA//2 - 2 - j*2, ALTURA//2 + 2 + j*2, LARGURA//2 + 2 + j*2, random.randint(0,255))
            video.append(imagem_seguida)
            imagem = imagem_seguida


        #Repetição de Quadrados Fechando
        for j in range(20):
            imagem_seguida = imagem.crop()
            imagem_seguida.pinte_retangulo(ALTURA//2 - 2 - 20*2 + 2*j, LARGURA//2 - 2 - 20*2 + 2*j, ALTURA//2 + 2 + 20*2 - 2*j, LARGURA//2 + 2 + 20*2 - 2*j, random.randint(10, 255))
            video.append(imagem_seguida)
            imagem = imagem_seguida


        #Repetição de Quadrados Maiores intervalos
        for j in range(20):
            imagem_seguida = imagem.crop()
            imagem_seguida.pinte_retangulo(ALTURA//2 - 2 - 20*2 + 4*j, LARGURA//2 - 2 - 20*2 + 4*j, ALTURA//2 + 2 + 20*2 - 4*j, LARGURA//2 + 2 + 20*2 - 4*j, random.randint(10, 255))
            video.append(imagem_seguida)
            imagem = imagem_seguida

    # Novas bolas random
    for j in range(15):
        if j == 0:
            numero_bolas = random.randint(7, 15)
            for i in range (numero_bolas):
                cor = []
                cor.append(253)
                raio.append(random.randint(3, 10))
                centrox.append(random.randint(raio[i], ALTURA - raio[i]))
                centroy.append(random.randint(raio[i], LARGURA - raio[i]))
                imagem.pinte_disco(centrox[i],centroy[i],raio[i],cor[i])
            video.append(imagem)

        else:
            imagem_seguida = imagem.crop()
            for i in range(numero_bolas):
                cor[i] = cor[i] - 5
                imagem.pinte_disco(centrox[i], centroy[i], raio[i], cor[i])
                video.append(imagem_seguida)
                imagem = imagem_seguida

    # Bolas random crescendo
    for j in range(30):
        imagem_seguida = imagem.crop()
        for i in range(numero_bolas):
            raio[i] = raio[i] + 0.5
            imagem_seguida.pinte_disco(centrox[i], centroy[i], raio[i], random.randint(5, 255))
            video.append(imagem_seguida)
            imagem = imagem_seguida

    # Bolas random decrescendo
    for j in range(30):
        imagem_seguida = imagem.crop()
        for i in range(numero_bolas):
            raio[i] = raio[i] - 2
            imagem_seguida.pinte_disco(centrox[i], centroy[i], raio[i], random.randint(5, 255))
            video.append(imagem_seguida)
            imagem = imagem_seguida

    # Bola Central Crescendo
    for z in range(3):
        for j in range(30):
            imagem_seguida = imagem.crop()
            raio[i] = raio[i] + 3
            imagem_seguida.pinte_disco(ALTURA//2, LARGURA//2, raio[i], random.randint(0, 255))
            video.append(imagem_seguida)
            imagem = imagem_seguida

        # Bola Central decrescendo
        for j in range(30):
            imagem_seguida = imagem.crop()
            raio[i] = raio[i] - 3
            imagem_seguida.pinte_disco(ALTURA // 2, LARGURA // 2, raio[i], 255 - 3*j)
            video.append(imagem_seguida)
            imagem = imagem_seguida

    print(len(video))
    mostre_animacao(video)



# --------------------------------------------------------------------------
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR
#
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()