from unittest import TestCase
from regular_expressions import is_poker


class Test(TestCase):
    def test_is_poker_full_house(self):
        test_hand = "aaakk"
        expected = True
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_pair(self):
        test_hand = "aakjt"
        expected = True
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_two_pair(self):
        test_hand = "aakk3"
        expected = True
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_three_of_a_kind(self):
        test_hand = "aaa34"
        expected = True
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_four_of_a_kind(self):
        test_hand = "aaaak"
        expected = True
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_straight(self):
        test_hand = "23456"
        expected = True
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_hand_too_small(self):
        test_hand = "2233"
        expected = False
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_hand_too_big(self):
        test_hand = "aa3344"
        expected = False
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_number_card_not_in_range(self):
        test_hand = "1aaaa"
        expected = False
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_face_card_not_in_range(self):
        test_hand = "f2222"
        expected = False
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_five_of_a_kind(self):
        test_hand = "aaaaa"
        expected = False
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)

    def test_is_poker_case_insenstivity(self):
        test_hand = "aAaA2"
        expected = True
        actual = is_poker(test_hand)
        self.assertEqual(expected, actual)
