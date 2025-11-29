from board import Board
from player import Player
from algorithms import check_winner

class TicTacToe:
    def __init__(self, size=3):
        self.board = Board(size)
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current = self.player1

    def switch(self):
        self.current = (
            self.player2 if self.current == self.player1
            else self.player1
        )

    def play_turn(self, row, col):
        """
        Intenta jugar un turno. Devuelve True si ok, False si casilla ocupada.
        """
        return self.board.place(row, col, self.current.symbol)

    def check_state(self):
        """
        Devuelve:
        - 'X' o 'O' si hay ganador
        - 'draw' si hay empate
        - None si el juego sigue
        """
        winner = check_winner(self.board)
        if winner:
            return winner

        if self.board.is_full():
            return "draw"

        return None

    def __str__(self):
        return str(self.board)
