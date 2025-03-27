from Board import Board
import typing
from Action import Action

class Player:
    def __init__(self, playerNumber):
        self.number = playerNumber

    def getValidActions(self, board: Board) -> typing.List[Action]:
        actions = []
        for from_row in range(board.row_count):
            for from_col in range(board.column_count):
                if board.board[from_row][from_col] == self.number:
                    for to_row in range(board.row_count):
                        for to_col in range(board.column_count):
                            distance = board.get_distance(from_row, from_col, to_row, to_col)
                            if distance in [1, 2] and board.is_valid_position(to_row, to_col):
                                action = Action(from_row, from_col, to_row, to_col)
                                # Estimate captures
                                captures = sum(1 for dr in [-1, 0, 1] for dc in [-1, 0, 1] 
                                            if 0 <= to_row + dr < board.row_count and 
                                                0 <= to_col + dc < board.column_count and 
                                                board.board[to_row + dr][to_col + dc] == (3 - self.number))
                                actions.append((captures, distance, action))
        # Sort by captures (descending) and distance (ascending)
        actions.sort(key=lambda x: (-x[0], x[1]))
        return [action for _, _, action in actions]

    def do_move(self, board: Board, from_row, from_col, to_row, to_col):
        distance = board.get_distance(from_row, from_col, to_row, to_col)
        if distance == 1:
            board.place_piece(to_row, to_col, self.number)
        elif distance == 2:
            board.place_piece(to_row, to_col, self.number)
            board.place_piece(from_row, from_col, board.EMPTY)
        board.capture_adjacent(to_row, to_col, self.number)

    def terminal_test(self, board: Board):
        if len(self.getValidActions(board)) == 0 or board.is_board_full():
            return True
        return False