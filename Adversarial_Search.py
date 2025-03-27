import copy
from player import Player
from Board import Board
from Action import doAction
from utility import *

class AI:
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    def choose_action(self, board, player, opponent, max_depth):
        best_action = self.do_minimax(
            copy.deepcopy(board),
            copy.copy(player),
            copy.copy(opponent),
            max_depth,
        )
        return best_action

    def deepCopy(self, player, opponent, board) -> tuple[Player, Player, Board]:
        player_copy = copy.deepcopy(player)
        opponent_copy = copy.deepcopy(opponent)
        next_board = copy.deepcopy(board)
        return player_copy, opponent_copy, next_board

    def succesor(self, board: Board, player: Player, opponent: Player, reverse=False):
        if (reverse):
            actions = opponent.getValidActions(board)
        else:
            actions = player.getValidActions(board)

        result = []
        for action in actions:
            player_copy, opponent_copy, next_board = self.deepCopy(player, opponent, board)
            if (reverse):
                doAction(action, opponent_copy, next_board)
            else:
                doAction(action, player_copy, next_board)
            result.append([next_board, player_copy, opponent_copy, action])
            """" next board , player, opponent , action"""
        return result

    def do_minimax(self, board: Board, player: Player, opponent: Player, depth):
        alpha = -100000000
        beta = 100000000
        value, state = self.max(board, player, opponent, depth, alpha, beta)
        return state[3]

    def max(self, board: Board, player: Player, opponent: Player, depth, alpha, beta):
        if player.terminal_test(board): return utility(board, player, opponent), None
        if depth == 0: return utility(board, player, opponent), None
        possible_states = self.succesor(board, player, opponent)
        beststate = None
        bestvalue = self.MIN_VALUE
        for state in possible_states:
            temp, _ = self.min(state[0], state[1], state[2], depth - 1, alpha, beta)
            if bestvalue <= temp:
                bestvalue = temp
                beststate = state
            if bestvalue >= beta: return bestvalue, beststate
            alpha = max(alpha, bestvalue)
        return bestvalue, beststate

    def min(self, board: Board, player: Player, opponent: Player, depth, alpha, beta):
        if player.terminal_test(board): return utility(board, player, opponent), None
        if depth == 0: return utility(board, player, opponent), None
        possible_states = self.succesor(board, player, opponent, True)
        beststate = None
        bestvalue = self.MAX_VALUE
        for state in possible_states:
            temp, _ = self.max(state[0], state[1], state[2], depth - 1, alpha, beta)
            if bestvalue >= temp:
                bestvalue = temp
                beststate = state
            if bestvalue <= alpha: return bestvalue, beststate
            beta = min(beta, bestvalue)
        return bestvalue, beststate