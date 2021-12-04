import unittest
import bingo

class TestGetBinarySystemResults(unittest.TestCase):
    testInput = [line.rstrip() for line in open("2021/4/testinput.txt")]
    def test_get_power_consumption(self):
        score = bingo.GameState(self.testInput, 5).playGame()
        self.assertEqual(score, 4512, "Wrong Value")
    
    def test_get_life_support_rating(self):
        score = bingo.GameState(self.testInput, 5).playGameUntilLastWin()
        self.assertEqual(score, 1924, "Wrong Value")