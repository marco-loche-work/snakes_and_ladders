import unittest


class MyTestCase(unittest.TestCase):

    game = Game()

    def test_case_1(self):
        self.assertEqual(self.game.play(1, 1), "Player 1 is on square 38")

    def test_case_2(self):
        self.assertEqual(self.game.play(1, 5), "Player 1 is on square 44")

    def test_case_3(self):
        self.assertEqual(self.game.play(6, 2), "Player 2 is on square 31")

    def test_case_4(self):
        self.assertEqual(self.game.play(1, 1), "Player 1 is on square 25")

