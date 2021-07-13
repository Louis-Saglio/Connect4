from unittest import TestCase

from env import Connect4, IllegalMove


class TestConnect4(TestCase):
    def test_play(self):
        game = Connect4()
        game.play(0)
        game.play(0)
        game.play(0)
        game.play(0)
        game.play(1)
        game.play(1)
        game.play(1)
        game.play(9)
        self.assertListEqual(game.grid[0], [1, 2, 1, 2, 0, 0, 0, 0, 0, 0])
        self.assertListEqual(game.grid[1], [1, 2, 1, 0, 0, 0, 0, 0, 0, 0])
        self.assertListEqual(game.grid[9], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_play_not_in_grid(self):
        game = Connect4()
        with self.assertRaises(IllegalMove):
            game.play(11)

    def test_play_full_column(self):
        game = Connect4()
        with self.assertRaises(IllegalMove):
            for _ in range(11):
                game.play(0)

    def test_detect_line_in_col(self):
        game = Connect4()
        self.assertEqual(game._detect_line_in_col(), 0)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        self.assertEqual(game._detect_line_in_col(), 1)

    def test_detect_line_in_col_1(self):
        game = Connect4()
        self.assertEqual(game._detect_line_in_col(), 0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        self.assertEqual(game._detect_line_in_col(), 1)

    def test_detect_line_in_row(self):
        game = Connect4()
        game.play(4)
        game.play(4)
        game.play(5)
        game.play(5)
        game.play(5)
        game.play(6)
        game.play(6)
        game.play(7)
        game.play(7)
        game.play(8)
        game.play(8)
        self.assertEqual(game._detect_line_in_row(), 0)
        game.play(9)
        self.assertEqual(game._detect_line_in_row(), 2)

    # noinspection DuplicatedCode
    def test_str(self):
        game = Connect4()
        expected = """0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0"""
        self.assertEqual(expected, str(game))
        game.play(0)
        game.play(0)
        game.play(0)
        game.play(0)
        game.play(1)
        game.play(1)
        game.play(1)
        game.play(9)
        expected = """0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0
2  0  0  0  0  0  0  0  0  0
1  1  0  0  0  0  0  0  0  0
2  2  0  0  0  0  0  0  0  0
1  1  0  0  0  0  0  0  0  2"""
        self.assertEqual(expected, str(game))

    def test_detect_line_in_diagonal_right(self):
        game = Connect4()
        self.assertEqual(game._detect_line_in_diagonal_right(), 0)
        game.play(2)
        game.play(0)
        game.play(3)
        game.play(0)
        game.play(3)
        game.play(4)
        game.play(4)
        game.play(4)
        game.play(5)
        game.play(5)
        game.play(5)
        game.play(6)
        game.play(6)
        game.play(6)
        game.play(6)
        self.assertEqual(game._detect_line_in_diagonal_right(), 1)

    def test_detect_line_in_diagonal_left(self):
        game = Connect4()
        self.assertEqual(game._detect_line_in_diagonal_left(), 0)
        game.play(8)
        game.play(8)
        game.play(7)
        game.play(0)
        game.play(7)
        game.play(0)
        game.play(6)
        game.play(6)
        game.play(6)
        game.play(5)
        game.play(5)
        game.play(5)
        game.play(5)
        self.assertEqual(game._detect_line_in_diagonal_left(), 1)

    def test_detect_winner(self):
        game = Connect4()
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        game.play(0)
        game.play(1)
        self.assertEqual(game.detect_winner(), 0)
        game.play(0)
        self.assertEqual(game.detect_winner(), 1)
