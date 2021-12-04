import unittest
import main

class TestCountIncreases(unittest.TestCase):
    testInput = [line.rstrip() for line in open("testinput.txt")]
    def test_count_increases(self):
        count = main.countIncreases(self.testInput)
        self.assertEqual(count, 7, "Wrong Count")
    
    def test_count_increases_window(self):
        count = main.countIncreasesWindows(self.testInput, 3)
        self.assertEqual(count, 5, "Wrong Count")



if __name__ == '__main__':
    unittest.main()