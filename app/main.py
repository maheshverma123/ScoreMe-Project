import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Square")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game variables
square_size = 50
score = 0
font = pygame.font.SysFont(None, 36)

# Function to display the score
def display_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Function to move the square to a random position
def move_square():
    return random.randint(0, WIDTH - square_size), random.randint(0, HEIGHT - square_size)

# Main game loop
def game_loop():
    global score
    clock = pygame.time.Clock()
    square_x, square_y = move_square()

    # Main game loop
    while True:
        screen.fill(WHITE)  # Fill the screen with white
        display_score()  # Display the score

        # Draw the square
        pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse click to catch the square
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if square_x <= mouse_x <= square_x + square_size and square_y <= mouse_y <= square_y + square_size:
                    score += 1
                    square_x, square_y = move_square()  # Move the square to a new random position

        pygame.display.update()  # Update the display
        clock.tick(30)  # Set the frame rate to 30 frames per second

# Run the game
if __name__ == "__main__":
    game_loop()
