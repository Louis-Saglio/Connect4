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
