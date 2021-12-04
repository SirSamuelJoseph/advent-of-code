import unittest
import increase

class TestCountIncreases(unittest.TestCase):
    testInput = [line.rstrip() for line in open("2021/1/testinput.txt")]
    def test_count_increases(self):
        count = increase.countIncreases(self.testInput)
        self.assertEqual(count, 7, "Wrong Count")
    
    def test_count_increases_window(self):
        count = increase.countIncreasesWindows(self.testInput, 3)
        self.assertEqual(count, 5, "Wrong Count")
