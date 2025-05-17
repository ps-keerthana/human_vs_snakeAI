import pygame
import sys
from snake import Snake
from food import Food
from ai_player import AIPlayer

# Constants
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game AI vs Manual Comparison")

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def run_manual_game():
    snake = Snake(100, 100, BLOCK_SIZE)
    food = Food(BLOCK_SIZE, WIDTH, HEIGHT, snake.body)
    food_log = []
    direction_map = {
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1),
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0)
    }

    print("Manual game starts now...")
    move_count = 0
    while True:
        screen.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in direction_map:
                    snake.change_direction(direction_map[event.key])

        snake.move()
        move_count += 1
        snake.draw(screen)
        food.draw(screen)

        if snake.body[0] == food.position:
            food_log.append(food.position)
            snake.grow()
            food = Food(BLOCK_SIZE, WIDTH, HEIGHT, snake.body)

        if snake.check_collision():
            print("Manual game over! Foods eaten:", len(food_log))
            pygame.time.wait(1000)
            return food_log, len(food_log), move_count

        pygame.display.update()
        clock.tick(FPS)

def run_ai_game(food_log):
    snake = Snake(100, 100, BLOCK_SIZE)
    ai = AIPlayer(BLOCK_SIZE, WIDTH, HEIGHT)
    food = Food(BLOCK_SIZE, WIDTH, HEIGHT, snake.body)

    food_index = 0
    move_count = 0
    print("Now AI will play with the same food positions...")

    while food_index < len(food_log):
        screen.fill(BLACK)
        draw_grid()

        food.position = tuple(food_log[food_index])  # use saved food position
        direction = ai.get_direction(snake.body[0], snake.body, food.position)
        if direction != (0, 0):
            snake.change_direction(direction)

        snake.move()
        move_count += 1
        snake.draw(screen)
        food.draw(screen)

        if snake.body[0] == food.position:
            snake.grow()
            food_index += 1

        if snake.check_collision():
            print("AI game over early! Foods eaten:", food_index)
            pygame.time.wait(1000)
            return food_index, move_count

        pygame.display.update()
        clock.tick(FPS)

    print("AI finished all food targets.")
    return food_index, move_count

def main():
    food_log, manual_foods, manual_moves = run_manual_game()
    pygame.display.update()
    pygame.time.wait(5000)
    ai_foods, ai_moves = run_ai_game(food_log)

    print("\nComparison Result:")
    print("Manual player:", manual_foods, "foods in", manual_moves, "moves")
    print("AI player:", ai_foods, "foods in", ai_moves, "moves")

    if ai_foods == manual_foods:
        efficiency = (ai_moves / manual_moves) * 100 if manual_moves > 0 else 0
        accuracy = (ai_moves / manual_moves) * 100 if manual_moves > 0 else 0
        print(f"Manual Player Accuracy: {accuracy:.2f}% compared to AI's optimal path")
    else:
        print("AI did not complete as many foods as manual. No accuracy comparison.")

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()