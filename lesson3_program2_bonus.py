#addendum to program2 but includes a randomly moving rectangle

#count the score of the player when it hits the obstacle
#add a score variable and increment it when the player hits the obstacle

# creating shapes and moving them around the screen

import pygame
import sys
#import the random module
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))  # window size
pygame.display.set_caption("My First Pygame Window")

x=100
y=100

#create the score variable
score=0
font = pygame.font.SysFont(None, 36)

obstacle_rect_x = 200
obstacle_rect_y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background (white)
    screen.fill((255, 255, 255))

    #display the score
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    
    #randomly move the obstacle rectangle, introduce elif statements to keep the rectangle within the screen
    if 0 < obstacle_rect_x < 800:
        obstacle_rect_x += random.randint(-10, 10)
    elif obstacle_rect_x <= 0:
        obstacle_rect_x += 10
    elif obstacle_rect_x >= 800:
        obstacle_rect_x -= 10

    if 0 < obstacle_rect_y < 600:
        obstacle_rect_y += random.randint(-10, 10)
    elif obstacle_rect_y <= 0:
        obstacle_rect_y += 10
    elif obstacle_rect_y >= 600: 
        obstacle_rect_y -= 10
    #instantiate the player rectangle and then if it hits the obstacle rect, print collision detected
    player_rect = pygame.draw.rect(screen, (0, 128, 255), (x, y, 50, 50))  #  width=50, height=50
    obstacle_rect = pygame.draw.circle(screen, (255, 0, 0), (obstacle_rect_x, obstacle_rect_y), 40)       # center=(200,200), radius=40 
    if player_rect.colliderect(obstacle_rect):
        print("Collision detected!")
        score +=1
        
    pygame.display.update()

pygame.quit()
sys.exit()