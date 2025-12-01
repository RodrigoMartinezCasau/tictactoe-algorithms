# AI to play solo mode
# Minimax only avaible in 3x3 board 

# Minimax requirement to check for the minimun or maximum value
from math import inf


class AI:
    def __init__(self, symbol):
        self.symbol = symbol
        self.opponent = 'O' if symbol == 'X' else 'X'

    def minimax(self, board, is_maximizing):
        # Check for the best posible move 
        winner = board.check_winner()
        if winner == self.symbol:
            return 1
        elif winner == self.opponent:
            return -1
        elif board.is_full():
            return 0

        if is_maximizing: # Maximizing the value
            best_score = -inf
            for (r, c) in board.get_empty_cells():
                board.grid[r][c] = self.symbol
                score = self.minimax(board, False)
                board.grid[r][c] = ' '
                if score > best_score:
                    best_score = score
            return best_score
        else: # Minimizing the value 
            best_score = inf
            for (r, c) in board.get_empty_cells():
                board.grid[r][c] = self.opponent
                score = self.minimax(board, True)
                board.grid[r][c] = ' '
                if score < best_score:
                    best_score = score
            return best_score
        
    # Here we evaluate the best possible moves 
    def best_move(self, board):
        best_score = -inf
        move = None
        for (r, c) in board.get_empty_cells():
            board.grid[r][c] = self.symbol
            score = self.minimax(board, False)
            board.grid[r][c] = ' '
            if score > best_score:
                best_score = score
                move = (r, c)
        return move
    
    # Minimax chooses its best move 
    def make_move(self, board):
        r, c = self.best_move(board)
        board.make_move(r, c, self.symbol)
        print(f"AI plays at row {r+1}, col {c+1}")
