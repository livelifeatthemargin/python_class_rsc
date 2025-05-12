#creating rectangles

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))  # window size
pygame.display.set_caption("My First Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background (white)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 128, 255), (100, 100, 50, 50))  # x=100, y=100, width=50, height=50
    pygame.draw.circle(screen, (255, 0, 0), (200, 200), 40)       # center=(200,200), radius=40 
    pygame.display.update()

pygame.quit()
sys.exit()