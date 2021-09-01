# randomize rows, columns and numbers (of valid base pattern)
from random import sample


# pattern for a baseline valid solution
def pattern(base, side, r, c): return (base * (r % base) + r // base + c) % side


def shuffle(s): return sample(s, len(s))


def give_board(base):
    side = base * base
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(base, side, r, c)] for c in cols] for r in rows]
    squares = side * side
    empties = squares * 30 // 100
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board
