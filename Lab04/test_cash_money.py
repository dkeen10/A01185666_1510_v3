from unittest import TestCase
from lab04 import cash_money


class TestCashMoney(TestCase):
    def test_cash_money(self):
        """Test cash_money function against a certain amount."""
        self.assertEqual([2, 1, 0, 1, 0, 1, 1, 1, 0, 1, 2], cash_money(263.33))

    def test_cash_money_lower_bound(self):
        """Test cash_money function against the lower bound."""
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], cash_money(0))
