import pygame
import sys
from snake import Snake
from food import Food
from ai_player import AIPlayer
# Define constants here
WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 20
FPS = 10
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 60))  # extra space below grid for stats
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game AI vs Manual Comparison")

font = pygame.font.SysFont("comicsansms", 24)
game_over_font = pygame.font.SysFont("comicsansms", 72, bold=True)

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

font = pygame.font.SysFont("comicsansms", 16)  # smaller font

def draw_stats(food_eaten, moves, mode, fps):
    # Draw a black bar below the grid
    pygame.draw.rect(screen, (20, 20, 20), (0, HEIGHT, WIDTH, 60))

    # Color for mode text and stats
    if mode == "Manual":
        color = (0, 255, 0)  # bright green
    else:
        color = (0, 150, 255)  # nice blue

    # Prepare stats texts
    texts = [
        f"Food eaten: {food_eaten}",
        f"Moves: {moves}",
        f"Mode: {mode}",
        f"Speed (FPS): {int(fps)}"
    ]

    # Draw stats horizontally with some spacing
    padding = 15
    x_pos = 10
    y_pos = HEIGHT + 20

    for text in texts:
        label = font.render(text, True, color)
        screen.blit(label, (x_pos, y_pos))
        x_pos += label.get_width() + padding

    # Optional watermark - slightly transparent gray
    watermark_color = (100, 100, 100)
    watermark = font.render(f"{mode} MODE", True, watermark_color)
    screen.blit(watermark, (WIDTH - 110, HEIGHT + 30))

def show_game_over_stats(manual_foods, manual_moves, ai_foods, ai_moves):
    screen.fill((0,0,0))
    
    # Centered Game Over text
    game_over_text = game_over_font.render("GAME OVER", True, (255, 50, 50))
    rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//3))
    screen.blit(game_over_text, rect)

    # Stats summary
    accuracy = min(100, (ai_moves / manual_moves) * 100) if manual_moves > 0 else 0
    lines = [
        f"Manual player: {manual_foods} foods, {manual_moves} moves",
        f"AI player: {ai_foods} foods, {ai_moves} moves",
        f"Manual Player Accuracy: {accuracy:.2f}%",
        "Press any key to exit."
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + i * 30))
        screen.blit(text, rect)
    
    pygame.display.update()

    # Wait for user key to quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False
        clock.tick(30)  # Slow down the loop to avoid high CPU usage
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

    move_count = 0
    mode = "Manual"
    running = True
    while running:
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

        draw_stats(len(food_log), move_count, mode, FPS)


        if snake.check_collision():
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
    mode = "AI"

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

        draw_stats(food_index, move_count, mode, FPS)

        if snake.body[0] == food.position:
            snake.grow()
            food_index += 1

        if snake.check_collision():
            pygame.time.wait(1000)
            return food_index, move_count

        pygame.display.update()
        clock.tick(FPS)

    return food_index, move_count

def main():
    
    
    food_log, manual_foods, manual_moves = run_manual_game()
    pygame.time.wait(1000)  # short pause between games
    ai_foods, ai_moves = run_ai_game(food_log)

    print("\nComparison Result:")
    print("Manual player:", manual_foods, "foods in", manual_moves, "moves")
    print("AI player:", ai_foods, "foods in", ai_moves, "moves")

    accuracy = min(100, (ai_moves / manual_moves) * 100) if manual_moves > 0 else 0
    print(f"Manual Player Accuracy: {accuracy:.2f}% compared to AI's optimal path")

    show_game_over_stats(manual_foods, manual_moves, ai_foods, ai_moves)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
