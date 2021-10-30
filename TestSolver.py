import unittest
import numpy as np
from CubeRepresentation import multiple_moves
from BFSSolver import breadth_first_search


class TestSolver(unittest.TestCase):
    def test_one_turn(self):
        solved_state = np.array([i//4 for i in range(24)])
        starting_state = multiple_moves(solved_state, ['R']).tolist()
        self.assertEqual(breadth_first_search(starting_state), ["R'"])

    def test_two_turns(self):
        solved_state = np.array([i//4 for i in range(24)])
        starting_state = multiple_moves(solved_state, ['R', "D'"]).tolist()
        self.assertEqual(breadth_first_search(starting_state), ["D", "R'"])


if __name__ == '__main__':
    unittest.main()