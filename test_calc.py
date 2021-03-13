"""
Unit testing the calculator app
"""

import calc


class TestCalc:

    def test_add(self):
        assert 5 == calc.add(1, 4)

    def test_subtract(self):
        assert 2 == calc.sub(5, 3)
