import sys
import pygame
import time



def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))  #touple
    pygame.display.set_caption("Endless something")
    background = pygame.image.load("backgroundImage.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background, (0, 0))



main()