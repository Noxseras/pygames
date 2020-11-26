class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.score = 0


class Board:
    def __init__(self):
        self.grid = []
        self.reset()

    def reset(self):
        self.grid = [[None, None, None], [None, None, None], [None, None, None]]

    def play(self, player, r, c):
        if r < 1 or r > 3 or c < 1 or c > 3:
            return False
        if self.grid[r - 1][c - 1] is None:
            self.grid[r - 1][c - 1] = player
            return True
        else:
            return False

    def display(self):
        for i in range(3):
            for j in range(3):
                symbol = '-' if self.grid[i][j] is None else self.grid[i][j].symbol
                print(symbol, end=' ')
            print()

    def winner(self):
        for i in range(3):
            if self.grid[i][0] is not None and self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                return self.grid[i][0]
            if self.grid[0][i] is not None and self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                return self.grid[0][i]
        if self.grid[0][0] is not None and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return self.grid[0][0]
        if self.grid[0][2] is not None and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return self.grid[0][2]
        return None

    def tie(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] is None:
                    return False
        return True


class ConsoleGame:
    def __init__(self):
        self.a = Player('X')
        self.b = Player('O')
        self.current = self.a
        self.board = Board()

    def can_play(self):
        w = self.board.winner()
        if w is not None:
            print(w.symbol, ' wins')
            w.score += 1
            self.current = w
            return False
        if self.board.tie():
            return False
        return True

    def play(self, r, c):
        if self.board.play(self.current, r, c):
            self.current = self.a if self.current == self.b else self.b
        else:
            print("Try again")

    def print_score(self):
        print("SCORE X:" + str(self.a.score) + " O:" + str(self.b.score))


if __name__ == "__main__":
    game = ConsoleGame()

    while True:
        while game.can_play():
            game.board.display()
            try:
                row = int(input("Row: "))
                col = int(input("Column: "))
                game.play(row, col)

            except ValueError:
                print('Invalid values, try again')

        game.board.display()
        game.print_score()

        ans = input("Play again? y/n: ")
        if ans == 'n':
            break
        else:
            game.board.reset()