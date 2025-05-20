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

player_x=400
player_y=500

#create the score variable
score=0
font = pygame.font.SysFont(None, 36)

#instantiate a number of blocks
blocks = []
num_blocks = 10
block_size = 50
block_speed = 10

#num lives
lives = 3

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

    #display the lives
    lives_text = font.render(f"Lives: {lives}", True, (0,0,0))
    screen.blit(lives_text, (10, 10))
    #display the score
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 40))

    if not game_over:
        score += 1  # Increment score over time
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed
        #instantiate the player rectangle and then if it hits the obstacle rect, print collision detected
        # Draw player
        player_img = pygame.image.load("player.png").convert_alpha()
        player_img = pygame.transform.scale(player_img, (100, 100))  # same size as the rectangle
        player_rect = player_img.get_rect(topleft=(player_x, player_y))
        screen.blit(player_img, (player_x, player_y))    
        #check collisions, decrement score if it happens
        for i, block in enumerate(blocks):
            enemy_img = pygame.image.load("enemy.png").convert_alpha()
            enemy_img = pygame.transform.scale(enemy_img, (block_size, block_size))  # same size as the rectangle
            block_rect = enemy_img.get_rect(topleft=(block[0], block[1]))
            screen.blit(enemy_img, (block[0], block[1]))
            #block_rect = pygame.Rect(block[0], block[1], block_size, block_size)
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


    
    if game_over:
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 30))
            info_text = font.render("Press R to Restart or Q to Quit", True, (255, 0, 0))
            screen.blit(info_text, (screen_width // 2 - 180, screen_height // 2 + 10))
            # Display the final score
            final_score_text = font.render(f"Final Score: {score}", True, (255, 0, 0))
            screen.blit(final_score_text, (screen_width // 2 - 80, screen_height // 2 + 50))

            # Check if user presses R or Q
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset all game variables
                score = 0
                lives = 3
                blocks = [create_block() for _ in range(num_blocks)]

                game_over = False
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()


    pygame.display.update()

pygame.quit()
sys.exit()