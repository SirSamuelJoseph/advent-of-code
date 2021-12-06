import unittest
import lanternfish

class TestGetLanternfishCount(unittest.TestCase):
    testInput = [line.rstrip() for line in open("2021/6/testinput.txt")]
    def test_get_short_count(self):
        start = lanternfish.initState(self.testInput)
        count = lanternfish.advanceGivenDays(start, 80)
        self.assertEqual(count, 5934, "Wrong Value")

    def test_get_big_count(self):
        start = lanternfish.initState(self.testInput)
        count = lanternfish.advanceGivenDays(start, 80)
        self.assertEqual(count, 5934, "Wrong Value")