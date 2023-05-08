import pygame
import random

# Set up the game window
window_width = 640
window_height = 480
pygame.init()
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define the colors
green = (0, 154, 23)
black = (0, 0, 0)
red = (200, 50, 50)

# Define the game variables
snake_block_size = 20
snake_speed = 15

# Define the font
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    """
    Displays a message on the screen in the specified color.
    """
    message = font_style.render(msg, True, color)
    game_window.blit(message, [window_width / 6, window_height / 3])

def display_score(score):
    """
    Displays the current score on the screen.
    """
    score_surface = font_style.render(f"Score: {score}", True, black)
    game_window.blit(score_surface, (10, 10))


def gameLoop():
    """
    Runs the game loop.
    """
    game_over = False
    game_close = False

    # Set up the initial snake position and movement
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # Set up the initial food position
    foodx = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
    foody = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size

    snake_List = []
    Length_of_snake = 1
    score = 0

    while not game_over:

        while game_close == True:
            game_window.fill(green)
            message(f"You Lost! Press Q-Quit or C-Play Again \n Score: {score}", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if the snake has hit the wall
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Draw the snake and the food on the screen
        game_window.fill(green)
        pygame.draw.rect(game_window, red, [foodx, foody, snake_block_size, snake_block_size])
        pygame.draw.rect(game_window, black, [x1, y1, snake_block_size, snake_block_size])

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            # Update the position of the food
            foodx = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
            foody = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size

            # Increase the score and length of the snake
            score += 1
            print(f"Score: {score}")
            Length_of_snake += 1
            display_score(score)

        # Add the new segment to the snake's body
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove the oldest segment of the snake's body if it hasn't eaten food
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake has collided with itself
        for eachSegment in snake_List[:-1]:
            if eachSegment == snake_Head:
                game_close = True

        # Draw the snake body
        for segment in snake_List:
            pygame.draw.rect(game_window, black, [segment[0], segment[1], snake_block_size, snake_block_size])
            display_score(score)
            
        pygame.display.update()

        # Set the game speed
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Quit pygame and exit the program
    pygame.quit()
    quit()



gameLoop()
