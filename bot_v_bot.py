import time
from typing import Dict, Tuple

from goboard_slow import GameState
from gotypes import Player
from agent.naive import RandomBot
from utils import print_board, print_move


def setup_game(board_size: int) -> Tuple[GameState, Dict[Player, RandomBot]]:
    """
    Creates a new game state and sets up the bots.

    Args:
        board_size (int): The size of the board.

    Returns:
        GameState: The initial game state.
        dict: A dictionary of bots for each player.
    """
    game = GameState.new_game(board_size)
    bots = {
        Player.BLACK: RandomBot(),
        Player.WHITE: RandomBot(),
    }
    return game, bots


def play_game(game: GameState, bots: Dict[Player, RandomBot]) -> None:
    """
    Plays the game until it is over.

    Args:
        game (GameState): The current game state.
        bots (dict): A dictionary of bots for each player.
    """
    while not game.is_over():
        time.sleep(0.3)

        print(chr(27) + "[2J")  # Clear the screen
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


def main() -> None:
    """
    The main function to start the game.
    """
    board_size = 9
    game, bots = setup_game(board_size)
    play_game(game, bots)


if __name__ == "__main__":
    main()
