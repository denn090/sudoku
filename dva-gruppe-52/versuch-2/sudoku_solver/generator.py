# sudoku_generator.py

import random
import copy
import datetime
import uuid
import json

from solver import solve, count_solutions  # Import aus solver.py

def generate(difficulty_level):
    difficulty_names = {0: "easy", 1: "medium", 2: "hard", 3: "expert"}

    if difficulty_level not in difficulty_names:
        raise ValueError("Schwierigkeitsgrad muss zwischen 0 und 3 liegen.")

    difficulty_str = difficulty_names[difficulty_level]
    holes_map = {0: 35, 1: 45, 2: 55, 3: 60}
    holes = holes_map[difficulty_level]

    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)

    solution = copy.deepcopy(board)
    puzzle = copy.deepcopy(board)
    remove_cells(puzzle, holes)

    return {
        "id": str(uuid.uuid4()),
        "difficulty": difficulty_str,
        "board": puzzle,
        "solution": solution,
        "createdAt": datetime.datetime.utcnow().isoformat() + "Z"
    }

def fill_board(board):
    numbers = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_safe(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_safe(board, row, col, num):
    from solver import valid
    return valid(board, row, col, num)

def remove_cells(board, holes):
    attempts = holes + 10
    while holes > 0 and attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] == 0:
            continue

        backup = board[row][col]
        board[row][col] = 0

        test_board = copy.deepcopy(board)
        if count_solutions(test_board) == 1:
            holes -= 1
        else:
            board[row][col] = backup

        attempts -= 1
