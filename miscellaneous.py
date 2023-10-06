# miscellaneous question:**Implement n-Queen’s Problem.

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(["".join(["Q" if col == 1 else "." for col in row]) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0  # Backtrack
    backtrack(0)
    return solutions
def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print("\n")
n = 8 
solutions = solve_n_queens(n)
if solutions:
    print(f"Found {len(solutions)} solutions for {n}-Queens:")
    print_solutions(solutions)
else:
    print(f"No solutions found for {n}-Queens.")
