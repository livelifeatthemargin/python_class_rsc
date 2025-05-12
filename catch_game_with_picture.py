import pygame
import random
import sys

def main():
    # 1) Initialize Pygame and create a window
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Catch the Falling Blocks")

    clock = pygame.time.Clock()

    # 2) Define some basic colors (R, G, B)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED   = (255, 0, 0)
    BLUE  = (0, 0, 255)

    # 3) Player setup
    player_img = pygame.image.load("player.png").convert_alpha()  # use convert_alpha() for transparency
    player_width = 500
    player_height = 50
    player_x = screen_width // 2 - player_width // 2  # center on screen
    player_y = screen_height - player_height - 10     # near the bottom
    player_speed = 7

    # 4) Score and lives
    score = 0
    lives = 3

    # 5) Text (font) setup
    font = pygame.font.SysFont(None, 36)

    # 6) Falling blocks setup
    block_size = 50
    block_speed_min = 3
    block_speed_max = 7
    num_blocks = 5
    blocks = []

    # Helper function to create a new random block
    def create_block():
        x = random.randint(0, screen_width - block_size)
        y = random.randint(-300, -50)  # spawn above the screen
        speed = random.randint(block_speed_min, block_speed_max)
        return [x, y, speed]

    # Initialize a list of blocks
    for _ in range(num_blocks):
        blocks.append(create_block())

    # Game over flag
    game_over = False

    # 7) Main game loop
    while True:
        # Limit FPS to ~60
        clock.tick(60)

        # Fill screen with white
        screen.fill(WHITE)

        # Handle events (exit on window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # If we haven't hit Game Over, update gameplay
        if not game_over:

            # Draw player
            player_img = pygame.image.load("player.png").convert_alpha()
            player_img = pygame.transform.scale(player_img, (player_width, player_height))  # same size as the rectangle
            player_rect = player_img.get_rect(topleft=(player_x, player_y))
            screen.blit(player_img, (player_x, player_y))    

            keys = pygame.key.get_pressed()

            # Move player left or right
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
                player_x += player_speed

            # Update each block's position
            for i, block in enumerate(blocks):
                block[1] += block[2]  # block[1] = y position, block[2] = speed down

                # If a block goes off the bottom of the screen, lose a life and respawn it at the top
                if block[1] > screen_height:
                    lives -= 1
                    blocks[i] = create_block()
                    if lives <= 0:
                        game_over = True

            # Check collisions: if player catches a block, increase score and respawn the block
            for i, block in enumerate(blocks):
                block_rect = pygame.Rect(block[0], block[1], block_size, block_size)
                if player_rect.colliderect(block_rect):
                    score += 1
                    blocks[i] = create_block()

        # Draw blocks
        for block in blocks:
            pygame.draw.rect(screen, RED, (block[0], block[1], block_size, block_size))

        # Draw score and lives
        score_text = font.render(f"Score: {score}", True, BLACK)
        lives_text = font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        # If game over, show message and let the player restart or quit
        if game_over:
            game_over_text = font.render("GAME OVER", True, RED)
            screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 30))
            info_text = font.render("Press R to Restart or Q to Quit", True, RED)
            screen.blit(info_text, (screen_width // 2 - 180, screen_height // 2 + 10))

            # Check if user presses R or Q
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset all game variables
                score = 0
                lives = 3
                blocks = [create_block() for _ in range(num_blocks)]
                player_x = screen_width // 2 - player_width // 2
                player_y = screen_height - player_height - 10
                game_over = False
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        # Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()