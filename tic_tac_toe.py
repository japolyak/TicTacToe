cells = input("Enter the cells: ")


def x_or_o(inp):
    x_list_o = []
    for e in inp:
        if e == "X":
            x_list_o.append(e)
        elif e == "O":
            x_list_o.append(e)
        else:
            x_list_o.append(" ")
    return x_list_o


def start_matrix(a):
    game_field = [["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                  ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
                  ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
                  ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
                  ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]

    n = 0
    xo = x_or_o(a)

    for it in range(1, 4):
        for e in range(2, 7, 2):
            game_field[it][e] = xo[n]
            n += 1
    return game_field


def print_field(nest_list):
    for k in range(0, 9):
        print(nest_list[0][k], end='')
    print()

    for e in range(1, 4):
        for k in range(0, 9):
            print(nest_list[e][k], sep='', end='')
        print()

    for k in range(0, 9):
        print(nest_list[4][k], end='')
    print()


start_field = start_matrix(cells)
print_field(start_field)

while True:
    coor = input("Enter the coordinates: ")

    try:
        first = int(coor[0])
        second = int(coor[2])
    except ValueError:
        print("You should enter numbers!")
        continue

    if first < 1 or second < 1:
        print("Coordinates should be from 1 to 3!")
        continue
    elif first > 3 or second > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    if start_field[first][second * 2] == "X" or start_field[first][second * 2] == "O":
        print("This cell is occupied! Choose another one!")
        continue

    x_count = 0
    o_count = 0

    for i in range(1, 4):
        for j in range(2, 7, 2):

            if start_field[i][j] == "X":
                x_count += 1

            elif start_field[i][j] == "O":
                o_count += 1

    if x_count > o_count:
        start_field[first][second * 2] = "O"
    else:
        start_field[first][second * 2] = "X"

    print_field(start_field)

    rule = True

    for i in range(1, 4):
        row = start_field[i]
        diag = start_field

        if diag[1][2] == diag[2][4] == diag[3][6] == "X" or diag[1][6] == diag[2][4] == diag[3][2] == "X":
            print("X wins")
            rule = False
            break

        elif diag[1][2] == diag[2][4] == diag[3][6] == "O" or diag[1][6] == diag[2][4] == diag[3][2] == "O":
            print("O wins")
            rule = False
            break

        elif row[2] == row[4] == row[6] == "X":
            print("X wins")
            rule = False
            break

        elif row[2] == row[4] == row[6] == "O":
            print("O wins")
            rule = False
            break

    if rule:
        for i in range(1, 4):
            row = start_field[i]

            for j in range(2, 7, 2):
                if row[j] == " ":
                    print("Game not finished")
                    rule = False
                    break

        if rule:
            print("Draw")
            break

    break

# dev branch
