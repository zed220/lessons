import unittest
from unittest.mock import patch
import Main

class Testing(unittest.TestCase):


    def test_input_2_values(self):
        user_input = [ 55, 44 ]
        with patch('builtins.input', side_effect=user_input):
            Main.Main()
        self.assertEqual(stacks, expected_stacks)
        
        pass


if __name__ == '__main__':
    unittest.main()