import sys
import pygame
import time


def main():
    pygame.init()




    while True:

        for event in pygame.event.get():  # "event" could be any word (ie. cat)
            if event.type == pygame.QUIT:  # same here... "event.type" doesn't have to be (ie. cat.type)
                sys.exit()



        pygame.display.update()

main()