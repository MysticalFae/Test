import sys
import pygame
import time



def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))  #touple
    pygame.display.set_caption("Endless image")
    background = pygame.image.load("backgroundImage.png")
    background = pygame.transform.scale(background, (800, 700))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.blit(background, (0, 0))

        pygame.display.update()

main()