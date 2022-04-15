#!/usr/bin/env python3

import os
import sys


def cl_scr():
    """ cleans the terminal """
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")


def gen_board(rows: int, columns: int) -> list[list[str]]:
    """
    generate tic-tac-toe board each value = " . "
    :param rows: number of rows
    :param columns: number of columns
    :return: list of lists
    """
    board = []
    for line in range(rows):
        row = []
        for field in range(columns):
            row.append(" . ")
        board.append(row)
    return board


def gen_board_greeter(rows: int, columns: int) -> list[list[str]]:
    """
    generate tic-tac-toe board each value = " RC "; R=row, C=column
    :param rows: number of rows
    :param columns: number of columns
    :return: list of lists
    """
    board_greeter = []
    for line in range(rows):
        row = []
        for field in range(columns):
            row.append(" " + str(line + 1) + str(field + 1) + " ")
        board_greeter.append(row)
    return board_greeter


def greeter(board: list[list[str]], board_greeter: list[list[str]], sepa="=" * 49) -> None:
    """ welcomes in the game with the possible display of rules """
    cl_scr()
    print("", sepa, "Welcome to Tic Tac Toe".center(len(sepa)), sepa, sep="\n")
    rule = input("\n\n\"Enter\" to continue..., \"r\" to read game rules: ")
    if not rule == "":
        rules(board, board_greeter)
    cl_scr()


def rules(board: list[list[str]], board_greeter: list[list[str]], sepa="=" * 49) -> None:
    """ prints out game instruction """
    cl_scr()
    print("",
          sepa,
          "GAME RULES".center(len(sepa)),
          sepa,
          "Each player can place one mark / stone per turn",
          "in the 9x9 grid. The WINNER is who places",
          "5 marks / stones in any of those ways:",
          "* horizontal row",
          "* vertical row",
          "* diagonal row",
          sepa,
          sep="\n")
    input("\n\"Enter\" to continue...")

    cl_scr()
    print("\nYou will be shown the board and asked",
          "to choose the slot.\n", sep="\n")
    pr_board(board)
    print("Choose the slot where you want to drag: ")
    input("\n\"Enter\" to continue...")

    cl_scr()
    print("\nThe slot coordinates is combination of",
          "\"row number\" and \"column number\".",
          "All slot coordinates as follow.\n", sep="\n")
    pr_board(board_greeter, "  ")
    input("\n\"Enter\" to continue...")

    cl_scr()
    print("", sepa, "REMEMBER".center(len(sepa)), sepa, sep="\n")
    print("",
          "At any time during the game, when entering",
          "data from the keyboard, you can immediately end",
          "the game by entering \"q\".", sep="\n")
    input("\n\"Enter\" to continue...")

    cl_scr()
    print("", sepa, "Let's start the game.".center(len(sepa)), sepa, sep="\n")
    input("\n\"Enter\" to continue...")
    cl_scr()


def pr_board(board: list[list[str]], gret: str = " ") -> None:
    """ prints out game board """
    print("\n ", end="")
    for i in range(1, len(board) + 1):
        print(gret, i, end="")
    print()

    for ind_r, row in enumerate(board):
        print(ind_r + 1, "", end="")
        for ind_c, slot in enumerate(row):
            print(slot, end="")
        print(end="\n")
    print()


def end(user_input: str, sepa="=" * 49) -> bool:
    """ checks the quit request if so, prints out thanks note """
    if user_input.lower() == "q":
        cl_scr()
        print("", sepa, "Thank you for the game.".center(len(sepa)), sepa, "",  sep="\n")
        return True


def is_number(num: str) -> bool:
    """ checks if the player's turn is integer """
    try:
        int(num)
        cl_scr()
        return True
    except ValueError:
        cl_scr()
        print("\nThis is not a valid number")
        return False


def in_bounds(user_input: str) -> bool:
    """ checks if the player's turn is within 11 through 99 """
    if int(user_input) in range(11, 100):
        return True
    else:
        cl_scr()
        print("\nThis number is not from 11 through 99.")
        return False


def is_taken(row: int, col: int, board: list[list[str]]) -> bool:
    """ checks if the slot in the board is already occupied """
    if board[row][col] != " . ":
        print("\nThis slot is taken")
        return True
    else:
        return False


def change_player(player: bool) -> str:
    """ swap players """
    if player:
        return " X "
    else:
        return " O "


