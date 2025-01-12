import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake and food initialization
snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake body
snake_dir = (CELL_SIZE, 0)  # Initial direction
food = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
score = 0

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def check_collision(snake):
    head = snake[0]
    # Check if the snake collides with the walls
    if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
        return True
    # Check if the snake collides with itself
    if head in snake[1:]:
        return True
    return False

def main():
    global snake, snake_dir, food, score
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Control snake direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
            snake_dir = (0, -CELL_SIZE)
        if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
            snake_dir = (0, CELL_SIZE)
        if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
            snake_dir = (-CELL_SIZE, 0)
        if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
            snake_dir = (CELL_SIZE, 0)

        # Move the snake
        new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake = [new_head] + snake[:-1]

        # Check if the snake eats the food
        if snake[0] == food:
            snake.append(snake[-1])  # Grow the snake
            score += 1
            food = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

        # Check for collisions
        if check_collision(snake):
            print(f"Game Over! Your score: {score}")
            running = False

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        pygame.display.flip()

        # Control the frame rate
        clock.tick(10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()