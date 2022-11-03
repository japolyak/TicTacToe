from random import randrange
import numpy as np


class GameState:
    def __init__(self):
        self.game_field = [[" ", " ", " "],
                           [" ", " ", " "],
                           [" ", " ", " "]]

        self.move_count = 0

    def print_field(self):
        print(9 * '-')

        for i in range(3):
            cell = self.game_field[i]
            print('|', cell[0], cell[1], cell[2], '|', sep=' ')

        print(9 * '-')

    def move_maker(self, x, y):
        if self.move_count % 2 == 1:
            move = "O"
        else:
            move = "X"

        self.game_field[x][y] = move
        self.print_field()

    def user_move(self):
        while True:
            coords = input("Enter the coordinates: ")

            try:
                x = int(coords[0])
                y = int(coords[2])
            except ValueError:
                print("You should enter numbers!")
                continue

            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue

            x -= 1
            y -= 1

            if self.game_field[x][y] != " ":
                print("This cell is occupied! Choose another one!")
                continue

            self.move_maker(x, y)
            break

    def easy_move(self):  # computers move on easy level

        print("Making easy move")
        x = randrange(0, 3)
        y = randrange(0, 3)

        while self.game_field[x][y] != " ":
            x = randrange(0, 3)
            y = randrange(0, 3)

        self.move_maker(x, y)

    def medium_move(self):  # medium computer move

        if self.move_count >= 3:
            x, y = 0, 0

            for i in range(3):  # vertical move
                x_in_row = 0
                o_in_row = 0
                w_s = 0

                for j in range(3):
                    if self.game_field[j][i] == " ":
                        w_s += 1
                        x = j
                        y = i
                    elif self.game_field[j][i] == "X":
                        x_in_row += 1
                    elif self.game_field[j][i] == "O":
                        o_in_row += 1

                if w_s == 1 and (o_in_row == 2 or x_in_row == 2):
                    print("Making medium move")
                    self.move_maker(x, y)
                    return

            trans_field = np.transpose(self.game_field)

            for i in range(3):  # horizontal move
                x_in_row = 0
                o_in_row = 0
                w_s = 0

                for j in range(3):
                    if trans_field[j][i] == " ":
                        w_s += 1
                        x = j
                        y = i
                    elif trans_field[j][i] == "X":
                        x_in_row += 1
                    elif trans_field[j][i] == "O":
                        o_in_row += 1

                if w_s == 1 and (o_in_row == 2 or x_in_row == 2):
                    print("Making medium move")
                    self.move_maker(y, x)
                    return

            while True:  # diagonal move
                x_in_row = 0
                o_in_row = 0
                w_s = 0
                for i in range(3):

                    if self.game_field[i][i] == " ":
                        w_s += 1
                        x = i
                        y = i
                    elif self.game_field[i][i] == "X":
                        x_in_row += 1
                    elif self.game_field[i][i] == "O":
                        o_in_row += 1

                if w_s == 1 and (o_in_row == 2 or x_in_row == 2):
                    print("Making medium move")
                    self.move_maker(x, y)
                    return

                x_in_row = 0
                o_in_row = 0
                w_s = 0

                for i in range(3):

                    if self.game_field[i][2 - i] == " ":
                        w_s += 1
                        x = i
                        y = 2 - i
                    elif self.game_field[i][2 - i] == "X":
                        x_in_row += 1
                    elif self.game_field[i][2 - i] == "O":
                        o_in_row += 1

                if w_s == 1 and (o_in_row == 2 or x_in_row == 2):
                    print("Making medium move")
                    self.move_maker(x, y)
                    return
                break

        x = randrange(0, 3)
        y = randrange(0, 3)

        while self.game_field[x][y] != " ":
            x = randrange(0, 3)
            y = randrange(0, 3)

        print("Making medium move")
        self.move_maker(x, y)

    def hard_move(self):

        s_board = self.game_field
        u_board = []

        for i in s_board:
            for j in i:
                u_board.append(j)

        for i, j in enumerate(u_board):
            if j == " ":
                u_board[i] = i

        hu_move = "O"
        ai_move = "X"

        def empty_indexes(board):
            return [k for k in board if k != "X" and k != "O"]

        def rules(cell, player):
            if ((cell[0] == cell[1] == cell[2] == player) or (cell[3] == cell[4] == cell[5] == player) or
                    (cell[6] == cell[7] == cell[8] == player) or (cell[0] == cell[3] == cell[6] == player) or
                    (cell[1] == cell[4] == cell[7] == player) or (cell[2] == cell[5] == cell[8] == player) or
                    (cell[0] == cell[4] == cell[8] == player) or (cell[2] == cell[4] == cell[6] == player)):

                return True
            else:
                return False

        def minimax(new_board, player):
            free_spots = empty_indexes(new_board)

            if rules(new_board, hu_move):
                return {"score": -10}
            elif rules(new_board, ai_move):
                return {"score": 10}
            elif not free_spots:
                return {"score": 0}

            moves = []

            for i, j in enumerate(free_spots):
                move = {"index": j}

                new_board[j] = player

                if player == ai_move:
                    result = minimax(new_board, hu_move)
                    move["score"] = result["score"]
                else:
                    result = minimax(new_board, ai_move)
                    move["score"] = result["score"]

                new_board[j] = j

                moves.append(move)

            best_move = 0
            if player == ai_move:
                best_score = -10000
                for i in range(0, len(moves)):
                    if moves[i]["score"] > best_score:
                        best_score = moves[i]["score"]
                        best_move = i

            else:
                best_score = 10000
                for i in range(0, len(moves)):
                    if moves[i]["score"] < best_score:
                        best_score = moves[i]["score"]
                        best_move = i

            return moves[best_move]

        player_move = "X"
        if self.move_count % 2 == 1:
            player_move = "O"

        move = minimax(u_board, player_move)["index"]

        x = move // 3
        y = move - 3 * x

        print("Making hard move")
        self.move_maker(x, y)

    move_handlers = {
        'user': user_move,
        'easy': easy_move,
        'medium': medium_move,
        'hard': hard_move,
    }


def victory_rules(state):

    while True:

        for i in range(0, 3):  # horizontal check
            row = state.game_field[i]

            if " " in row:
                pass
            else:
                if row[0] == row[1] == row[2] == "X":
                    print("X wins")
                    return True

                elif row[0] == row[1] == row[2] == "O":
                    print("O wins")
                    return True

        trans_field = np.transpose(state.game_field)

        for i in range(0, 3):  # vertical check
            row = trans_field[i]
            if " " in row:
                pass
            else:
                if row[0] == row[1] == row[2] == "X":
                    print("X wins")
                    return True

                elif row[0] == row[1] == row[2] == "O":
                    print("O wins")
                    return True

        if state.game_field[0][0] == state.game_field[1][1] == state.game_field[2][2] != " " or \
                state.game_field[0][2] == state.game_field[1][1] == state.game_field[2][0] != " ":  # diagonal check
            print(f"{state.game_field[1][1]} wins")
            return True

        break


def run_game():

    game_state = GameState()
    game_state.print_field()

    player1_move = game_state.move_handlers[params[1]]
    player2_move = game_state.move_handlers[params[2]]

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


if __name__ == '__main__':
    while True:
        params = input("Input command: ").split()

        if params[0] == "exit":
            break

        elif len(params) != 3:
            print("Bad parameters!")
            continue

        run_game()
