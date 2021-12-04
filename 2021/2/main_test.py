import unittest
import main

class TestGetPosition(unittest.TestCase):
    testInput = [line.rstrip() for line in open("2021/2/testinput.txt")]
    def test_get_position(self):
        pos = main.getPositionFromDirections(testInput)
        self.assertEqual(count, 150, "Wrong Place")
    
    def test_get_complex_position(self):
        pos = main.getComplexPositionFromDirections(testInput)
        self.assertEqual(count, 5, "Wrong Place")