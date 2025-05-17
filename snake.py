import pygame

# Colors
GREEN = (0, 255, 0)

class Snake:
    def __init__(self, x, y, block_size):
        self.block_size = block_size
        self.body = [(x, y)]
        self.direction = (1, 0)  # Starts moving right
        self.grow_flag = False

    def change_direction(self, new_dir):
        # Prevent snake from reversing directly
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0] * self.block_size,
                    head_y + self.direction[1] * self.block_size)
        self.body.insert(0, new_head)

        if self.grow_flag:
            self.grow_flag = False  # only grow once
        else:
            self.body.pop()  # remove tail

    def grow(self):
        self.grow_flag = True

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, self.block_size, self.block_size))

    def check_collision(self):
        head = self.body[0]
        # Collides with walls
        if (head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 600):
            return True
        # Collides with itself
        if head in self.body[1:]:
            return True
        return False
