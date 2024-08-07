from typing import Dict, Optional

from goboard_slow import Board, Move
from gotypes import Player, Point

COLS = "ABCDEFGHJKLMNOPQRST"
STONE_TO_CHAR: Dict[Optional[Player], str] = {
    None: " . ",
    Player.BLACK: " x ",
    Player.WHITE: " o ",
}


def print_move(player: Player, move: Move) -> None:
    """
    Prints the player's move in a readable format.

    Args:
        player (Player): The player making the move.
        move: The move being made.
    """
    if move.is_pass:
        move_str = "passes"
    elif move.is_resign:
        move_str = "resigns"
    else:
        move_str = f"{COLS[move.point.col - 1]}{move.point.row}"
    print(f"{player} {move_str}")


def print_board(board: Board) -> None:
    """
    Prints the current state of the board.

    Args:
        board: The board to be printed.
    """
    for row in range(board.num_rows, 0, -1):
        bump = " " if row <= 9 else ""
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print(f"{bump}{row} {''.join(line)}")
    print("    " + "  ".join(COLS[: board.num_cols]))
