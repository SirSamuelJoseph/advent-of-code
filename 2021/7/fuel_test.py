import unittest
import fuel

class TestGetFuelCost(unittest.TestCase):
    testInput = [line.rstrip().split(',') for line in open("2021/7/testinput.txt")][0]
    def test_get_effecient_fuel_count(self):
        count = fuel.getCheapestConvergence(self.testInput, True)
        self.assertEqual(count, 37, "Wrong Value")

    def test_get_inefficient_fuel_count(self):
        count = fuel.getCheapestConvergence(self.testInput)
        self.assertEqual(count, 168, "Wrong Value")