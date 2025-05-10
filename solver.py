import heapq

from state import PuzzleState

def astar_puzzle(start_board):
    start_zero = next((i, j) for i in range(4) for j in range(4) if start_board[i][j] == 0) # search at the start state to fine the zero pos 
    start_state = PuzzleState(start_board, start_zero) # start state store the start board an the zero pos

    open_set = [] 
    heapq.heappush(open_set, start_state)
    visited = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.board in visited:
            continue
        visited.add(current.board)

        if current.is_goal():
            path = []
            while current:
                path.append((current.move, current.board))
                current = current.previous
            return path[::-1]

        for neighbor_board, zero_pos, move in current.get_neighbors():
            neighbor = PuzzleState(neighbor_board, zero_pos, current.moves + 1, current, move)
            if neighbor.board not in visited:
                heapq.heappush(open_set, neighbor)

    return None