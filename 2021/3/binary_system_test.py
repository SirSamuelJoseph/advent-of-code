import unittest
import binary_system

class TestGetBinarySystemResults(unittest.TestCase):
    testInput = [line.rstrip() for line in open("2021/3/testinput.txt")]
    def test_get_power_consumption(self):
        val = binary_system.getPowerConsumption(self.testInput)
        self.assertEqual(val, 198, "Wrong Value")
    
    def test_get_life_support_rating(self):
        val = binary_system.getLifeSupportRating(self.testInput)
        self.assertEqual(val, 230, "Wrong Value")