def is_row_win(active_player: str, board: list[list[str]]) -> bool:
    """ checks if player obtains its 5 continuous marks in a row """
    slot_count_row = 0                  # number of continuous marks in row
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == active_player:
                slot_count_row += 1
            else:
                slot_count_row = 0
            if slot_count_row == 5:
                return True
    return False


def is_col_win(active_player: str, board: list[list[str]]) -> bool:
    """ checks if player obtains its 5 continuous marks in a column """
    slot_count_col = 0                  # number of continuous marks in row
    for row in range(len(board)):
        for col in range(len(board)):
            if board[col][row] == active_player:
                slot_count_col += 1
            else:
                slot_count_col = 0
            if slot_count_col == 5:
                return True
    return False


def diagonals(board: list[list[str]]) -> tuple[list[list[str]], list[list[str]]]:
    """
    generates all possible diagonals which might to win
    :return: list of forward diagonals, list of backward diagonals
    """
    # inspired by
    # https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

    """ all possible diagonals """
    col = len(board[0])
    row = len(board)
    f_dia = [[] for _ in range(row + col - 1)]      # list of / diagonals
    b_dia = [[] for _ in range(len(f_dia))]         # list of \ diagonals
    min_b_dia = -row + 1

    for x in range(col):
        for y in range(row):
            f_dia[x + y].append(board[y][x])
            b_dia[x - y - min_b_dia].append(board[y][x])

    """ diagonals with length of 5+ """
    f_dia = [_ for _ in f_dia if len(_) >= 5]
    b_dia = [_ for _ in b_dia if len(_) >= 5]

    return f_dia, b_dia


def is_dia_win(active_player: str, board: list[list[str]]) -> bool:
    """ checks if player obtains its 5 marks in a diagonal """

    f_dia, b_dia = diagonals(board)

    for dia in f_dia:
        slot_count_f_dia = 0        # number of continuous marks in / diagonal
        for slot in dia:
            if slot == active_player:
                slot_count_f_dia += 1
            else:
                slot_count_f_dia = 0

            if slot_count_f_dia == 5:
                return True

    for dia in b_dia:
        slot_count_b_dia = 0        # number of continuous marks in \ diagonal
        for slot in dia:
            if slot == active_player:
                slot_count_b_dia += 1
            else:
                slot_count_b_dia = 0

            if slot_count_b_dia == 5:
                return True


def is_win(active_player: str, board: list[list[str]]) -> bool:
    """ combine results of particular win functions """
    if is_row_win(active_player, board) or is_col_win(active_player, board) or is_dia_win(active_player, board):
        return True


def main():
    """setting variables"""
    sepa: str = "=" * 49
    columns: int = 9
    rows: int = 9
    player: bool = True      # True refers to " X " False refers to " O "
    slots_taken: int = 0     # 81 refers to fully occupied board

    """generate boards"""
    board: list[list[str]] = gen_board(rows, columns)
    board_greeter: list[list[str]] = gen_board_greeter(rows, columns)

    """play Tic Tac Toe"""
    greeter(board, board_greeter)

    while True:
        active_player: str = change_player(player)
        pr_board(board)
        print(f"Player{active_player}")
        player_input = input("Choose the slot where you want to drag: ")

        """check if you want to quit"""
        if end(player_input, sepa):
            break

        """check if player_input is number"""
        if not is_number(player_input):
            print("Try again, please.", end="\n")
            continue

        """check if player_input is within bounds"""
        if not in_bounds(player_input):
            print("Try again, please.", end="\n")
            continue

        """obtain coordinates from player_input"""
        row = int(player_input[0]) - 1
        col = int(player_input[1]) - 1

        """check if slot is taken"""
        if is_taken(row, col, board):
            print("Try again, please.", end="\n")
            continue

        """write player_input to the board"""
        board[row][col] = active_player

        """check if board is full; full refers to draw"""
        slots_taken += 1
        if slots_taken == 81:
            print("", sepa, "It's a draw.".center(len(sepa)), sepa, sep="\n")
            pr_board(board)
            break

        """check if active_player won"""
        if is_win(active_player, board):
            print("", sepa, f"Player{active_player} WON".center(len(sepa)), sepa, sep="\n")
            pr_board(board)
            break

        """swap player"""
        player = not player


if __name__ == '__main__':
    main()
