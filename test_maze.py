import a2
from a2 import *
import unittest

class TestMaze(unittest.TestCase):
    """docstring for TestMaze"""
    
    def setUp(self):
        """docstring for setUp"""
        self.maze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']], 
      Rat('J', 1, 1),
      Rat('P', 1, 4))
      
    def test_is_wall(self):
        """docstring for test_is_wall"""
        self.assertTrue(self.maze.is_wall(0, 0))
        self.assertFalse(self.maze.is_wall(1, 2))
        
    def test_get_character(self):
        """docstring for test_get_character"""
        expected = '#'
        actual = self.maze.get_character(0, 0)
        self.assertEquals(expected, actual)

        expected = '.'
        actual = self.maze.get_character(2, 1)
        self.assertEquals(expected, actual)
        
        expected = '@'
        actual = self.maze.get_character(3, 3)
        self.assertEquals(expected, actual)
    
    def test_get_character__with_rat_should_return_rat(self):
        """docstring for test_get_character__with_rat_should_return_rat"""
        expected = 'J'
        actual = self.maze.get_character(1, 1)
        self.assertEquals(expected, actual)
        
    def test_move_into_a_hall(self):
        """docstring for test_move_into_a_hall"""
        expected_success = True
        actual_success = self.maze.move(self.maze.rat_1, DOWN, NO_CHANGE)
        expected_row = 2
        expected_col = 1
        self.assertEquals(expected_success, actual_success)
        self.assertEquals(expected_row, self.maze.rat_1.row)
        self.assertEquals(expected_col, self.maze.rat_1.col)
        
    def test_move_into_wall(self):
        """docstring for test_move_into_wall"""
        expected_success = False
        actual_success = self.maze.move(self.maze.rat_1, NO_CHANGE, LEFT)
        expected_row = 1
        expected_col = 1
        self.assertEquals(expected_success, actual_success)
        self.assertEquals(expected_row, self.maze.rat_1.row)
        self.assertEquals(expected_col, self.maze.rat_1.col)
        
    def test_move_into_sprout(self):
        """docstring for test_move_into_sprout"""
        expected_success = True
        self.maze.move(self.maze.rat_1, DOWN, NO_CHANGE)
        self.maze.move(self.maze.rat_1, DOWN, NO_CHANGE)
        actual_success = self.maze.move(self.maze.rat_1, DOWN, NO_CHANGE)
        expected_row = 4
        expected_col = 1
        expected_num_sprouts_eaten = 1
        self.assertEquals(expected_success, actual_success)
        self.assertEquals(expected_row, self.maze.rat_1.row)
        self.assertEquals(expected_col, self.maze.rat_1.col)
        self.assertEquals(expected_num_sprouts_eaten, self.maze.rat_1.num_sprouts_eaten)
        self.assertEquals(HALL, self.maze.maze[expected_row][expected_col])
        self.assertEquals(2, self.maze.num_sprouts_left)
    
    def test_count_sprouts(self):
        """docstring for test_count_sprouts"""
        expected = 3
        actual = self.maze.count_sprouts()
        self.assertEquals(expected, actual)
        
    def test_str(self):
        """docstring for test_str"""
        expected = "#######\n"+"#J..P.#\n"+ "#.###.#\n"+ "#..@#.#\n"+ "#@#.@.#\n"+ "#######\n"+ "J at (1, 1) ate 0 sprouts.\n"+ "P at (1, 4) ate 0 sprouts."
        actual = self.maze.__str__()
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
        