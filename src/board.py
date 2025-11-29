class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]

    def reset(self):
        self.grid = [[" " for _ in range(self.size)] for _ in range(self.size)]

    def place(self, row, col, symbol):
        """
        Coloca la ficha en (row, col) si está libre.
        """
        if self.grid[row][col] != " ":
            return False
        self.grid[row][col] = symbol
        return True

    def is_full(self):
        """
        Comprueba si el tablero está completo.
        """
        for row in self.grid:
            if " " in row:
                return False
        return True

    def __str__(self):
        """
        Representación bonita del tablero.
        """
        rows = []
        for r in range(self.size):
            row = " | ".join(self.grid[r])
            rows.append(row)
        line = "\n" + ("-" * (self.size * 4 - 1)) + "\n"
        return line.join(rows)
