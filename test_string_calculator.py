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

    def test_multiple_numbers_comma_separated(self):
        self.assertEqual(self.calc.add("1,2,3,4,5"), 15)

    def test_newline_as_delimiter(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_single_char_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2")
        self.assertEqual(str(context.exception), "negative numbers -2")

    def test_multiple_negative_numbers_message(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("-1,2,-3")
        self.assertEqual(str(context.exception), "negative numbers -1, -3")

if __name__=="__main__":
    unittest.main()



