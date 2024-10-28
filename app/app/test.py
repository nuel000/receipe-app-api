"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """
    Test the Calc Module
    """
    def test_add_numbers(self):
        """Adding numbers"""
        res = calc.add(5,6)
        self.assertEquals(res,11)
        
    def test_subtract_numbers(self):
        """Subtracting numbers"""
        res = calc.subtract(5,6)
        self.assertEquals(res,-1)

