import pygame
from pygame.locals import *
from pygame import Color

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond,(0,0))

"""
paramètres : 
- la surface où peindre le cercle
- les paramètres r,g,b de la couleur
- les coordonnées x,y du centre
- le rayon
"""

def head():
    pygame.draw.circle(fenetre, (0,0,0), (300, 175), 50)
def arms():
    pygame.draw.line(fenetre, (0,0,0), (200, 250), (400, 250), 10)
def body():
    pygame.draw.line(fenetre, (0,0,0), (300, 175), (300, 375), 10)
def legs():
    pygame.draw.lines(fenetre, (0,0,0), False, [(200, 450),(300, 375),(400, 450)], 10)
def stickman():
    head()
    arms()
    body()
    legs()

stickman()

continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    pygame.display.update()


pygame.quit()