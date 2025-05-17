import pygame
import random

RED = (255, 0, 0)

class Food:
    def __init__(self, block_size, width, height, snake_body):
        self.block_size = block_size
        self.width = width
        self.height = height
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        cols = self.width // self.block_size
        rows = self.height // self.block_size
        while True:
            x = random.randint(0, cols - 1) * self.block_size
            y = random.randint(0, rows - 1) * self.block_size
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, self.block_size, self.block_size))
