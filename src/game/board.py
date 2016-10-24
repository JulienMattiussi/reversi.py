from .color import UNDERLINE, colorize


class Board:

    """ Reversi Board """

    CELL_EMPTY = 2
    CELL_BLACK = 1
    CELL_WHITE = 0

    def __init__(self, rows=8, columns=8):

        """ Rows / Columns count must be even for placing the departure discs in the center of the board """

        if rows % 2 != 0 or columns % 2 != 0:
            raise ValueError("Board rows and columns count must be set with an even number.")

        self.cells = []
        self.rows = rows
        self.columns = columns

        self._init_board()

    def play(self, row, column, color):

        """ Place disk at the given position """

        if not self.is_possible_move(row, column):
            raise ValueError("You can't place a disk at the following position ({0}, {1})".format(row, column))

        self.cells[row][column] = color
        self.recompute_cells()

        return self.compute_score()

    def compute_score(self):

        """ Compute current score by color """

        score = {"white": 0, "black": 0}

        for row in self.cells:
            for col in row:
                if col == self.CELL_WHITE:
                    score["white"] += 1
                if col == self.CELL_BLACK:
                    score["black"] += 1

        return score

    def recompute_cells(self):

        """ Rearrange cells to flip disks """

        # TODO

    def render(self):

        """ Render current board """

        character = ""
        board_render = "_" * (self.columns * 2 + 1) + "\n"

        for row in self.cells:
            board_render += "|"
            for col in row:
                if col == self.CELL_WHITE:
                    character = "○"
                elif col == self.CELL_BLACK:
                    character = "●"
                else:
                    character = " "
                board_render += colorize(character, UNDERLINE) + "|"
            board_render += "\n"

        print(board_render)

    def get_possibles_positions(self):

        """ Return all possibles positions in an array of tuples """

        allowed_positions = []

        for rowidx, row in enumerate(self.cells):
            for colidx, col in enumerate(row):
                self.cells[rowidx][colidx] = col

        return allowed_positions

    def populate_from_positions_array(self, positions):

        """ Populate the current board with given positions """

        self._check_positions_array_validity(positions)

        for rowidx, row in enumerate(positions):
            for colidx, col in enumerate(row):
                self.cells[rowidx][colidx] = col

    def is_possible_move(self, row, column):

        return (row, column) in self.get_possibles_positions()

    def _check_positions_array_validity(self, positions):

        """Ensure that given positions match the current board configuration"""

        rowlen = len(positions)

        if rowlen != self.rows:
            raise ValueError("Invalid rows count for board population. {0} given, {1} expected.".format(rowlen, self.rows))

        for rowidx, row in enumerate(positions):
            if len(row) != self.columns:
                raise ValueError("Invalid columns count for board population at {0} row".format(rowidx))

    def _init_board(self):

        """ Init board with default reversi configuration """

        self.cells = [[self.CELL_EMPTY for x in range(self.columns)] for y in range(self.rows)]
