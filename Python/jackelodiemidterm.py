import pygame, sys,os
import random
pygame.init()

background_color = (255, 0, 0)

screen_size = (640, 640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Midterm')
screen.fill(background_color)



running = True

x = -10
y = -10

for i in range(0, 64):
    x += 10
    for j in range(0, 64):
        y += 10
        pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), pygame.Rect(x, y, 10, 10))
    y = -10
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

            

