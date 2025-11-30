import unittest
from src.board import Board
from src.game import Game

class TestTicTacToe(unittest.TestCase):

    def test_empty_board(self):
        b = Board(3)
        for row in b.grid:
            self.assertEqual(row.count(' '), 3)

    def test_place_move(self):
        b = Board(3)
        b.place_move(0, 0, 'X')
        self.assertEqual(b.grid[0][0], 'X')

    def test_row_win(self):
        b = Board(3)
        b.grid = [
            ['X', 'X', 'X'],
            [' ', 'O', ' '],
            ['O', ' ', ' ']
        ]
        self.assertEqual(b.check_winner(), 'X')

    def test_column_win(self):
        b = Board(3)
        b.grid = [
            ['O', 'X', ' '],
            ['O', 'X', ' '],
            ['O', ' ', 'X']
        ]
        self.assertEqual(b.check_winner(), 'O')

    def test_diagonal_win(self):
        b = Board(3)
        b.grid = [
            ['X', 'O', ' '],
            ['O', 'X', ' '],
            [' ', ' ', 'X']
        ]
        self.assertEqual(b.check_winner(), 'X')

    def test_no_win(self):
        b = Board(3)
        b.grid = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertIsNone(b.check_winner())

if __name__ == "__main__":
    unittest.main()
