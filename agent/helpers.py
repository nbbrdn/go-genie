from goboard_slow import Board
from gotypes import Point


def is_point_an_eye(board: Board, point: Point, color) -> bool:
    """Checks if a point is an eye for the given color."""

    # A point cannot be an eye if it is occupied.
    if board.get(point) is not None:
        return False

    # All adjacent points must contain stones of the same color.
    if not all(
        board.is_on_grid(neighbor) and board.get(neighbor) == color
        for neighbor in point.neighbors()
    ):
        return False

    # Check the corners around the point: they must be friendly or off the board.
    friendly_corners, off_board_corners = 0, 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1),
    ]

    for corner in corners:
        if board.is_on_grid(corner):
            if board.get(corner) == color:
                friendly_corners += 1
        else:
            off_board_corners += 1

    # If the point is on the edge, all corners must be controlled.
    if off_board_corners > 0:
        return off_board_corners + friendly_corners == 4

    # If the point is in the center, at least three corners must be controlled.
    return friendly_corners >= 3
