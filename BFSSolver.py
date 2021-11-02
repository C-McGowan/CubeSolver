from CubeRepresentation import ALL_MOVES, SOLVED_PERMUTATION
from collections import deque

move_opposites = {
    "R": "R'",
    "R'": "R",
    "B": "B'",
    "B'": "B",
    "D": "D'",
    "D'": "D"
}


class State:
    def __init__(self, permutation=SOLVED_PERMUTATION, path=None):
        self.permutation = permutation
        self.path = path
        if self.path is None:
            self.path = []

    def get_next_state(self, move):
        next_permutation = self.permutation.permutation_after_move(move)
        next_path = self.path + [move]
        return State(next_permutation, next_path)

    def all_next_states(self):
        return [self.get_next_state(move) for move in ALL_MOVES]

    def hash_state(self):
        return self.permutation.hash_state()


def breadth_first_search(start_state):
    queue = deque([start_state])
    visited_states = {}
    while queue:
        current_state = queue.popleft()
        if current_state.hash_state() in visited_states:
            continue
        if current_state.permutation == SOLVED_PERMUTATION:
            return current_state.path
        visited_states[current_state.hash_state()] = current_state.path
        for next_state in current_state.all_next_states():
            queue.append(next_state)

    raise ValueError("Started from illegal state.")


def bidirectional_breadth_first_search(start_state):
    search_queue = deque([start_state])
    solution_queue = deque([State(SOLVED_PERMUTATION)])
    visited_search_states = {}
    visited_solution_states = {}
    while search_queue and solution_queue:
        current_search_state = search_queue.popleft()
        if current_search_state.hash_state() in visited_solution_states:
            search_path = current_search_state.path
            solution_path = visited_solution_states[current_search_state.hash_state()]
            inverted_solution_path = [move_opposites[move] for move in solution_path[::-1]]
            return search_path + inverted_solution_path

        elif current_search_state.hash_state() not in visited_search_states:
            visited_search_states[current_search_state.hash_state()] = current_search_state.path
            for next_search_state in current_search_state.all_next_states():
                search_queue.append(next_search_state)

        current_solution_state = solution_queue.popleft()
        if current_solution_state.hash_state() in visited_search_states:
            search_path = visited_search_states[current_solution_state.hash_state()]
            inverted_solution_path = [move_opposites[move] for move in current_solution_state.path[::-1]]
            return search_path + inverted_solution_path

        elif current_solution_state.hash_state() not in visited_solution_states:
            visited_solution_states[current_solution_state.hash_state()] = current_solution_state.path
            for next_solution_state in current_solution_state.all_next_states():
                solution_queue.append(next_solution_state)
    raise ValueError("Started from illegal state.")


