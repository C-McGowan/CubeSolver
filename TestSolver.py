import unittest
import numpy as np
from CubeRepresentation import SOLVED_PERMUTATION, Permutation
from BFSSolver import breadth_first_search, State


# TODO: Parameterise tests
# TODO: Fix other tests
class TestSolver(unittest.TestCase):
    def test_start_state(self):
        self.assertEqual(breadth_first_search(State()), [])

    def test_one_turn(self):
        starting_permutation = SOLVED_PERMUTATION.permutation_after_move('R')
        starting_state = State(starting_permutation)
        self.assertEqual(breadth_first_search(starting_state), ["R'"])

    def test_two_turns(self):
        moves = ["R", "D"]
        starting_permutation = SOLVED_PERMUTATION
        for move in moves:
            starting_permutation = starting_permutation.permutation_after_move(move)
        starting_state = State(starting_permutation)
        self.assertEqual(breadth_first_search(starting_state), ["D'", "R'"])

    def test_maximum_scramble(self):
        moves = ["R'", "D", "B'", "R", "B'", "R'", "B", "B", "R", "D'", "B", "R", "D", "D"]
        starting_permutation = SOLVED_PERMUTATION
        for move in moves:
            starting_permutation = starting_permutation.permutation_after_move(move)
        starting_state = State(starting_permutation)
        self.assertEqual(len(breadth_first_search(starting_state)), 14)

    def test_scramble_error(self):
        invalid_permutation = Permutation(np.array([i for i in range(24)]))
        invalid_state = State(invalid_permutation)
        with self.assertRaises(ValueError):
            breadth_first_search(invalid_state)


if __name__ == '__main__':
    unittest.main()
