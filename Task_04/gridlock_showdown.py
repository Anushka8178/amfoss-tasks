def check_winner(grid):
    for sym in ['X', 'O', '+']:
        # Check rows and columns
        for i in range(3):
            if all(grid[i][j] == sym for j in range(3)) or all(grid[j][i] == sym for j in range(3)):
                return sym

        # Check diagonals
        if all(grid[i][i] == sym for i in range(3)) or all(grid[i][2 - i] == sym for i in range(3)):
            return sym

    return "DRAW"

# Function to solve each test case
def solve_test_case():
    # Input
    grid = [list(input().strip()) for k in range(3)]
    winner = check_winner(grid)
    print(winner)

# Main function
t = int(input())
for k in range(t):
    solve_test_case()
