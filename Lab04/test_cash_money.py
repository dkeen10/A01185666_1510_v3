from unittest import TestCase
from lab04 import cash_money


class TestCashMoney(TestCase):
    def test_cash_money(self):
        self.assertEqual([2, 1, 0, 1, 0, 1, 1, 1, 0, 1, 2], cash_money(263.33))
