def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    #Return True if valid, False otherwise

    #Identify if the guess is already in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #Identify if the guess is already in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #Identify the 3x3 grid we are and verify
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def sudoku_solver(puzzle):
    row, col = find_next_empty(puzzle)

    #Return True if the puzzle is already full-filled (solved)
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if sudoku_solver(puzzle):  
                return True

            puzzle[row][col] = -1  

    return False  

if __name__ == '__main__':
    ex_board = [
        [ 3,  9, -1,   -1,  5, -1,  -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,  -1, -1,  5],
        [-1, -1, -1,    7, -1,  9,  -1,  8, -1],

        [-1,  5, -1,   -1,  6,  8,  -1, -1, -1],
        [ 2, -1,  6,   -1, -1,  3,  -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,  -1, -1,  4],

        [ 5, -1, -1,   -1, -1, -1,  -1, -1, -1],
        [ 6,  7, -1,   -1, -1,  5,  -1,  4, -1],
        [-1, -1,  9,   -1, -1, -1,   2, -1, -1],
    ]
    
    solved = sudoku_solver(ex_board)
    print(solved)
    for row in ex_board:
        print(row)