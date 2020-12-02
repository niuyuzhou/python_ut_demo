import unittest

from divisible import divisible_3

class TestDivisible3(unittest.TestCase):
    def test_divisible_check(self):
        """
        Test that it can check divisible by 3
        """
        result = divisible_3(0)
        self.assertEqual(result, "aunty")
        result = divisible_3(3)
        self.assertEqual(result, "aunty")
        result = divisible_3(4)
        self.assertEqual(result, "uncle")
    def test_bad_type(self):
        """
        Test that it can handle the execption
        """
        data = "abc"
        with self.assertRaises(TypeError):
            result = divisible_3(data)

if __name__ == '__main__':
    unittest.main()
