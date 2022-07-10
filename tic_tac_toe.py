from random import randrange

game_field = [["-", "-", "-", "-", "-", "-", "-", "-", "-"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]


while True:
    begin = input("Input command: ").split()

    if begin[0] == "exit":
        begin = ['', '', '']
        break

    elif len(begin) != 3:
        print("Bad parameters!")
        continue

    break


def print_field(field):  # printing gamefield
    for k in range(0, 9):
        print(field[0][k], end='')
    print()

    for e in range(1, 4):
        for k in range(0, 9):
            print(field[e][k], sep='', end='')
        print()

    for k in range(0, 9):
        print(field[4][k], end='')
    print()


def easy_move(field):  # computers move on easy level
    print("Making move level \"easy\"")
    x_coor = randrange(1, 4)
    y_coor = randrange(1, 4)

    global moves_count

    while field[x_coor][y_coor * 2] == "X" or field[x_coor][y_coor * 2] == "O":
        x_coor = randrange(1, 4)
        y_coor = randrange(1, 4)

    if moves_count % 2 == 1:
        field[x_coor][y_coor * 2] = "O"
        print_field(field)
        moves_count += 1
    else:
        field[x_coor][y_coor * 2] = "X"
        print_field(field)
        moves_count += 1


def first_user_move(field):
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

        if field[x_move][y_move * 2] == "X" or field[x_move][y_move * 2] == "O":
            print("This cell is occupied! Choose another one!")
            continue

        field[x_move][y_move * 2] = "X"
        break


def user_move(field):
    global moves_count
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

        if field[x_move][y_move * 2] == "X" or field[x_move][y_move * 2] == "O":
            print("This cell is occupied! Choose another one!")
            continue

        if moves_count % 2 == 1:
            field[x_move][y_move * 2] = "O"
            print_field(field)
            moves_count += 1
            break
        else:
            field[x_move][y_move * 2] = "X"
            print_field(field)
            moves_count += 1
            break


def easy_first_move(field):
    print_field(field)

    print("Making move level \"easy\"")
    first_x_move = randrange(1, 4)
    first_y_move = randrange(1, 4)
    field[first_x_move][first_y_move * 2] = "X"
    print_field(field)


def victory_rules(field):
    global victory
    while True:

        for i in range(1, 4):
            row = field[i]
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
            if field[1][i] == " " or field[2][i] == " " or field[3][i] == " ":
                victory = False
                pass
            else:
                if field[2] == field[4] == field[6] == "X":
                    victory = True
                    print("X wins")
                    break
                elif field[2] == field[4] == field[6] == "O":
                    victory = True
                    print("O wins")
                    break

        if victory is True:
            break

        if field[1][2] == field[2][4] == field[3][6] == "X" or \
                field[1][6] == field[2][4] == field[3][2] == "X":
            print("X wins")
            break

        elif field[1][2] == field[2][4] == field[3][6] == "O" or \
                field[1][6] == field[2][4] == field[3][2] == "O":
            print("O wins")
            break

        break


if begin[1] == "easy":

    if begin[2] == "easy":

        easy_first_move(game_field)
        moves_count = 1
        victory = False

        while moves_count < 9:
            easy_move(game_field)
            if moves_count >= 5:
                victory_rules(game_field)
                if victory is True:
                    break

    elif begin[2] == "user":

        easy_first_move(game_field)
        moves_count = 1
        victory = False

        while moves_count < 9:
            user_move(game_field)
            if moves_count >= 5:
                victory_rules(game_field)
                if victory is True:
                    break
            easy_move(game_field)
            if moves_count >= 5:
                victory_rules(game_field)
                if victory is True:
                    break

elif begin[1] == "user":

    if begin[2] == "easy":
        print_field(game_field)

        first_user_move(game_field)
        print_field(game_field)
        moves_count = 1
        victory = False

        while moves_count < 9:
            easy_move(game_field)
            if moves_count >= 5:
                victory_rules(game_field)
                if victory is True:
                    break
            user_move(game_field)
            if moves_count >= 5:
                victory_rules(game_field)
                if victory is True:
                    break

    elif begin[2] == "user":
        print_field(game_field)

        first_user_move(game_field)
        print_field(game_field)
        moves_count = 1
        victory = False

        while moves_count < 9:
            user_move(game_field)
            if moves_count >= 5:
                victory_rules(game_field)
                if victory is True:
                    break
