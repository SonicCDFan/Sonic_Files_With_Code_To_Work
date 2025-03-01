import pygame,random

IMAGEMSONIC=pygame.image.load("img/R.png")
IMAGEMFUNDO=pygame.image.load("img/fundo.png")
IMAGEMMOEDA=pygame.image.load("img/moedas.png")

LARGURAMOEDA=80
ALTURAMOEDA=30
LARGURASONIC=240
ALTURASONIC=140
LARGURAJANELA=800
ALTURAJANELA=700
VEL=6
INTERACAO=30

IMAGEMFUNDO=pygame.transform.scale(IMAGEMFUNDO,(LARGURAJANELA,ALTURAJANELA))
IMAGEMMOEDA=pygame.transform.scale(IMAGEMMOEDA,(LARGURAMOEDA,ALTURAMOEDA))
IMAGEMSONIC=pygame.transform.scale(IMAGEMSONIC,(LARGURASONIC,ALTURASONIC))


def moverJogador(jogador,teclas,dimensaoJanela):
    bordaesq=0
    bordasup=0
    bordadir=dimensaoJanela[0]
    bordainf=dimensaoJanela[1]
    if teclas["esquerda"]and jogador["objeto"].left>bordaesq:
        jogador["objeto"].x-=jogador["vel"]
    if teclas["direita"]and jogador["objeto"].left<bordadir:
        jogador["objeto"].x+=jogador["vel"]
    if teclas["cima"]and jogador["objeto"].left>bordasup:
        jogador["objeto"].y-=jogador["vel"]
    if teclas["baixo"]and jogador["objeto"].left<bordainf:
        jogador["objeto"].y+=jogador["vel"]

def moverMoeda(moeda):
    moeda["objeto"].x -=moeda["vel"]

pygame.init()
relogio=pygame.time.Clock()

janela=pygame.display.set_mode((LARGURAJANELA,ALTURAJANELA))
pygame.display.set_caption("SONIC")

jogador={"objeto":pygame.Rect(300,100,LARGURASONIC,ALTURASONIC),"imagem":IMAGEMSONIC,"vel":VEL,"colisaoRect":pygame.Rect( ▋