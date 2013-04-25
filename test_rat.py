import a2
from a2 import *
import unittest


class TestRat(unittest.TestCase):
    """docstring for RatTest"""
    
    def setUp(self):
        """docstring for setUp"""
        self.rat = Rat('P', 1, 1)
    
    def test_set_location(self):
        """docstring for test_set_location
            location should accept two postive integers that are in the maze 
        """
        self.rat.set_location(2, 2)
        expected_row = 2
        expected_col = 2
        self.assertEquals(expected_row, self.rat.row)
        self.assertEquals(expected_col, self.rat.col)
        
    def test_eat_sprout(self):
        """docstring for test_eat_sprout
            eating a sprout should increase the number of num_sprouts_eaten
        """
        before = self.rat.num_sprouts_eaten
        self.rat.eat_sprout()
        after = self.rat.num_sprouts_eaten
        self.assertEquals(after, before + 1)
    
    def test_str(self):
        """docstring for test_str
            given the setUp is Rat('P', 1, 1)
            this test should return 'P at (1, 1) are 0 sprouts
            when initialized
        """
        expected = 'P at (1, 1) ate 0 sprouts.'
        actual = self.rat.__str__()
        self.assertEquals(expected, actual)
    
if __name__ == '__main__':
    unittest.main(exit=False)
        