import pygame
import sys

LARGURA_JANELA = 640
ALTURA_JANELA = 480

AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)

xDaBola = LARGURA_JANELA / 2
yDaBola = ALTURA_JANELA / 2
tamanhoDaBola = 20
velocidadeDaBolaEmX = 3
velocidadeDaBolaEmY = 3

yDoJogador1 = ALTURA_JANELA / 2
yDoJogador2 = ALTURA_JANELA / 2

def xDoJogador1():
    return 30  

def xDoJogador2():
    return LARGURA_JANELA - 30 - larguraDosJogadores()

def larguraDosJogadores():
    return tamanhoDaBola

def alturaDosJogadores():
    return 3 * tamanhoDaBola

def atualizar():
    global xDaBola, yDaBola, velocidadeDaBolaEmX, velocidadeDaBolaEmY, yDoJogador1, yDoJogador2

    xDaBola += velocidadeDaBolaEmX
    yDaBola += velocidadeDaBolaEmY

    if (xDaBola + tamanhoDaBola / 2 > xDoJogador2() - larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador2 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador2 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if (xDaBola - tamanhoDaBola / 2 < xDoJogador1() + larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador1 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador1 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if yDaBola + tamanhoDaBola / 2 > ALTURA_JANELA or yDaBola - tamanhoDaBola / 2 < 0:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if xDaBola < 0 or xDaBola > LARGURA_JANELA:
        xDaBola = LARGURA_JANELA / 2
        yDaBola = ALTURA_JANELA / 2

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        yDoJogador1 -= 5
    if keys[pygame.K_s]:
        yDoJogador1 += 5
    if keys[pygame.K_UP]:
        yDoJogador2 -= 5
    if keys[pygame.K_DOWN]:
        yDoJogador2 += 5

    yDoJogador1 = max(0, min(yDoJogador1, ALTURA_JANELA - alturaDosJogadores()))
    yDoJogador2 = max(0, min(yDoJogador2, ALTURA_JANELA - alturaDosJogadores()))

def desenhar():
    screen.fill(PRETO)
    pygame.draw.rect(screen, AMARELO, (xDaBola - tamanhoDaBola / 2, yDaBola - tamanhoDaBola / 2, tamanhoDaBola, tamanhoDaBola))
    pygame.draw.rect(screen, VERMELHO, (xDoJogador1(), yDoJogador1, larguraDosJogadores(), alturaDosJogadores()))
    pygame.draw.rect(screen, AZUL, (xDoJogador2(), yDoJogador2, larguraDosJogadores(), alturaDosJogadores()))
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Jogo de Pong")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    atualizar()
    desenhar()
    clock.tick(60)
