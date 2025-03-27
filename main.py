from player import Player
from Board import Board
from Adversarial_Search import AI
from Action import doAction

depth = 4 
player1 = Player(1)
player2 = Player(2)
board = Board(row_count=5, column_count=5, center_block=True)  

board.draw_board()

Round = 1
player1_ai = AI()
player2_ai = AI()

isPlayer1 = True

while True:
    if isPlayer1:
        ai_action = player1_ai.choose_action(board, player1, player2, depth)
        doAction(ai_action, player1, board)
        print(
            f"AI {player1.number} chose to move from "
            f"row={ai_action.from_row+1}, col={ai_action.from_col+1} to "
            f"row={ai_action.to_row+1}, col={ai_action.to_col+1}:"
        )
    else:
        ai_action = player2_ai.choose_action(board, player2, player1, depth)
        doAction(ai_action, player2, board)
        print(
            f"AI {player2.number} chose to move from "
            f"row={ai_action.from_row+1}, col={ai_action.from_col+1} to "
            f"row={ai_action.to_row+1}, col={ai_action.to_col+1}:"
        )

    board.draw_board()

    if player1.terminal_test(board) or player2.terminal_test(board):
        print(f"Round: {Round}\n")
        player1_count = board.count_pieces(player1)
        player2_count = board.count_pieces(player2)
        if player1_count > player2_count:
            print(f"{player1.number} wins with {player1_count} pieces!")
        elif player2_count > player1_count:
            print(f"{player2.number} wins with {player2_count} pieces!")
        else:
            print("Stalemate!")
        print(f"Player 1 pieces: {player1_count}")
        print(f"Player 2 pieces: {player2_count}")
        exit()

    isPlayer1 = not isPlayer1
    print(f"Round: {Round}\n")
    Round += 1