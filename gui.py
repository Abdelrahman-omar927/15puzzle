import tkinter as tk
from tkinter import messagebox
from solver import astar_puzzle
from utils import generate_easy_board

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("15-Puzzle Solver")
        self.root.configure(bg='black')

        self.grid_frame = tk.Frame(root, bg='black')
        self.grid_frame.pack(pady=20)

        self.control_frame = tk.Frame(root, bg='black')
        self.control_frame.pack(pady=10)

        self.current_board = generate_easy_board(30)
        self.tiles = []
        self.solution_path = []
        self.current_step = 0

        self.create_widgets()
        self.update_grid()

    def create_widgets(self):
        for i in range(4):
            row = []
            for j in range(4):
                tile = tk.Label(self.grid_frame,
                               text="",
                               width=4,
                               height=2,
                               font=('Arial', 24, 'bold'),
                               relief="ridge",
                               borderwidth=2,
                               bg='black',
                               fg='white',
                               highlightbackground='white',
                               highlightcolor='white')
                tile.grid(row=i, column=j, padx=2, pady=2)
                row.append(tile)
            self.tiles.append(row)

        button_style = {'bg': 'black', 'fg': 'white', 'font': ('Arial', 12, 'bold')}

        self.generate_btn = tk.Button(self.control_frame,
                                     text="Generate New Puzzle",
                                     command=self.generate_puzzle,
                                     **button_style)
        self.generate_btn.pack(side=tk.LEFT, padx=5)

        self.solve_btn = tk.Button(self.control_frame,
                                  text="Solve",
                                  command=self.start_solving,
                                  **button_style)
        self.solve_btn.pack(side=tk.LEFT, padx=5)

        self.status_label = tk.Label(self.root,
                                    text="Ready",
                                    font=('Arial', 12),
                                    bg='black',
                                    fg='white')
        self.status_label.pack(pady=10)

    def update_grid(self):
        for i in range(4):
            for j in range(4):
                val = self.current_board[i][j]
                text = str(val) if val != 0 else ""
                self.tiles[i][j].config(text=text)


    def generate_puzzle(self):
        self.current_board = generate_easy_board(50)
        self.solution_path = []
        self.current_step = 0
        self.update_grid()
        self.status_label.config(text="New puzzle generated")

    def start_solving(self):
        self.status_label.config(text="Solving...")
        self.root.update()

        solution = astar_puzzle(self.current_board)

        if not solution:
            messagebox.showerror("Error", "No solution found!")
            self.status_label.config(text="No solution found")
            return

        self.solution_path = solution
        self.current_step = 0
        self.status_label.config(text=f"Found solution with {len(solution)-1} moves")
        self.animate_solution()

    def animate_solution(self):
        if self.current_step >= len(self.solution_path):
            self.status_label.config(text="Solution complete!")
            return

        _, board_state = self.solution_path[self.current_step]
        self.current_board = [list(row) for row in board_state]
        self.update_grid()

        move_number = self.current_step
        self.status_label.config(text=f"Showing move {move_number}/{len(self.solution_path)-1}")

        self.current_step += 1
        self.root.after(500, self.animate_solution)

if __name__ == "__main__":

    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()




