class TicTacToe:
    def __init__(self):
        self.board = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
        self.current_marker = ''
        self.current_player = 1

    def print_board(self):
        for i in range(3):
            print(f" {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print("---|---|---")

    def place_marker(self, slot):
        row = (slot - 1) // 3
        col = (slot - 1) % 3

        if self.board[row][col] not in ['X', 'O']:
            self.board[row][col] = self.current_marker
            return True
        else:
            return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.current_player
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.current_player

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.current_player
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.current_player

        return 0

    def swap_player_and_marker(self):
        self.current_marker = 'O' if self.current_marker == 'X' else 'X'
        self.current_player = 2 if self.current_player == 1 else 1

    def start_game(self):
        self.current_marker = input("Player 1, choose your marker (X or O): ").upper()

        winner = 0
        for i in range(9):
            self.print_board()
            try:
                slot = int(input(f"Player {self.current_player}, choose a slot (1-9): "))
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if slot < 1 or slot > 9 or not self.place_marker(slot):
                print("Invalid move! Try again.")
                continue

            winner = self.check_winner()
            if winner != 0:
                self.print_board()
                print(f"Player {winner} wins!")
                break

            self.swap_player_and_marker()

        if winner == 0:
            self.print_board()
            print("It's a draw!")


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
