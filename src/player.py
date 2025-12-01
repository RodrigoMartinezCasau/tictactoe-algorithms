# Each player gets to choose the position by indicating the cordinates of the move 

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        size = board.size
        while True:
            try:
                row = int(input(f"Row (1-{size}): ")) - 1
                col = int(input(f"Col (1-{size}): ")) - 1
            except ValueError:
                print("Please enter numbers.")
                continue

            if board.make_move(row, col, self.symbol):
                break
            else:
                print("Invalid move, try again.")
