class PuzzleState:
    def __init__(self, board, zero_pos, moves=0, previous=None, move=None):
        self.board = tuple(tuple(row) for row in board)
        self.zero_pos = zero_pos
        self.moves = moves
        self.previous = previous
        self.move = move
        self.size = len(board)
        self.goal = self.generate_goal()
        self.heuristic_val = self.heuristic()

    def generate_goal(self):
        return (
            (1, 2, 3, 4),
            (5, 6, 7, 8),
            (9, 10, 11, 12),
            (13, 14, 15, 0)
        )

    def is_goal(self):
        return self.board == self.goal

    def get_neighbors(self):
        neighbors = []
        x, y = self.zero_pos
        directions = {
            (-1, 0): 'Up',
            (1, 0): 'Down',
            (0, -1): 'Left',
            (0, 1): 'Right'
        }

        for (dx, dy), move in directions.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                new_board = [list(row) for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append((new_board, (new_x, new_y), move))
        return neighbors

    def heuristic(self):
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                val = self.board[i][j]
                if val != 0:
                    target_x = (val - 1) // self.size
                    target_y = (val - 1) % self.size
                    distance += abs(i - target_x) + abs(j - target_y)
        return distance

    def __lt__(self, other):
        return (self.moves + self.heuristic_val) < (other.moves + other.heuristic_val)