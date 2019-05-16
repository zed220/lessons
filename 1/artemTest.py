import unittest
import artem


class Testing(unittest.TestCase):
    
    def test_artem1(self):
        self.assertEqual(10, artem.artem3(5, 5))


if __name__ == '__main__':
    unittest.main()