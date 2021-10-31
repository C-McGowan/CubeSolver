from CubeRepresentation import ALL_MOVES, SOLVED_STATE
from collections import deque
import numpy as np


class State:
    def __init__(self, permutation=SOLVED_STATE, path=None):
        self.permutation = permutation
        self.path = path
        if self.path is None:
            self.path = []

    def do_move(self, move):
        permutation = np.array(self.permutation)
        return permutation[ALL_MOVES[move]].tolist()

    def get_next_state(self, move):
        next_permutation = self.do_move(move)
        next_path = self.path + [move]
        return State(next_permutation, next_path)

    def all_next_states(self):
        return [self.get_next_state(move) for move in ALL_MOVES]

    def hash_state(self):
        return tuple(self.permutation)


def breadth_first_search(start_state):
    queue = deque([start_state])
    visited_states = {}
    while queue:
        current_state = queue.popleft()
        if current_state.hash_state() in visited_states:
            continue
        if current_state.permutation == SOLVED_STATE:
            return current_state.path
        visited_states[current_state.hash_state()] = current_state.path
        for next_state in current_state.all_next_states():
            queue.append(next_state)

    raise ValueError("Started from illegal state.")
