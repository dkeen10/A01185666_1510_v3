from unittest import TestCase
from lab04 import cash_money


class TestCashMoney(TestCase):
    def test_cash_money_lower_bound(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], cash_money(0))

    def test_cash_money_one_cent(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], cash_money(0.01))

    def test_cash_money_two_cents(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], cash_money(0.02))

    def test_cash_money_five_cents(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], cash_money(0.05))

    def test_cash_money_ten_cents(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], cash_money(0.1))

    def test_cash_money_twenty_five_cents(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], cash_money(0.25))

    def test_cash_money_one_dollar(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], cash_money(1))

    def test_cash_money_one_dollar_and_five_cents(self):
        self.assertEqual([0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], cash_money(1.05))

    def test_cash_money_two_dollars(self):
        self.assertEqual([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], cash_money(2))

    def test_cash_money_five_dollars(self):
        self.assertEqual([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], cash_money(5))

    def test_cash_money_ten_dollars(self):
        self.assertEqual([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], cash_money(10))

    def test_cash_money_ten_dollars_and_thirty_seven_cents(self):
        """error"""
        self.assertEqual([0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2], cash_money(10.27))

    def test_cash_money_twenty_dollars(self):
        self.assertEqual([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], cash_money(20))

    def test_cash_money_fifty_dollars(self):
        self.assertEqual([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], cash_money(50))

    def test_cash_money_one_hundred_dollars(self):
        self.assertEqual([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], cash_money(100))

    def test_cash_money_one_hundred_dollars_and_fifty_seven_cents(self):
        """error"""
        self.assertEqual([1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2], cash_money(100.57))

    def test_cash_money_one_hundred_eighty_seven_dollars_and_forty_one_cents(self):
        """error"""
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], cash_money(188.41))
