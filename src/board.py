# board checking for different possible outcomes 
# board can be of any size between 3x3 and 7x7 when not played against AI
# board works by checking if the previous element is equal to the following O(n)

class Board:
    # Timecomplexity: O(n^2)
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    # Timecomplexity: O(1)
    def make_move(self, row, col, symbol):
        if 0 <= row < self.size and 0 <= col < self.size:
            if self.grid[row][col] == ' ':
                self.grid[row][col] = symbol
                return True
        return False
    
    # Check for full board in case there is a draw
    # Timecomplexity: O(n^2)
    def is_full(self): 
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    # Check if cell is empty, then add the input
    # Timecomplexity: O(n^2)
    def get_empty_cells(self):
        empty = []
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == ' ':
                    empty.append((r, c))
        return empty
    
    # Checks for each one of possible winning ways
    # Does it by going through each cell since the board size is notnfixed
    # Timecomplexity: O(n^2)
    def check_winner(self):
        n = self.size
        g = self.grid

        # checking rows for a winner 
        for r in range(n):
            first = g[r][0]
            if first != ' ':
                win = True
                for c in range(1, n):
                    if g[r][c] != first:
                        win = False
                        break
                if win:
                    return first

        # checking columns for a winner
        for c in range(n):
            first = g[0][c]
            if first != ' ':
                win = True
                for r in range(1, n):
                    if g[r][r*0 + c] != first:  # simple, same column
                        win = False
                        break
                if win:
                    return first
                
        # for the diagonals we have to check each one of them, not iterating since there will always be 2
        # first diagonal
        first = g[0][0]
        if first != ' ':
            win = True
            for i in range(1, n):
                if g[i][i] != first:
                    win = False
                    break
            if win:
                return first

        # second diagonal
        first = g[0][n - 1]
        if first != ' ':
            win = True
            for i in range(1, n):
                if g[i][n - 1 - i] != first:
                    win = False
                    break
            if win:
                return first

        return None
    
    # Simply to determine the indexes of the number of rows and collums 
    # Timecomplexity: O(n^2)
    def __str__(self):
        result = "   " + " ".join(str(i + 1) for i in range(self.size)) + "\n"
        for i, row in enumerate(self.grid): # enumerate to split the value and the index 
            result += str(i + 1) + "  " + " ".join(row) + "\n"
        return result
