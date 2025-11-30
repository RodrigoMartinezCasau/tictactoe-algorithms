# board.py

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def make_move(self, row, col, symbol):
        if 0 <= row < self.size and 0 <= col < self.size:
            if self.grid[row][col] == ' ':
                self.grid[row][col] = symbol
                return True
        return False

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def get_empty_cells(self):
        empty = []
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == ' ':
                    empty.append((r, c))
        return empty

    def check_winner(self):
        n = self.size
        g = self.grid

        # rows
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

        # columns
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

        # main diagonal
        first = g[0][0]
        if first != ' ':
            win = True
            for i in range(1, n):
                if g[i][i] != first:
                    win = False
                    break
            if win:
                return first

        # anti-diagonal
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

    def __str__(self):
        # header
        result = "   " + " ".join(str(i + 1) for i in range(self.size)) + "\n"
        for i, row in enumerate(self.grid):
            result += str(i + 1) + "  " + " ".join(row) + "\n"
        return result
