import unittest
from string_calculator import StringCalculator

class Testcalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_comma_separated(self):
        self.assertEqual(self.calc.add("1,5"), 6)

if __name__=="__main__":
    unittest.main()



