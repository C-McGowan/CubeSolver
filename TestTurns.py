import unittest
from CubeRepresentation import do_move, SOLVED_STATE

# TODO: Parameterise tests
class TestTurns(unittest.TestCase):
    def test_r_turn(self):
        self.assertEqual(do_move(SOLVED_STATE, "R"), [0, 1, 0, 1, 1, 5, 1, 5, 2, 2, 2, 2, 0, 3, 0 , 3, 4, 4, 4, 4, 5, 3, 5, 3])

    def test_r_prime_turn(self):
        self.assertEqual(do_move(SOLVED_STATE, "R'"), [0, 3, 0, 3, 1, 0, 1, 0, 2, 2, 2, 2, 5, 3, 5, 3, 4, 4, 4, 4, 5, 1, 5, 1])

    def test_d_turn(self):
        self.assertEqual(do_move(SOLVED_STATE, "D"), [0, 0, 0, 0, 1, 1, 4, 4, 2, 2, 1, 1, 3, 3, 2, 2, 4, 4, 3, 3, 5, 5, 5, 5])

    def test_d_prime_turn(self):
        self.assertEqual(do_move(SOLVED_STATE, "D'"), [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 1, 5, 5, 5, 5])

    def test_b_turn(self):
        self.assertEqual(do_move(SOLVED_STATE, "B"), [2, 2, 0, 0, 1, 1, 1, 1, 2, 5, 2, 5, 3, 3, 3, 3, 0, 4, 0, 4, 5, 5, 4, 4])

    def test_b_prime_turn(self):
        self.assertEqual(do_move(SOLVED_STATE, "B'"), [4, 4, 0, 0, 1, 1, 1, 1, 2, 0, 2, 0, 3, 3, 3, 3, 5, 4, 5, 4, 5, 5, 2, 2])

    def test_t_perm(self):
        initial_state = SOLVED_STATE
        moves = ["R", "D", "R'", "D'", "R'", "B", "R", "R", "D'", "R'", "D'", "R", "D", "R'", "B'"]
        for move in moves:
            initial_state = do_move(initial_state, move)
        self.assertEqual(initial_state, [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 1, 3, 3, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5])


if __name__ == '__main__':
    unittest.main()
