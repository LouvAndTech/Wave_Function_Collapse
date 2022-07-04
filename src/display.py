import pygame
from math import cos,sin,radians

#Taille
HAUTEUR = 23 * 32
LARGEUR = 40 * 32

#Couleurs
WHITE = (255,255,255)
LIGHTBLUE = (114,159,207)
BLUE = (52,101,164)
GREEN = (0,255,0)
DARKGREEN = (78,154,6)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
PINK = (168,50,117)
PURPLE = (119,50,168)

class Screen():
    def __init__(self):
        pygame.init()
        self.QUITEVENT = pygame.QUIT
        self.KEYDOWN = pygame.KEYDOWN
        self.K_SPACE = pygame.K_SPACE
        self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
        pygame.display.set_caption("Wave Function Collaspe")

    """
    Method to en the pygame session
    @param: None
    @return: None
    """
    def close(self):
        pygame.display.quit()
        pygame.quit()

    """
    Method to update the screen
    @param: None
    @return: None
    """
    def updateScreen(self):
        pygame.display.flip()

    def eventGet(self):
        return pygame.event.get()

    """
    Method to display the background
    @param: screen, the screen
    @return: None
    """
    def fondDecran(self):
        self.screen.fill(BLACK)

    def printImage(self,imagePath,pos):
        self.screen.blit(pygame.image.load(imagePath), pos)

    def drawLigne(self,start,end):
       pygame.draw.line(self.screen,GREEN,start,end,3)
    