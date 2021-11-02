from CubeRepresentation import SOLVED_PERMUTATION, Permutation, ALL_MOVES, COLOURS, COLOUR_VALUES
from BFSSolver import State, bidirectional_breadth_first_search
import random


def get_user_input(message, valid_responses, error_message, match_first_letter=False):
    valid_inputs = {response.upper(): response for response in valid_responses}
    if match_first_letter:
        valid_inputs.update({response[0].upper(): response for response in valid_responses})
    while True:
        user_input = input(message).strip().upper()
        try:
            return valid_inputs[user_input]
        except KeyError:
            print(error_message)


def stringify_moves(moves):
    return ", ".join(moves)


def random_scramble(length=20):
    permutation = SOLVED_PERMUTATION
    moves = [random.choice(list(ALL_MOVES.keys())) for i in range(length)]
    for move in moves:
        permutation = permutation.permutation_after_move(move)
    print("Scramble: " + stringify_moves(moves))
    print(permutation)
    input()
    return permutation


def manual_scramble(permutation=SOLVED_PERMUTATION):
    print("Enter moves to scramble, or press q to quit\n"
          "Valid moves are: R, R', B, B', D or D'")
    message = "Enter move: "
    error_message = """Invalid move
                    Please enter a valid move, or press q to exit
                    Valid moves are: R, R', B, B', D or D'"""
    valid_moves = list(ALL_MOVES.keys()) + ["Q"]
    while True:
        move = get_user_input(message, valid_moves, error_message)
        if move == "Q":
            print(permutation)
            break
        permutation = permutation.permutation_after_move(move)
    return permutation


def input_scramble():
    input_permutation = [str(i).center(6) for i in range(24)]
    input_permutation[2] = "white "
    input_permutation[4] = "green "
    input_permutation[17] = "orange"
    leading_space = len(f'|{input_permutation[0]}|{input_permutation[1]}')
    net = "{spaces}|{0}|{1}|\n" \
          "{spaces}|{2}|{3}|\n" \
          "|{16}|{17}|{4}|{5}|{8}|{9}|{12}|{13}|\n" \
          "|{18}|{19}|{6}|{7}|{10}|{11}|{14}|{15}|\n" \
          "{spaces}|{20}|{21}|\n" \
          "{spaces}|{22}|{23}|"
    colour_net = net.format(*input_permutation, spaces=" " * leading_space)
    print("Please orient the cube so that the white sticker of the white-green-orange piece is facing up, "
          "and the green piece if facing towards you.")
    print("Valid colours: (w)hite, (g)reen, (r)ed, (b)lue, (o)range, (y)ellow")
    for i in range(24):
        if i in [2, 4, 17]:
            continue

        inputted_piece = get_user_input(
            message=f'\n{colour_net}\n\nPlease enter the colour at position {i}: ',
            valid_responses=COLOURS.values(),
            error_message="Colour error, valid colours are: 'white', 'green', 'red', 'blue', 'orange', 'yellow'",
            match_first_letter=True
        )

        input_permutation[i] = inputted_piece.center(6)
        colour_net = net.format(*input_permutation, spaces=" " * leading_space)
    print(colour_net)
    return Permutation([COLOUR_VALUES[colour.strip()] for colour in input_permutation])


def solve_cube(permutation, solve_function=bidirectional_breadth_first_search):
    solution_path = solve_function(State(permutation))
    print("Solution: " + stringify_moves(solution_path))
    input()


def main():
    permutation = SOLVED_PERMUTATION
    while True:
        action = get_user_input(
            message="""Enter action:
    1. Print current cube state
    2. Manually scramble cube
    3. Randomly scramble cube
    4. Enter cube state
    5. Print cube solution
    6. Reset cube
    7. Exit
    """,
            valid_responses=[str(i) for i in range(1, 8)],
            error_message="Invalid action."
        )
        if action == "1":
            print(permutation)
        elif action == "2":
            permutation = manual_scramble(permutation)
        elif action == "3":
            permutation = random_scramble()
        elif action == "4":
            permutation = input_scramble()
        elif action == "5":
            solve_cube(permutation, bidirectional_breadth_first_search)
        elif action == "6":
            permutation = SOLVED_PERMUTATION
        elif action == "7":
            break


if __name__ == '__main__':
    main()
