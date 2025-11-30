# game.py

from board import Board
from player import Player
from ai import AI

class Game:
    def __init__(self, vs_ai: bool):
        self.vs_ai = vs_ai
        self.board = None
        self.current_symbol = 'X'
        self.player_x = None
        self.player_o = None
        self.ai = None

        if vs_ai:
            # tablero fijo 3x3 para IA
            self.board = Board(3)
            first = input("Do you want to go first? (y/n): ").strip().lower()
            if first == 'y':
                self.player_x = Player('X')
                self.ai = AI('O')
                self.player_o = None
            else:
                self.player_x = None
                self.ai = AI('X')
                self.player_o = Player('O')
        else:
            # jugador vs jugador, tamaño 3-7
            size = 0
            while size < 3 or size > 7:
                try:
                    size = int(input("Choose board size (3-7): "))
                except ValueError:
                    print("Please enter a number.")
            self.board = Board(size)
            self.player_x = Player('X')
            self.player_o = Player('O')

    def switch_turn(self):
        self.current_symbol = 'O' if self.current_symbol == 'X' else 'X'

    def play(self):
        while True:
            print("\nCurrent board:")
            print(self.board)

            winner = self.board.check_winner()
            if winner:
                print(f"Player {winner} wins!")
                break

            if self.board.is_full():
                print("It's a draw!")
                break

            if self.vs_ai:
                # IA mode
                if self.current_symbol == 'X':
                    if self.player_x is not None:
                        self.player_x.make_move(self.board)
                    else:
                        self.ai.make_move(self.board)
                else:
                    if self.player_o is not None:
                        self.player_o.make_move(self.board)
                    else:
                        self.ai.make_move(self.board)
            else:
                # human vs human
                if self.current_symbol == 'X':
                    self.player_x.make_move(self.board)
                else:
                    self.player_o.make_move(self.board)

            self.switch_turn()
