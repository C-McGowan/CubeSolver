from CubeRepresentation import SOLVED_PERMUTATION, Permutation, ALL_MOVES, COLOURS, COLOUR_VALUES
from BFSSolver import State, breadth_first_search
import random
import numpy as np

# TODO: Main function with verbose argument for solves
# TODO: Functionality: random scramble - happy with state?, input scrambled state, manually scramble, solve


def random_scramble(length=20):
    permutation = SOLVED_PERMUTATION
    for i in range(length):
        move = random.choice(list(ALL_MOVES.keys()))
        permutation = permutation.permutation_after_move(move)
    return permutation


def manual_scramble(permutation=SOLVED_PERMUTATION):
    print("Enter moves to scramble, or press q to quit\n"
          "Valid moves are: R, R', B, B', D or D'")

    while True:
        move = input("Enter move:").upper()
        if move == "Q":
            return permutation
        elif move not in ALL_MOVES:
            print("Invalid move\n"
                  "Please enter a valid move, or press q to exit\n"
                  "Valid moves are: R, R', B, B', D or D'")
            continue
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
    print("Valid colours: 'white', 'green', 'red', 'blue', 'orange', 'yellow'")
    i = 0
    while i < 24:
        print()
        print(colour_net)
        if i in [2, 4, 17]:
            i += 1
            continue
        inputted_piece = input(f'Please enter the colour at position {i}: ')
        if inputted_piece not in COLOURS.values():
            print("Colour error, valid colours are: 'white', 'green', 'red', 'blue', 'orange', 'yellow'")
            continue
        input_permutation[i] = inputted_piece.center(6)
        colour_net = net.format(*input_permutation, spaces=" " * leading_space)
        i += 1
    print(colour_net)
    # Correct check
    return Permutation([COLOUR_VALUES[colour.strip()] for colour in input_permutation])


def solve_cube(permutation):
    return breadth_first_search(State(permutation))


def main():
    permutation = SOLVED_PERMUTATION
    while True:
        print("Enter action:\n"
              "1. Print current cube state\n"
              "2. Manually scramble cube\n"
              "3. Randomly scramble cube\n"
              "4. Enter cube state\n"
              "5. Print cube solution\n"
              "6. Reset cube\n"
              "7. Exit")
        action = input().strip()
        if action == "1":
            print(permutation)
        elif action == "2":
            permutation = manual_scramble(permutation)
        elif action == "3":
            permutation = random_scramble()
        elif action == "4":
            permutation = input_scramble()
        elif action == "5":
            print(solve_cube(permutation))
        elif action == "6":
            permutation = SOLVED_PERMUTATION
        elif action == "7":
            break
        else:
            print("Invalid action.")


main()
