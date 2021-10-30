import numpy as np
from CubeRepresentation import do_move, move_dict, multiple_moves, print_word_cube
from collections import deque


def breadth_first_search(start_state):
    solved_state = [i // 4 for i in range(24)]
    queue = deque([[start_state, []]])
    visited_nodes = {}
    while queue:
        new_state, path = queue.popleft()
        if tuple(new_state) in visited_nodes:
            continue
        if new_state == solved_state:
            return path
        visited_nodes[tuple(new_state)] = path
        new_state = np.array(new_state)
        for move in move_dict:
            new_path = path + [move]
            queue.append([do_move(new_state, move).tolist(), new_path])
