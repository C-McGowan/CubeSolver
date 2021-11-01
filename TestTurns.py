import unittest
from CubeRepresentation import SOLVED_PERMUTATION, Permutation
import numpy as np

# TODO: Parameterise tests
class TestTurns(unittest.TestCase):
    def test_r_turn(self):
        self.assertEqual(SOLVED_PERMUTATION.permutation_after_move("R"),
                         Permutation([0, 1, 0, 1, 1, 5, 1, 5, 2, 2, 2, 2, 0, 3, 0 , 3, 4, 4, 4, 4, 5, 3, 5, 3]))

    def test_r_prime_turn(self):
        self.assertEqual(SOLVED_PERMUTATION.permutation_after_move("R'"),
                         Permutation([0, 3, 0, 3, 1, 0, 1, 0, 2, 2, 2, 2, 5, 3, 5, 3, 4, 4, 4, 4, 5, 1, 5, 1]))

    def test_d_turn(self):
        self.assertEqual(SOLVED_PERMUTATION.permutation_after_move("D"),
                         Permutation([0, 0, 0, 0, 1, 1, 4, 4, 2, 2, 1, 1, 3, 3, 2, 2, 4, 4, 3, 3, 5, 5, 5, 5]))

    def test_d_prime_turn(self):
        self.assertEqual(SOLVED_PERMUTATION.permutation_after_move("D'"),
                         Permutation([0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 1, 5, 5, 5, 5]))

    def test_b_turn(self):
        self.assertEqual(SOLVED_PERMUTATION.permutation_after_move("B"),
                         Permutation([2, 2, 0, 0, 1, 1, 1, 1, 2, 5, 2, 5, 3, 3, 3, 3, 0, 4, 0, 4, 5, 5, 4, 4]))

    def test_b_prime_turn(self):
        self.assertEqual(SOLVED_PERMUTATION.permutation_after_move("B'"),
                         Permutation([4, 4, 0, 0, 1, 1, 1, 1, 2, 0, 2, 0, 3, 3, 3, 3, 5, 4, 5, 4, 5, 5, 2, 2]))

    def test_t_perm(self):
        t_permutation = SOLVED_PERMUTATION
        moves = ["R", "D", "R'", "D'", "R'", "B", "R", "R", "D'", "R'", "D'", "R", "D", "R'", "B'"]
        for move in moves:
            t_permutation = t_permutation.permutation_after_move(move)
        self.assertEqual(t_permutation,
                         Permutation([0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 1, 3, 3, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5]))


if __name__ == '__main__':
    unittest.main()
