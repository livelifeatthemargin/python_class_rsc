#collision basics
#the rectangle will print if it collides with another object

# creating shapes and moving them around the screen

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))  # window size
pygame.display.set_caption("My First Pygame Window")

x=100
y=100



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background (white)
    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    #instantiate the player rectangle and then if it hits the obstacle rect, print collision detected
    player_rect = pygame.draw.rect(screen, (0, 128, 255), (x, y, 50, 50))  #  width=50, height=50
    obstacle_rect = pygame.draw.circle(screen, (255, 0, 0), (200, 200), 40)       # center=(200,200), radius=40 
    if player_rect.colliderect(obstacle_rect):
        print("Collision detected!")
    pygame.display.update()

pygame.quit()
sys.exit()