class UltimateTicTacToeBoard:
    def __init__(self):
        self.board = []
        for i in range(9):
            r = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            self.board.append(r)
        self.winning_cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(' '.join(map(str, self.board[i * 3 + j][:3])), end=' | ' if j < 2 else '')
            print()

            for j in range(3):
                print(' '.join(map(str, self.board[i * 3 + j][3:6])), end=' | ' if j < 2 else '')
            print()

            for j in range(3):
                print(' '.join(map(str, self.board[i * 3 + j][6:])), end=' | ' if j < 2 else '')
            print()

            print("-" * 22)

    def check_if_valid_move(self, move, board_num):
        move = move - 1
        board_num = board_num - 1

        if move > 8 or move < 0:
            return False
        if board_num > 8 or board_num < 0:
            return False

        if self.board[board_num][move] == "X" or self.board[board_num][move] == "O":
            return False

        return True

    def check_valid_board_num(self, board_num):
        bn = board_num - 1

        if bn > 8 or bn < 0:
            return False

        return self.winning_cells[bn] == " "

    def make_move_human(self, move, board_num, sign):
        self.board[board_num - 1][move - 1] = sign

    def make_move_ai(self, move, board_num, sign):
        self.board[board_num][move] = sign


    def check_winner_small(self):
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for board_num in range(9):
            grid = self.board[board_num]

            for positions in win_positions:
                if (grid[positions[0]] == grid[positions[1]] == grid[positions[2]] != " "
                        and "T" not in [grid[pos] for pos in positions]):
                    winner = grid[positions[0]]
                    self.winning_cells[board_num] = winner

                    if winner == "X":
                        self.draw_X(board_num)
                    else:
                        self.draw_O(board_num)

                if all(sq != " " for sq in self.board[board_num]):
                    self.draw_tie(board_num)
                    self.winning_cells[board_num] = "T"

    def draw_tie(self, board_num):
        self.board[board_num] = [
            "T", "T", "T",
            "T", "T", "T",
            "T", "T", "T"
        ]

    def draw_X(self, board_num):
        self.board[board_num] = [
            "X", " ", "X",
            " ", "X", " ",
            "X", " ", "X"
        ]

    def draw_O(self, board_num):
        self.board[board_num] = [
            "O", "O", "O",
            "O", " ", "O",
            "O", "O", "O"
        ]

    def check_winner_big(self):
        win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for positions in win_positions:
            if (self.winning_cells[positions[0]] == self.winning_cells[positions[1]] == self.winning_cells[positions[2]] != " "
                    and "T" not in [self.winning_cells[pos] for pos in positions]):
                return self.winning_cells[positions[0]]
        return False

    def check_if_tie(self):
        if all(sq != " " for sq in self.winning_cells):
            return True
        return False

