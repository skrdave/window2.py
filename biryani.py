import pygame,sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Helllo world!")

screen.fill("blue")

img1 = pygame.image.load("images/biryani.jpeg")
img1 = pygame.transform.scale(img1,(100,100))
img1 = pygame.transform.rotate(img1,-90)



while True:
    screen.blit(img1,(100,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

