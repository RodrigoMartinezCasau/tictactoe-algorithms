# game to be determined by the players decissions
# multiple possibilities to be selected and managed here

# We get the functions from the different files
from board import Board
from player import Player
from ai import AI

# We create a class to individualize each game
class Game:
    def __init__(self, vs_ai: bool):
        # Defining the players and the characteristics of the game starting from None 
        self.vs_ai = vs_ai
        self.board = None
        self.current_symbol = 'X'
        self.player_x = None
        self.player_o = None
        self.ai = None

        # If the player selects the AI mode:
        if vs_ai:
            # board 3x3 for IA (if bigger, too many possibilities for the AI to think)
            self.board = Board(3)
            first = input("Do you want to go first? (y/n): ").strip().lower() 
            # To check which symbols is used for who 
            if first == 'y':
                self.player_x = Player('X')
                self.ai = AI('O')
                self.player_o = None
            else:
                self.player_x = None
                self.ai = AI('X')
                self.player_o = Player('O')

        # if AI not chosen, board size can be selected - Ask the user
        else:
            size = 0
            while size < 3 or size > 7:
                try:
                    size = int(input("Choose board size (3-7): "))
                except ValueError:
                    print("Please enter a number.")
            self.board = Board(size)
            self.player_x = Player('X')
            self.player_o = Player('O')
            
    # After one play by one user, the other gets to move        
    def switch_turn(self):
        self.current_symbol = 'O' if self.current_symbol == 'X' else 'X'

    # Play the game updating the board and checking for winners, or a draw!    
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
