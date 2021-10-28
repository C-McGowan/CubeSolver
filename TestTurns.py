import unittest
import numpy as np
from CubeRepresentation import do_move


class TestTurns(unittest.TestCase):
    def test_r_turn(self):
        solved_state = np.array([i//4 for i in range(24)])
        self.assertEqual(do_move(solved_state, "R").tolist(), [0, 1, 0, 1, 1, 5, 1, 5, 2, 2, 2, 2, 0, 3, 0 , 3, 4, 4, 4, 4, 5, 3, 5, 3])

    def test_r_prime_turn(self):
        solved_state = np.array([i//4 for i in range(24)])
        self.assertEqual(do_move(solved_state, "R'").tolist(), [0, 3, 0, 3, 1, 0, 1, 0, 2, 2, 2, 2, 5, 3, 5, 3, 4, 4, 4, 4, 5, 1, 5, 1])

    def test_d_turn(self):
        solved_state = np.array([i//4 for i in range(24)])
        self.assertEqual(do_move(solved_state, "D").tolist(), [0, 0, 0, 0, 1, 1, 4, 4, 2, 2, 1, 1, 3, 3, 2, 2, 4, 4, 3, 3, 5, 5, 5, 5])

    def test_d_prime_turn(self):
        solved_state = np.array([i // 4 for i in range(24)])
        self.assertEqual(do_move(solved_state, "D'").tolist(), [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 1, 5, 5, 5, 5])

    def test_b_turn(self):
        solved_state = np.array([i // 4 for i in range(24)])
        self.assertEqual(do_move(solved_state, "B").tolist(), [2, 2, 0, 0, 1, 1, 1, 1, 2, 5, 2, 5, 3, 3, 3, 3, 0, 4, 0, 4, 5, 5, 4, 4])

    def test_b_prime_turn(self):
        solved_state = np.array([i // 4 for i in range(24)])
        self.assertEqual(do_move(solved_state, "B'").tolist(), [4, 4, 0, 0, 1, 1, 1, 1, 2, 0, 2, 0, 3, 3, 3, 3, 5, 4, 5, 4, 5, 5, 2, 2])

    def test_t_perm(self):
        initial_state = np.array([i // 4 for i in range(24)])
        moves = ["R", "D", "R'", "D'", "R'", "B", "R", "R", "D'", "R'", "D'", "R", "D", "R'", "B'"]
        for move in moves:
            initial_state = do_move(initial_state, move)
        self.assertEqual(initial_state.tolist(), [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 1, 3, 3, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5])


if __name__ == '__main__':
    unittest.main()
