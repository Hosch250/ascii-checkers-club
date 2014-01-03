class Checker:
    """The checkers piece."""

    # constants (Checker._____)
    PLAYER_ONE = 'one'
    PLAYER_TWO = 'two'

    # constructor
    def __init__(self, player):
        """Constructs a new checkers piece."""
        self.player = player
        self.king = False

    @staticmethod
    def character(piece):
        """Returns the character for a piece (' ' (a space), x, o, X, or O)."""
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
            r1.extend([None, Checker(player)] if player == Checker.PLAYER_ONE else [Checker(player), None])
            r2.extend([None, Checker(player)] if player == Checker.PLAYER_TWO else [Checker(player), None])
            r3.extend([None, Checker(player)] if player == Checker.PLAYER_ONE else [Checker(player), None])
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

    def move(self, player, from_coords, to_coords):
        """
        Given a player that is moving, and A0-style coordinates for from and to, moves the piece.
        Returns a string (error message) if move failed, None otherwise.
        TODO jumping and capturing
        """
        
        while not is_coord(from_coord) or not is_coord(to_coord):
            new_move = input('Player %s, enter move (for example, A0 B1 to move the piece at A0 to B1): ' % player).split(' ')
            from_coord, to_coord = move[0], move[1]
        
        from_y, from_x = 'ABCDEFGH'.index(from_coords[0]), int(from_coords[1])
        to_y, to_x = 'ABCDEFGH'.index(to_coords[0]), int(to_coords[1])
        if self.data[from_x][from_y] is None:
            return 'There is no piece there!'
        elif self.data[from_x][from_y].player == player:
            if abs(from_x - to_x) == 1 and abs(from_y - to_y) == 1:
                if self.data[to_x][to_y] is None:
                    self.data[to_x][to_y], self.data[from_x][from_y] = self.data[from_x][from_y], None
                    return None
                else:
                    return 'There\'s already a piece in that space!'
            else:
                return 'That\'s not a diagonal move!'
        else:
            return 'That\'s not your piece!'

def is_coord(coord):
    return coord in ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
                     'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
                     'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
                     'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
                     'E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7',
                     'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7',
                     'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7',
                     'H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7']

def ask_for_move(player, board):
    """Ask the player for a move, and move there, given a board."""
    move = input('Player %s, enter move (for example, A0 B1 to move the piece at A0 to B1): ' % player).split(' ')
    message = board.move(player, move[0], move[1])
    while message is not None:
        move = input(message + ' Please try again: ').split(' ')
        message = board.move(player, move[0], move[1])

if __name__ == '__main__':
    players = input('Enter number of players (1 or 2): ')
    while players not in ['1', '2']:
        players = input('Invalid number of players. Try again: ')

    if players == '1':
        print('AI not implemented yet. So... I\'ll just... do nothing')
    else:
        board = Board()
        while True:
            print(board.render())
            ask_for_move(Checker.PLAYER_ONE, board)
            print(board.render())
            ask_for_move(Checker.PLAYER_TWO, board)
