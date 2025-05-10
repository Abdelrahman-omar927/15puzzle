import random

def print_board(board):
    for row in board:
        print(" ".join(f"{val:2}" if val != 0 else "  " for val in row))
    print()

def print_solution_with_actions(path):
    for step, (action, board) in enumerate(path):
        move_text = f"Move {step}: {action}" if action else "Initial State"
        print(move_text)
        print_board(board)

def is_solvable(board):
    flat = [num for row in board for num in row if num != 0]
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1

    size = len(board)
    empty_row = next(i for i in range(size) if 0 in board[i])
    empty_row_from_bottom = size - empty_row

    if size % 2 != 0:
        return inversions % 2 == 0
    else:
        return (empty_row_from_bottom % 2 == 0) != (inversions % 2 == 0)

def generate_easy_board(move_count=10):
    goal = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    x, y = 3, 3
    board = [row[:] for row in goal]

    previous_pos = None

    for _ in range(move_count):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                if previous_pos == (new_x, new_y):  
                    continue
                board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
                previous_pos = (x, y)
                x, y = new_x, new_y
                break
    return board