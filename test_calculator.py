"""
Unit testing the calculator app
"""

import calculator


class TestCalc:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.sub(5, 3)

    def test_multiply(self):
        assert 2 == calculator.multiply(1, 2)

