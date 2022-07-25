from random import randrange
import numpy as np


class GameState:

    game_field = [[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]]

    move_count = 0

    medium_x = 0
    medium_y = 0


class VictoryRules:

    def __init__(self, field):
        self.field = field


while True:
    params = input("Input command: ").split()

    if params[0] == "exit":
        finish = False
        break

    elif len(params) != 3:
        print("Bad parameters!")
        continue

    finish = True

    break


def print_field(state):  # printing gamefield
    print(9 * '-')

    for i in range(0, 3):
        cell = state.game_field[i]
        print('|', cell[0], cell[1], cell[2], '|', sep=' ')

    print(9 * '-')


def easy_move(state):  # computers move on easy level

    if state.move_count % 2 == 1:
        move = "O"
    else:
        move = "X"

    print("Making move level \"easy\"")
    x = randrange(0, 3)
    y = randrange(0, 3)

    while state.game_field[x][y] == "X" or state.game_field[x][y] == "O":
        x = randrange(0, 3)
        y = randrange(0, 3)

    state.game_field[x][y] = move
    print_field(state)


def medium_move(state):  # medium computer move

    if state.move_count % 2 == 1:
        move = "O"
    else:
        move = "X"

    if state.move_count >= 3:
        for c_i, i in enumerate(state.game_field):  # horizontal move

            x_in_row = 0
            o_in_row = 0
            w_s = 0

            for c_j, j in enumerate(i):
                if j == ' ':
                    w_s += 1
                    x = c_i
                    y = c_j
                elif j == "X":
                    x_in_row += 1
                elif j == "O":
                    o_in_row += 1

            if (x_in_row == 2 and w_s == 1) or (o_in_row == 2 and w_s == 1):
                state.game_field[x][y] = move
                print_field(state)
                return

        for i in range(0, 3):  # vertical move
            x_in_row = 0
            o_in_row = 0
            w_s = 0

            for j in range(0, 3):
                if state.game_field[j][i] == " ":
                    w_s += 1
                    x = j
                    y = i
                elif state.game_field[j][i] == "X":
                    x_in_row += 1
                elif state.game_field[j][i] == "O":
                    o_in_row += 1

            if (x_in_row == 2 and w_s == 1) or (o_in_row == 2 and w_s == 1):
                state.game_field[x][y] = move
                print_field(state)
                return

        while True:
            x_in_row = 0
            o_in_row = 0
            w_s = 0
            for i in range(0, 3):

                if state.game_field[i][i] == " ":
                    w_s += 1
                    x = i
                    y = i
                elif state.game_field[i][i] == "X":
                    x_in_row += 1
                elif state.game_field[i][i] == "O":
                    o_in_row += 1

            if (x_in_row == 2 and w_s == 1) or (o_in_row == 2 and w_s == 1):
                state.game_field[x][y] = move
                print_field(state)
                return

            x_in_row = 0
            o_in_row = 0
            w_s = 0

            for i in range(0, 3):

                if state.game_field[i][2 - i] == " ":
                    w_s += 1
                    x = i
                    y = 2 - i
                elif state.game_field[i][2 - i] == "X":
                    x_in_row += 1
                elif state.game_field[i][2 - i] == "O":
                    o_in_row += 1

            if (x_in_row == 2 and w_s == 1) or (o_in_row == 2 and w_s == 1):
                state.game_field[x][y] = move
                print_field(state)
                return
            break

    print("Making move level \"medium\"")
    x = randrange(0, 3)
    y = randrange(0, 3)

    while state.game_field[x][y] == "X" or state.game_field[x][y] == "O":
        x = randrange(0, 3)
        y = randrange(0, 3)

    state.game_field[x][y] = move
    print_field(state)


def hard_move(state):
    print("Will be")


def user_move(state):
    while True:
        coor = input("Enter the coordinates: ")

        try:
            x = int(coor[0])
            y = int(coor[2])
        except ValueError:
            print("You should enter numbers!")
            continue

        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        x -= 1
        y -= 1

        if state.game_field[x][y] == "X" or state.game_field[x][y] == "O":
            print("This cell is occupied! Choose another one!")
            continue

        if state.move_count % 2 == 1:
            state.game_field[x][y] = "O"
            print_field(state)
            break
        else:
            state.game_field[x][y] = "X"
            print_field(state)
            break


def victory_rules(state):
    while True:

        for i in range(0, 3):  # horizontal check
            row = state.game_field[i]
            if row[0] == " " or row[1] == " " or row[2] == " ":
                pass
            else:
                if row[0] == row[1] == row[2] == "X":
                    print("X wins")
                    return True

                elif row[0] == row[1] == row[2] == "O":
                    print("O wins")
                    return True

        trans_field = np.transpose(state.game_field)

        for i in range(0, 3):  # vertial check
            row = trans_field[i]
            if row[0] == " " or row[1] == " " or row[2] == " ":
                pass
            else:
                if row[0] == row[1] == row[2] == "X":
                    print("X wins")
                    return True

                elif row[0] == row[1] == row[2] == "O":
                    print("O wins")
                    return True

        if state.game_field[0][0] == state.game_field[1][1] == state.game_field[2][2] == "X" or \
                state.game_field[0][2] == state.game_field[1][1] == state.game_field[2][0] == "X":  # diagonal check
            print("X wins")
            return True

        elif state.game_field[0][0] == state.game_field[1][1] == state.game_field[2][2] == "O" or \
                state.game_field[0][2] == state.game_field[1][1] == state.game_field[2][0] == "O":
            print("O wins")
            return True

        break


move_handlers = {
    'user': user_move,
    'easy': easy_move,
    'medium': medium_move,
    'hard': hard_move,
}


def second_version():
    player1_move = move_handlers[params[1]]
    player2_move = move_handlers[params[2]]

    game_state = GameState()

    print_field(game_state)

    while game_state.move_count < 9:
        player1_move(game_state)
        game_state.move_count += 1

        if victory_rules(game_state):
            return
        elif game_state.move_count == 9:
            print("Draw")
            return

        player2_move(game_state)
        game_state.move_count += 1

        if victory_rules(game_state):
            return

    return


if finish is True:
    second_version()
