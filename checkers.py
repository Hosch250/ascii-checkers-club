class Checker:
    """The checkers piece."""

    # constants (Checker._____)
    PLAYER_ONE = 0
    PLAYER_TWO = 1

    # constructor
    def __init__(self, player):
        """Constructs a new checkers piece."""
        self.player = player
        self.king = False

    @staticmethod
    def character(piece):
        if piece is None: return ' '
        char = 'o' if piece.player == Checker.PLAYER_ONE else 'x'
        return char.upper() if piece.king else char

class Board:
    """The board on which the checkers lie."""

    # constructor
    def __init__(self):
        """Constructs a new, normal set up board."""
        self.data = []
        self.data.extend(Board.start_rows(Checker.PLAYER_ONE))
        self.data.extend(Board.empty_rows(2))
        self.data.extend(Board.start_rows(Checker.PLAYER_TWO))

    @staticmethod
    def start_rows(player):
        """The configuration of pieces that the game starts with."""
        r1, r2, r3 = [], [], []
        for _ in range(4):
            r1.extend([None, Checker(player)])
            r2.extend([Checker(player), None])
            r3.extend([None, Checker(player)])
        return [r1, r2, r3]

    @staticmethod
    def empty_rows(count):
        """Returns an amount of empty rows."""
        return [[None] * 8 for _ in range(count)]

    def render(self):
        """Returns an ASCII representation of the board."""
        s = '   A B C D E F G H \n'
        for n, row in enumerate(self.data):
            s += '  +-+-+-+-+-+-+-+-+\n'
            s += '%i |%s|\n' % (n, '|'.join([Checker.character(p) for p in row]))
        s += '  +-+-+-+-+-+-+-+-+'
        return s
        
    # x
    def is_empty(self, x, y):
        if x is 'A':
            xx = 0
        elif x is 'B':
            xx = 1
        elif x is 'C':
            xx = 2
        elif x is 'D':
            xx = 3
        elif x is 'E':
            xx = 4
        elif x is 'F':
            xx = 5
        elif x is 'G':
            xx = 6
        else:
            xx = 7
            
        return self.data[xx][y] is None

if __name__ == '__main__':
    board = Board()
    print(board.render())
