from Board import Board
from player import Player

def utility(board: Board, player: Player, opponent: Player):
    value = 0

    player_pieces = board.count_pieces(player)
    opponent_pieces = board.count_pieces(opponent)
    
    # If the game is over (terminal state), assign a decisive value
    if player.terminal_test(board):
        if player_pieces > opponent_pieces:
            value += 100000  # Player wins
        elif opponent_pieces > player_pieces:
            value -= 100000  # Opponent wins
        else:
            value = 0  # Draw
    else:
        # Heuristic for non-terminal states: difference in piece counts
        value += (player_pieces - opponent_pieces)

    return value