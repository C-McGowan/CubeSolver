from CubeRepresentation import ALL_MOVES, SOLVED_PERMUTATION, move_opposites
from collections import deque


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


def breadth_first_search(start_state):
    if start_state.permutation == SOLVED_PERMUTATION:
        return []
    queue = deque([start_state])
    visited_states = {start_state.permutation: []}
    while queue:
        current_state = queue.popleft()
        for next_state in current_state.all_next_states():
            if next_state.permutation == SOLVED_PERMUTATION:
                return next_state.path
            if next_state.permutation not in visited_states:
                visited_states[next_state.permutation] = next_state.path
                queue.append(next_state)

    raise ValueError("Started from illegal state.")


def get_combined_path(search_path, solution_path):
    return search_path + [move_opposites[move] for move in solution_path[::-1]]


def bidirectional_breadth_first_search(start_state):
    """Perform breadth first search forwards from starting scramble and backwards from solution,
    joining the paths when the same permutation is reached from both sides."""
    search_queue = deque([start_state])
    solution_queue = deque([State(SOLVED_PERMUTATION)])
    visited_search_states = {}
    visited_solution_states = {}

    while search_queue and solution_queue:
        current_search_state = search_queue.popleft()
        if current_search_state.permutation in visited_solution_states:
            solution_path = visited_solution_states[current_search_state.permutation]
            return get_combined_path(current_search_state.path, solution_path)

        elif current_search_state.permutation not in visited_search_states:
            visited_search_states[current_search_state.permutation] = current_search_state.path
            for next_search_state in current_search_state.all_next_states():
                search_queue.append(next_search_state)

        current_solution_state = solution_queue.popleft()
        if current_solution_state.permutation in visited_search_states:
            search_path = visited_search_states[current_solution_state.permutation]
            return get_combined_path(search_path, current_solution_state.path)

        elif current_solution_state.permutation not in visited_solution_states:
            visited_solution_states[current_solution_state.permutation] = current_solution_state.path
            for next_solution_state in current_solution_state.all_next_states():
                solution_queue.append(next_solution_state)

    raise ValueError("Started from illegal state.")


