from random import randrange


class GameState:
    game_field = [["-", "-", "-", "-", "-", "-", "-", "-", "-"], # change to the second emils version
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]


    # game_field = [
    #     ["", "", ""],
    #     ["", "", ""],
    #     ["", "", ""],
    # ]

    move_count = 0


while True:
    params = input("Input command: ").split()

    if params[0] == "exit":
        params = ['', '', '']
        break

    elif len(params) != 3:
        print("Bad parameters!")
        continue

    break


def print_field(state):  # printing gamefield
    for k in range(0, 9):
        print(state.game_field[0][k], end='')
    print()

    for e in range(1, 4):
        for k in range(0, 9):
            print(state.game_field[e][k], sep='', end='')
        print()

    for k in range(0, 9):
        print(state.game_field[4][k], end='')
    print()


def easy_move(state):  # computers move on easy level
    print("Making move level \"easy\"")
    x_coor = randrange(1, 4)
    y_coor = randrange(1, 4)

    while state.game_field[x_coor][y_coor * 2] == "X" or state.game_field[x_coor][y_coor * 2] == "O":
        x_coor = randrange(1, 4)
        y_coor = randrange(1, 4)

    if state.move_count % 2 == 1:
        state.game_field[x_coor][y_coor * 2] = "O"
        print_field(state)
    else:
        state.game_field[x_coor][y_coor * 2] = "X"
        print_field(state)


def user_move(state):
    while True:
        coor = input("Enter the coordinates: ")

        try:
            x_move = int(coor[0])
            y_move = int(coor[2])
        except ValueError:
            print("You should enter numbers!")
            continue

        if x_move < 1 or y_move < 1:
            print("Coordinates should be from 1 to 3!")
            continue
        elif x_move > 3 or y_move > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        if state.game_field[x_move][y_move * 2] == "X" or state.game_field[x_move][y_move * 2] == "O":
            print("This cell is occupied! Choose another one!")
            continue

        if state.move_count % 2 == 1:
            state.game_field[x_move][y_move * 2] = "O"
            print_field(state)
            break
        else:
            state.game_field[x_move][y_move * 2] = "X"
            print_field(state)
            break


def victory_rules(state): # bug with vertical rule
    victory = False
    while True:

        for i in range(1, 4):
            row = state.game_field[i]
            if row[2] == " " or row[4] == " " or row[6] == " ":
                victory = False
                pass
            else:
                if row[2] == row[4] == row[6] == "X":
                    victory = True
                    print("X wins")
                    break
                elif row[2] == row[4] == row[6] == "O":
                    victory = True
                    print("O wins")
                    break

        if victory is True:
            break

        for i in range(2, 7, 2):
            if state.game_field[1][i] == " " or state.game_field[2][i] == " " or state.game_field[3][i] == " ":
                victory = False
                pass
            else:
                if state.game_field[2] == state.game_field[4] == state.game_field[6] == "X":
                    victory = True
                    print("X wins")
                    break
                elif state.game_field[2] == state.game_field[4] == state.game_field[6] == "O":
                    victory = True
                    print("O wins")
                    break

        if victory is True:
            break

        if state.game_field[1][2] == state.game_field[2][4] == state.game_field[3][6] == "X" or \
                state.game_field[1][6] == state.game_field[2][4] == state.game_field[3][2] == "X":
            print("X wins")
            break

        elif state.game_field[1][2] == state.game_field[2][4] == state.game_field[3][6] == "O" or \
                state.game_field[1][6] == state.game_field[2][4] == state.game_field[3][2] == "O":
            print("O wins")
            break

        break

    return victory


move_handlers = {
    'user': user_move,
    'easy': easy_move,
}


def second_version():
    player1_move = move_handlers[params[1]]
    player2_move = move_handlers[params[2]]

    # null check?

    game_state = GameState()

    while game_state.move_count < 8:
        print(game_state.move_count)
        player1_move(game_state)
        game_state.move_count += 1

        if victory_rules(game_state):
            print("Someone won")
            return

        print(game_state.move_count)
        player2_move(game_state)
        game_state.move_count += 1

        if victory_rules(game_state):
            print("Someone won")
            return


second_version()
