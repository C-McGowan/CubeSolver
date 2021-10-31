import numpy as np

# TODO: Main function with verbose argument for solves
# TODO: Functionality: random scramble - happy with state?, input scrambled state, manually scramble, solve
# TODO: Turn into class
# TODO: Override print with print_word_cube, remove print_cube

class Permutation:
    def __init__(self, permutation):
        self.permutation = permutation

    def permutation_after_move(self, move):
        return Permutation(self.permutation[ALL_MOVES[move]])

    def hash_state(self):
        return tuple(self.permutation)

    def __eq__(self, other):
        return np.array_equal(self.permutation, other.permutation)


SOLVED_STATE = Permutation(np.array([i // 4 for i in range(24)]))

COLOURS = {
    0: "white ",
    1: "green ",
    2: " red  ",
    3: " blue ",
    4: "orange",
    5: "yellow"
}

ALL_MOVES = {  # TODO: Turn into enum
    # R turn maps face 0 -> 0, 5 -> 1, 2-> 2 etc.
    "R": np.array([0, 5, 2, 7, 4, 21, 6, 23, 10, 8, 11, 9, 3, 13, 1, 15, 16, 17, 18, 19, 20, 14, 22, 12]),
    "R'": np.array([0, 14, 2, 12, 4, 1, 6, 3, 9, 11, 8, 10, 23, 13, 21, 15, 16, 17, 18, 19, 20, 5, 22, 7]),
    "D": np.array([0, 1, 2, 3, 4, 5, 18, 19, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 14, 15, 22, 20, 23, 21]),
    "D'": np.array([0, 1, 2, 3, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 16, 17, 6, 7, 21, 23, 20, 22]),
    "B": np.array([9, 11, 2, 3, 4, 5, 6, 7, 8, 23, 10, 22, 14, 12, 15, 13, 1, 17, 0, 19, 20, 21, 16, 18]),
    "B'": np.array([18, 16, 2, 3, 4, 5, 6, 7, 8, 0, 10, 1, 13, 15, 12, 14, 22, 17, 23, 19, 20, 21, 11, 9]),
}


def print_net(net_values):
    leading_space = len(f'|{net_values[0]}|{net_values[1]}')
    net = "{spaces}|{0}|{1}|\n" \
          "{spaces}|{2}|{3}|\n" \
          "|{16}|{17}|{4}|{5}|{8}|{9}|{12}|{13}|\n" \
          "|{18}|{19}|{6}|{7}|{10}|{11}|{14}|{15}|\n" \
          "{spaces}|{20}|{21}|\n" \
          "{spaces}|{22}|{23}|"
    return net.format(*net_values, spaces=" " * leading_space)


def print_cube(state):
    print(print_net(state))


def print_word_cube(state):
    word_state = [COLOURS[state[i]] for i in state]
    print(print_net(word_state))
