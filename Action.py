class Action:
    def __init__(self, from_row, from_col, to_row, to_col):
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col

def doAction(action: Action, player, board):
    player.do_move(board, action.from_row, action.from_col, action.to_row, action.to_col)