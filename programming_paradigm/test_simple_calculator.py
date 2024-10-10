import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertNotEqual(self.calc.add(10,5), 7)

        

    def test_subtraction(self):
        """Test the subtract method"""
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertNotEqual(self.calc.add(10,5), 6)

    def test_multiply(self):
        """Test the multiply method"""
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(1,0), 0)
        self.assertEqual(self.calc.multiply('a',5), 'aaaaa')
    
    def test_divide(self):
        """Test the divide method"""

        #normal division
        self.assertEqual(self.calc.divide(4,2), 2)
        self.assertIsInstance(self.calc.divide(4,4), float)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertNotEqual(self.calc.divide(0,5), 5)

        #zero division
        self.assertEqual(self.calc.divide(2,0), None)
        self.assertEqual(self.calc.divide(0,2), 0)




# Remember to write additional test methods for subtract, multiply, and divide.
