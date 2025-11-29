import unittest
from game import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_empty_board(self):
        game = TicTacToe()
        self.assertEqual(game.check_state(), None)

    def test_row_win(self):
        game = TicTacToe()
        game.play_turn(0, 0)
        game.play_turn(1, 0)
        game.play_turn(0, 1)
        game.play_turn(1, 1)
        game.play_turn(0, 2)
        self.assertEqual(game.check_state(), "X")

    def test_column_win(self):
        game = TicTacToe()
        game.play_turn(0, 0)
        game.play_turn(0, 1)
        game.play_turn(1, 0)
        game.play_turn(1, 1)
        game.play_turn(2, 0)
        self.assertEqual(game.check_state(), "X")

    def test_diagonal_win(self):
        game = TicTacToe()
        game.play_turn(0, 0)
        game.play_turn(0, 1)
        game.play_turn(1, 1)
        game.play_turn(0, 2)
        game.play_turn(2, 2)
        self.assertEqual(game.check_state(), "X")

    def test_draw(self):
        game = TicTacToe()
        moves = [
            (0,0), (0,1),
            (0,2), (1,1),
            (1,0), (1,2),
            (2,0), (2,2),
            (2,1)
        ]
        for r, c in moves:
            game.play_turn(r, c)
            game.switch()

        self.assertEqual(game.check_state(), "draw")

if __name__ == '__main__':
    unittest.main()
