#render multiple falling rectangles

import pygame
import sys
import random

screen_width = 800
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))  # window size
pygame.display.set_caption("My First Pygame Window")

x=100
y=100

#create the score variable
score=0
font = pygame.font.SysFont(None, 36)

#instantiate a number of blocks
blocks = []
num_blocks = 5
block_size = 50
block_speed = 10

#ensure that the fps stays consistent
clock = pygame.time.Clock()

# Helper function to create a new random block
def create_block():
    x = random.randint(0, screen_width - block_size)
    y = random.randint(-300, -50)  # spawn above the screen
    speed = block_speed
    return [x, y, speed]

# Initialize a list of blocks
for _ in range(num_blocks):
    blocks.append(create_block())


#run the game

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background (white)
    screen.fill((255, 255, 255))

    #display the score
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))
    #increase score
    score += 1


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

    # Update block positions
    for i, block in enumerate(blocks):
        block[1] += block[2]  # block[1] = y position, block[2] = speed down

        # If a block goes off the bottom of the screen, lose a life and respawn it at the top
        if block[1] > screen_height:
            blocks[i] = create_block()

    for block in blocks:
        pygame.draw.rect(screen, (255, 0, 0), (block[0], block[1], block_size, block_size))
        
    pygame.display.update()

pygame.quit()
sys.exit()