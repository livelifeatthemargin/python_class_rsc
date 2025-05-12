#render multiple falling rectangles + create a game over sequence based on the number of lives
#questions for students - what happens if you increase p

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

#num lives
lives = 5

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

#game over flag
game_over = False

#set player speed
player_speed = 10

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
    #display the lives
    lives_text = font.render(f"Lives: {lives}", True, (0,0,0))
    screen.blit(lives_text, (10, 40))


    #introducing game over scenario
    if not game_over:
        #increase score
        score += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= player_speed
        if keys[pygame.K_RIGHT]:
            x += player_speed
        if keys[pygame.K_UP]:
            y -= player_speed
        if keys[pygame.K_DOWN]:
            y += player_speed
        #instantiate the player rectangle and then if it hits the obstacle rect, print collision detected
        player_rect = pygame.draw.rect(screen, (0, 128, 255), (x, y, 50, 50))  #  width=50, height=50
        
        #check collisions, decrement lives if it happens
        #once lives = 0, set game_over to True
        for i, block in enumerate(blocks):
            block_rect = pygame.Rect(block[0], block[1], block_size, block_size)
            if player_rect.colliderect(block_rect):
                lives -= 1
                blocks[i] = create_block()
                if lives <= 0:
                    game_over = True


        # Update block positions
        for i, block in enumerate(blocks):
            block[1] += block[2]  # block[1] = y position, block[2] = speed down

            # If a block goes off the bottom of the screen, lose a life and respawn it at the top
            if block[1] > screen_height:
                blocks[i] = create_block()


    for block in blocks:
        pygame.draw.rect(screen, (255, 0, 0), (block[0], block[1], block_size, block_size))
    
    if game_over:
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 30))
            info_text = font.render("Press R to Restart or Q to Quit", True, (255, 0, 0))
            screen.blit(info_text, (screen_width // 2 - 180, screen_height // 2 + 10))

            # Check if user presses R or Q
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset all game variables
                score = 0
                lives = 3
                blocks = [create_block() for _ in range(num_blocks)]
                #player_x = screen_width // 2 - player_width // 2
                #player_y = screen_height - player_height - 10
                game_over = False
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()


    pygame.display.update()

pygame.quit()
sys.exit()