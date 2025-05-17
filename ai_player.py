from collections import deque

class AIPlayer:
    def __init__(self, block_size, width, height):
        self.block_size = block_size
        self.width = width
        self.height = height

    def get_direction(self, head, body, food):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
        visited = set()
        queue = deque([(head, [])])
        body_set = set(body[1:])  # exclude head for safety

        while queue:
            current_pos, path = queue.popleft()
            if current_pos == food:
                return path[0] if path else (0, 0)

            for dx, dy in directions:
                new_x = current_pos[0] + dx * self.block_size
                new_y = current_pos[1] + dy * self.block_size
                new_pos = (new_x, new_y)

                if (0 <= new_x < self.width and
                    0 <= new_y < self.height and
                    new_pos not in body_set and
                    new_pos not in visited):

                    visited.add(new_pos)
                    queue.append((new_pos, path + [(dx, dy)]))

        # No path found — fallback to safe move
        for dx, dy in directions:
            new_x = head[0] + dx * self.block_size
            new_y = head[1] + dy * self.block_size
            new_pos = (new_x, new_y)
            if (0 <= new_x < self.width and
                0 <= new_y < self.height and
                new_pos not in body_set):
                return (dx, dy)

        return (0, 0)  # no valid moves
