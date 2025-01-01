import pygame
pygame.init()
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
AMPLADA_FINESTRA = 800
ALCADA_FINESTRA = 600
AMPLADA_PLATAFORMA = int(AMPLADA_FINESTRA * 0.2)
ALCADA_PLATAFORMA = 10
VELOCITAT_BOLA = 1
ANGLE_REBOT_ESQUERRA = 45
ANGLE_REBOT_DRETA = 135
finestra = pygame.display.set_mode((AMPLADA_FINESTRA, ALCADA_FINESTRA))
posicio_plataforma = [int(AMPLADA_FINESTRA / 2 - AMPLADA_PLATAFORMA / 2), ALCADA_FINESTRA - 50]
posicio_bola = [int(AMPLADA_FINESTRA / 2), int(ALCADA_FINESTRA / 2)]
direccio_bola = [0, -1]
def dibuixar_plataforma():
    pygame.draw.rect(finestra, BLANC, [posicio_plataforma[0], posicio_plataforma[1], AMPLADA_PLATAFORMA, ALCADA_PLATAFORMA])
def dibuixar_bola():
    pygame.draw.circle(finestra, BLANC, posicio_bola, 5)
def moure_plataforma(direccio):
    posicio_plataforma[0] += direccio
    if posicio_plataforma[0] < 0:
        posicio_plataforma[0] = 0
    elif posicio_plataforma[0] > AMPLADA_FINESTRA - AMPLADA_PLATAFORMA:
        posicio_plataforma[0] = AMPLADA_FINESTRA - AMPLADA_PLATAFORMA
def moure_bola():
    posicio_bola[0] += int(direccio_bola[0] * VELOCITAT_BOLA)
    posicio_bola[1] += int(direccio_bola[1] * VELOCITAT_BOLA)
    if posicio_bola[0] < 0 or posicio_bola[0] > AMPLADA_FINESTRA:
        direccio_bola[0] *= -1
    if posicio_bola[1] < 0:
        direccio_bola[1] *= -1
    if posicio_bola[1] > posicio_plataforma[1] and posicio_bola[1] < posicio_plataforma[1] + ALCADA_PLATAFORMA:
        if posicio_bola[0] > posicio_plataforma[0] and posicio_bola[0] < posicio_plataforma[0] + AMPLADA_PLATAFORMA:
            direccio_bola[1] *= -1
            if posicio_bola[0] < posicio_plataforma[0] + AMPLADA_PLATAFORMA / 2:
                direccio_bola[0] = -1
                direccio_bola[1] = -1
            else:
                direccio_bola[0] = 1
                direccio_bola[1] = -1
while True:
    finestra.fill(NEGRE)
    dibuixar_plataforma()
    dibuixar_bola()
    moure_plataforma(0)
    moure_bola()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moure_plataforma(-5)
            elif event.key == pygame.K_RIGHT:
                moure_plataforma(5)
            elif event.key == pygame.K_SPACE:
                direccio_bola[0] = 0
                direccio_bola[1] = -1
    pygame.display.update()
