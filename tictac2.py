import random


class TicTacToe:

    def __init__(self, player1_name='Player 1', player2_name='Player 2'):
        self.board = []
        self.player1_name = player1_name
        self.player2_name = player2_name

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.choice([self.player1_name, self.player2_name])

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return self.player1_name if player == self.player2_name else self.player2_name


    

 

    def show_board(self):
        print("   1 2 3 ")
        for i, row in enumerate(self.board):
            print(f"{i + 1} - {' '.join(row)}")

    def start(self):
        self.create_board()

        current_player = self.get_random_first_player()
        while True:
            print(f"{current_player}'s turn")

            self.show_board()

            # taking user input
            while True:
                try:
                    row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
                    if not (1 <= row <= 3 and 1 <= col <= 3):
                        raise ValueError
                    if self.board[row - 1][col - 1] != '-':
                        raise ValueError
                    break
                except:
                    print("Invalid input! Please enter valid row and column numbers.")

            # fixing the spot
            self.fix_spot(row - 1, col - 1, 'X' if current_player == self.player1_name else 'O')

            # checking whether current player is won or not
            if self.is_player_win('X' if current_player == self.player1_name else 'O'):
                print(f"{current_player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            current_player = self.swap_player_turn(current_player)

        # showing the final view of board
        print()
       
TicTacToe().start()
