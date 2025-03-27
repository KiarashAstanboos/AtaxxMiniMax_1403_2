import numpy as np

class Board:
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2
    BLOCK = -1

    def __init__(self, row_count=7, column_count=7, center_block=False):
        self.row_count = row_count
        self.column_count = column_count
        self.board = np.zeros((self.row_count, self.column_count))
        self.board[0][0] = self.PLAYER_1
        self.board[self.row_count - 1][self.column_count - 1] = self.PLAYER_1
        self.board[0][self.column_count - 1] = self.PLAYER_2
        self.board[self.row_count - 1][0] = self.PLAYER_2
        if center_block and self.row_count % 2 == 1 and self.column_count % 2 == 1:
            center_row = self.row_count // 2
            center_col = self.column_count // 2
            self.board[center_row][center_col] = self.BLOCK

    def place_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_position(self, row, col):
        return (0 <= row < self.row_count and 
                0 <= col < self.column_count and 
                self.board[row][col] == self.EMPTY)

    def get_distance(self, from_row, from_col, to_row, to_col):
        return max(abs(from_row - to_row), abs(from_col - to_col))

    def capture_adjacent(self, row, col, piece):
        opponent = self.PLAYER_2 if piece == self.PLAYER_1 else self.PLAYER_1
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < self.row_count and 0 <= new_col < self.column_count and 
                    self.board[new_row][new_col] == opponent):
                    self.board[new_row][new_col] = piece

    def draw_board(self):
        piece_map = {self.EMPTY: ' ', self.PLAYER_1: '●', self.PLAYER_2: '◯', self.BLOCK: 'X'}
        print("   " + "   ".join(str(i + 1) for i in range(self.column_count)))
        for index, r in enumerate(self.board):
            print(index + 1, end='  ')
            print(" | ".join(piece_map[piece] for piece in r))
            print("   ", end='')
            print("-" * (self.column_count * 4 - 1))

    def count_pieces(self, player):
        piece = player.number
        return np.sum(self.board == piece)

    def is_board_full(self):
        return np.all((self.board != self.EMPTY) | (self.board == self.BLOCK))

if __name__ == '__main__':
    board = Board(row_count=5, column_count=5, center_block=True)
    board.draw_board()