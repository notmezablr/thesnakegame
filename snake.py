import pygame
import time
import random

# Initialize the game
pygame.init()

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# Set the width and height of the display
display_width = 800
display_height = 600

# Set the size of each block in the game
block_size = 20

# Set the speed of the snake
snake_speed = 15

# Set the font size
font_size = 30
font_style = pygame.font.SysFont(None, font_size)

# Create the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Create the clock
clock = pygame.time.Clock()

# Define the snake
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

# Display the score
def score(score):
    text = font_style.render("Score: " + str(score), True, black)
    game_display.blit(text, [0, 0])

# Run the game
def game_loop():
    game_over = False
    game_close = False

    # Set the starting position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Set the initial change in position
    x1_change = 0
    y1_change = 0

    # Create the snake list and length
    snake_list = []
    length_of_snake = 1

    # Set the initial position of the food
    foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # If the game is closed, display the game over message
        while game_close:
            game_display.fill(white)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            score(length_of_snake - 1)
            pygame.display.update()

            # Check for user input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Update the display
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        snake(block_size, snake_list)
        score(length_of_snake - 1)

        # Update the display
        pygame.display.update()

        # Check for food consumption
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        # Set the speed of the game
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

# Start the game loop
game_loop()