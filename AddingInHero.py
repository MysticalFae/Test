import sys
import pygame
import time

class Character:

    def __init__(self, screen):
        self.screen = screen

        self.charImage = pygame.image.load("turtle-png-28.png")

        self.x = screen.get_width() / 2 - self.charImage.get_width() / 2
        self.y = screen.get_height() / 2 - self.charImage.get_height() / 2


    def move(self, x):
        self.x = x
        pass

    def draw(self):
        self.screen.blit(self.charImage, (self.x, self.y))




def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))  #touple
    pygame.display.set_caption("Endless image")

    background = pygame.image.load("backgroundImage.png")
    background = pygame.transform.scale(background, (800, 700))

    character1 = Character(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.blit(background, (0, 0))


        # pressedKey = pygame.key.get_pressed()
        # if pressedKey[pygame.K_LEFT]:
        #     character1.move(-5)
        # if pressedKey[pygame.K_RIGHT]:
        #     character1.move(5)

        character1.draw()

        pygame.display.update()

main()