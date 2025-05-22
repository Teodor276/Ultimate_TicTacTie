from board import UltimateTicTacToeBoard
from ai import AIPlayer
class UltimateTicTacToeGame:
    def __init__(self):
        self.human_player = "X"
        self.computer_player = "O"
    def make_human_move(self, board_num, b):
        while True:
            try:
                if b.check_valid_board_num(board_num):
                    move = int(input(f"In which cell would you like to place your move? You are in board {board_num}. (1-9): "))
                else:
                    while True:
                        board_num = int(input("The last board is finished, choose any unfinished board (1-9): "))
                        if b.check_valid_board_num(board_num):
                            move = int(input(f"In which cell would you like to place your move? You are in board {board_num}. (1-9): "))
                            break

                if b.check_if_valid_move(move, board_num):
                    b.make_move_human(move, board_num, self.human_player)
                    break
                else:
                    print("Move not available! Try Again!")
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")

        return move

    def select_player_symbols(self):
        while True:
            choice = input("Do you want to be X or O? (X goes first): ").upper()
            if choice in ["X", "O"]:
                self.human_player = choice
                self.computer_player = "O" if choice == "X" else "X"
                break
            else:
                print("Invalid choice! Please choose either X or O.")
    def play_game(self):

        print("""
!!! Important !!!

Ultimate Tic-Tac-Toe Board Representation:
    
To choose the board to play in, simply input the number of the board you want to access.

Also, the same structure is followed within the smaller board, where you would input the number of the cell where you want to place your move.

The structure:

1 | 2 | 3
----------
4 | 5 | 6
----------
7 | 8 | 9

After each of the small boards have been completed the program will draw:
                'X' for board won by X
                'O' for board won by O
                fill all squares with 'T' if tied. 
       
        """)

        self.select_player_symbols()

        b = UltimateTicTacToeBoard()
        computer = AIPlayer(self.human_player, self.computer_player)

        b.display_board() if self.human_player == "X" else False

        while True:
            try:
                next_board_num = int(
                    input("In which board would you like to start playing? (1-9): ")) if self.human_player == "X" else 5
                if 1 <= next_board_num <= 9:
                    break
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        board_played = None
        is_human_turn = True if self.human_player == "X" else False

        while True:
            if is_human_turn:
                next_board_num = self.make_human_move(next_board_num, b)
            else:
                next_board_num, board_played = computer.ai_make_move(b, next_board_num - 1)
                next_board_num = next_board_num + 1


            b.check_winner_small()
            if b.check_if_tie():
                print("\nThe has ended as a TIE! Better luck next time!\n")
                b.display_board()
                break
            if b.check_winner_big() in ["X", "O"]:
                print(f"\n{b.check_winner_big()} won the game!\n")
                b.display_board()
                break

            if not is_human_turn:
                print()
                b.display_board()
                print()
                print(f"\nAI made the move on board {board_played + 1} to square {next_board_num}\n")
            is_human_turn = not is_human_turn


