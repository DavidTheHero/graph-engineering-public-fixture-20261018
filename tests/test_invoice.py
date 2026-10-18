import unittest

from invoice import discounted_total


class DiscountTests(unittest.TestCase):
    def test_percentage_discount_is_applied_to_subtotal(self):
        self.assertEqual(discounted_total(20000, 10), 18000)

    def test_zero_discount_keeps_subtotal(self):
        self.assertEqual(discounted_total(2500, 0), 2500)

    def test_invalid_percentage_is_rejected(self):
        with self.assertRaises(ValueError):
            discounted_total(20000, 101)


if __name__ == "__main__":
    unittest.main()
