"""
Unit test
"""

import compute

class TestCalculator:

    def test_addition(self):
        assert 4 == compute.add(2, 2)

    def test_subtraction(self):
        assert 2 == compute.subtract(4, 2)
    
    def test_multiplication(self):
        assert 6 == compute.multiply(2, 3)