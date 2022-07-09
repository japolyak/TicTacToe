from random import randrange


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


game_field = [["-", "-", "-", "-", "-", "-", "-", "-", "-"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
              ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]


print_field(game_field)

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

    if game_field[x_move][y_move * 2] == "X" or game_field[x_move][y_move * 2] == "O":
        print("This cell is occupied! Choose another one!")
        continue

    game_field[x_move][y_move * 2] = "X"
    print_field(game_field)

    print("Making move level \"easy\"")
    x_coor = randrange(1, 4)
    y_coor = randrange(1, 4)

    while x_coor == x_move and y_coor == y_move:
        x_coor = randrange(1, 4)
        y_coor = randrange(1, 4)

    game_field[x_coor][y_coor * 2] = "O"
    print_field(game_field)

    for i in range(1, 4):
        row = game_field[i]
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
        if game_field[1][i] == " " or game_field[2][i] == " " or game_field[3][i] == " ":
            victory = False
            pass
        else:
            if game_field[2] == game_field[4] == game_field[6] == "X":
                victory = True
                print("X wins")
                break
            elif game_field[2] == game_field[4] == game_field[6] == "O":
                victory = True
                print("O wins")
                break

    if victory is True:
        break

    if game_field[1][2] == game_field[2][4] == game_field[3][6] == "X" or game_field[1][6] == game_field[2][4] == game_field[3][2] == "X":
        print("X wins")
        break

    elif game_field[1][2] == game_field[2][4] == game_field[3][6] == "O" or game_field[1][6] == game_field[2][4] == game_field[3][2] == "O":
        print("O wins")
        break
