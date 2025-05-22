import math
import time

class AIPlayer:

    def __init__(self, human_symbol, ai_symbol):
        self.ai_symbol = ai_symbol
        self.human_symbol = human_symbol
        self.actual_board = None

    def ai_make_move(self, board, board_num):
        self.actual_board = board

        # choose the board if the small board has been finished
        start_time_0 = time.time()
        if board.winning_cells[board_num] != " ":

            board_temp = self.actual_board.winning_cells
            best_score = -math.inf

            for sq in range(0, 9):

                if board_temp[sq] == " ":

                    board_temp[sq] = self.ai_symbol
                    new_score = self.minimax_alpha_beta_pruning(board_temp, False, start_time_0)
                    board_temp[sq] = " "

                    if new_score > best_score:
                        best_score = new_score
                        board_num = sq


        # Standard Minimax with Alpha-Beta Pruning for the move inside the small board
        best_score = -math.inf
        best_move = -math.inf

        start_time = time.time()
        temp_board = board.board[board_num]

        # Evaluate all possible moves
        for sq in range(9):
            if temp_board[sq] == " ":

                temp_board[sq] = self.ai_symbol
                new_score = self.minimax_alpha_beta_pruning(temp_board, False, start_time)
                temp_board[sq] = " "

                if new_score > best_score:
                    best_score = new_score
                    best_move = sq

        board.make_move_ai(best_move, board_num, self.ai_symbol)
        return best_move, board_num


    def minimax_alpha_beta_pruning(self, board, isMaximizing, start_time, alpha=-math.inf, beta=math.inf):
        state_board = self.check_winner(board)
        if state_board == self.ai_symbol:
            return 1
        elif state_board == self.human_symbol:
            return -1
        elif state_board == "Tie":
            return 0.5

        if time.time() - start_time > 4.0:
            return 0

        if isMaximizing:
            max_score = -math.inf
            for sq in range(9):
                if board[sq] == " ":

                    board[sq] = self.ai_symbol
                    new_score = self.minimax_alpha_beta_pruning(board, False, start_time, alpha, beta)
                    board[sq] = " "

                    max_score = max(max_score, new_score)

                    alpha = max(alpha, new_score)

                    if beta <= alpha:
                        break
            return max_score
        else:
            min_score = math.inf
            for sq in range(9):
                if board[sq] == " ":

                    board[sq] = self.human_symbol

                    new_score = self.minimax_alpha_beta_pruning(board, True, start_time, alpha, beta)

                    board[sq] = " "

                    min_score = min(min_score, new_score)
                    beta = min(beta, new_score)
                    if beta <= alpha:
                        break
            return min_score

    def check_winner(self, board: list) -> str:
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for positions in win_positions:
            if (board[positions[0]] == board[positions[1]] == board[positions[2]] != " "
                    and "T" not in [board[pos] for pos in positions]):
                return board[positions[0]]

        if " " not in board:
            return "Tie"

        return ""




