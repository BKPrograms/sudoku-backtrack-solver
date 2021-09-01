import math
import generator


def find_blank_list(board):
    blanks = []

    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == 0:
                blanks.append((i, j))

    return blanks


def is_n_possible_at_i_j(board, i, j, n):
    if n in board[i][:j] or n in board[i][j + 1:]:
        return False

    for i2, row in enumerate(board):

        if row[j] == n and i2 != i:
            return False

    x_dims = int(math.sqrt(len(board[0])))
    y_dims = int(math.sqrt(len(board)))

    x = (i // x_dims) * x_dims
    y = (j // y_dims) * y_dims
    for i3 in range(0, x_dims):
        for j3 in range(0, y_dims):

            if board[x + i3][y + j3] == n:
                return False

    return True


def solve(blanks, sboard):
    if not blanks:
        for row in sboard:
            print(row)

        print()
    else:
        curr_blank = blanks[0]
        possibles = []
        for n in range(1, len(sboard) + 1):
            if is_n_possible_at_i_j(sboard, curr_blank[0], curr_blank[1], n):
                possibles.append(n)

        for num in possibles:
            sboard[curr_blank[0]][curr_blank[1]] = num
            solve(blanks[1:], sboard)
            sboard[curr_blank[0]][curr_blank[1]] = 0  # Reset for next iteration


game = generator.give_board(2)

for row in game:
    print(row)

print('=' * 20)
print("Solutions:")
solve(find_blank_list(game), game)
