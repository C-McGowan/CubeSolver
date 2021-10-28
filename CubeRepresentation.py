import numpy as np


def print_cube(state):
    print(f'    |{state[0]}|{state[1]}|')
    print(f'    |{state[2]}|{state[3]}|')
    print(f'|{state[16]}|{state[17]}|{state[4]}|{state[5]}|{state[8]}|{state[9]}|{state[12]}|{state[13]}|')
    print(f'|{state[18]}|{state[19]}|{state[6]}|{state[7]}|{state[10]}|{state[11]}|{state[14]}|{state[15]}|')
    print(f'    |{state[20]}|{state[21]}|')
    print(f'    |{state[22]}|{state[23]}|')


def print_word_cube(state):
    print(f'              |{colour_dict[state[0]]}|{colour_dict[state[1]]}|')
    print(f'              |{colour_dict[state[2]]}|{colour_dict[state[3]]}|')
    print(f'|{colour_dict[state[16]]}|{colour_dict[state[17]]}|{colour_dict[state[4]]}|{colour_dict[state[5]]}|{colour_dict[state[8]]}|{colour_dict[state[9]]}|{colour_dict[state[12]]}|{colour_dict[state[13]]}|')
    print(f'|{colour_dict[state[18]]}|{colour_dict[state[19]]}|{colour_dict[state[6]]}|{colour_dict[state[7]]}|{colour_dict[state[10]]}|{colour_dict[state[11]]}|{colour_dict[state[14]]}|{colour_dict[state[15]]}|')
    print(f'              |{colour_dict[state[20]]}|{colour_dict[state[21]]}|')
    print(f'              |{colour_dict[state[22]]}|{colour_dict[state[23]]}|')


piece_dict = {
    "wgo": [2, 4, 17],
    "wbo": [0, 13, 16],
    "wrb": [1, 9, 12],
    "wgr": [3, 5, 8],
    "ygo": [20, 6, 19],
    "ygr": [21, 7, 10],
    "ybo": [22, 15, 18],
    "yrb": [23, 11, 14]
}

colour_dict = {
    0: "white ",
    1: "green ",
    2: " red  ",
    3: " blue ",
    4: "orange",
    5: "yellow"
}

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

solved_state = np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])

move_dict = {
    "R": np.array([0, 5, 2, 7, 4, 21, 6, 23, 10, 8, 11, 9, 3, 13, 1, 15, 16, 17, 18, 19, 20, 14, 22, 12]),
    "R'": np.array([0, 14, 2, 12, 4, 1, 6, 3, 9, 11, 8, 10, 23, 13, 21, 15, 16, 17, 18, 19, 20, 5, 22, 7]),
    "D": np.array([0, 1, 2, 3, 4, 5, 18, 19, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 14, 15, 22, 20, 23, 21]),
    "D'": np.array([0, 1, 2, 3, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 18, 19, 16, 17, 6, 7, 21, 23, 20, 22]),
    "B": np.array([9, 11, 2, 3, 4, 5, 6, 7, 8, 23, 10, 22, 14, 12, 15, 13, 1, 17, 0, 19, 20, 21, 16, 18]),
    "B'": np.array([18, 16, 2, 3, 4, 5, 6, 7, 8, 0, 10, 1, 13, 15, 12, 14, 22, 17, 23, 19, 20, 21, 11, 9]),
}


def do_move(state, move):
    return state[move_dict[move]]


def multiple_moves(state, moves):
    for move in moves:
        state = do_move(state, move)
    return state


solved_state = np.array([i//4 for i in range(24)])

