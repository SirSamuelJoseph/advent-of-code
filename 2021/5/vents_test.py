import unittest
import vents

class TestGetBinarySystemResults(unittest.TestCase):
    testInput = [line.rstrip() for line in open("2021/5/testinput.txt")]
    def test_get_vents_count(self):
        count = vents.getIntersectionsAboveOne(self.testInput, {}, False)
        self.assertEqual(score, 5, "Wrong Value")
    
    def test_get_vents_count_diagonal(self):
        count = vents.getIntersectionsAboveOne(self.testInput, {}, True)
        self.assertEqual(count, 12, "Wrong Value")