SHIPS = {
    'Carrier': 5,
    'Battleships': 4,
    'Cruiser': 3,
    'Submarine': 3,
    'Destroyer': 2
}


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.ships = []
        self.board = Board()

    def add_ship(self, type, row, col, direction):
        ship = Ship(type)
        self.ships.append(ship)
        self.board.add_ship(ship, row, col, direction)


class Ship:
    def __init__(self, type):
        self.type = type
        self.size = SHIPS[type]
        self.hit = False


class Board:
    def __init__(self):
        self.grid = []
        self.reset()

    def reset(self):
        for r in range(10):
            row = []
            for c in range(10):
                row.append(Cell())
            self.grid.append(row)

    def add_ship(self, ship, row, col, direction):
        if direction == 'V':
            for r in range (ship.size):
                self.grid[row+r][col].ship = ship
        else:
            for c in range (ship.size):
                self.grid[row][col+c].ship = ship

    def display_board_ships(self):
        for r in range(10):
            for c in range(10):
                print('- ' if self.grid[r][c].ship is None else 'S ', end='')
            print()


class Cell:
    def __init__(self):
        self.ship = None
        self.hit = False


class ConsoleGame:
    def __init__(self):
        self.player_a = Player("A")
        self.player_b = Player("B")
        self.current_player = self.player_a

    def get_ship_position(self):
        # TODO: loop until all values are valid
        row = int(input("Row 1-10: "))
        col = input("Col A-J: ")
        direction = input("H or V: ")
        return row-1, ord(col)-65, direction

    def set_ships(self):
        # TODO: lop for every player and for every ship
        row, col, direction = self.get_ship_position()
        self.player_a.add_ship('Submarine', row, col, direction)
        self.player_a.board.display_board_ships()
        row, col, direction = self.get_ship_position()
        self.player_b.add_ship('Submarine', row, col, direction)
        self.player_b.board.display_board_ships()


game = ConsoleGame()
game.set_ships()
'''
while game.can_play():
    game.display_board()
    row = int(input("Row 1-10: "))
    col = input("Col A-J")
    game.play(row, col)
game.display_winner()
'''
