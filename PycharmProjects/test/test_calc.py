import unittest
import calc


# https://docs.python.org/3/library/unittest.html?highlight=debug%20testcase#unittest.TestCase.debug
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)


if __name__ == "__main__":
    unittest.main()
