class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass


class InvalidMove(Exception):
    pass


class TicTacToeBoard(dict):
    CELLS = ('A1', 'A2', 'A3',
                   'B1', 'B2', 'B3',
                   'C1', 'C2', 'C3')
    PLAYERS = ('O', 'X')

    def __init__(self):
        self.last_turn = ' '
        self.winner = ''
        dict.__init__(self)
        for key in TicTacToeBoard.CELLS:
            dict.__setitem__(self, key, ' ')

    def __getitem__(self, key):
        value = dict.__getitem__(self, key)
        return value

    def __setitem__(self, key, value):
        if key not in TicTacToeBoard.CELLS:
            raise InvalidKey
        elif value not in TicTacToeBoard.PLAYERS:
            raise InvalidValue
        elif not self.__is_your_turn(value):
            raise NotYourTurn
        elif self[key] != ' ':
            raise InvalidMove
        else:
            dict.__setitem__(self, key, value)
            if self.__win():
                self.__set_winner()

    def __str__(self):
        return (
            '\n  -------------\n' +
            '3 | {} | {} | {} |\n' +
            '  -------------\n' +
            '2 | {} | {} | {} |\n' +
            '  -------------\n' +
            '1 | {} | {} | {} |\n' +
            '  -------------\n' +
            '    A   B   C  \n').format(self['A3'], self['B3'], self['C3'],
                                        self['A2'], self['B2'], self['C2'],
                                        self['A1'], self['B1'], self['C1'])

    def game_status(self):
        if self.__win():
            return self.__get_winner()+' wins!'
        elif self.__done():
            return 'Draw!'
        else:
            return 'Game in progress.'

    def __done(self):
        return all(value != ' ' for value in self.values())

    def __win(self):
        if self.__horizontal_win():
            return self.__horizontal_win()
        elif self.__vertical_win():
            return self.__vertical_win()
        elif self.__diagonal_win():
            return self.__diagonal_win()

    def __set_winner(self):
        if self.winner == '':
            self.winner = self.__win()

    def __get_winner(self):
        return self.winner

    def __is_your_turn(self, value):
        if self.last_turn == ' ':
            self.last_turn = value
            return True
        elif self.last_turn != value:
            self.last_turn = value
            return True
        else:
            return False

    def __horizontal_win(self):
        columns = ('A', 'B', 'C')
        for column in columns:
            if self[column+'1'] == self[column+'2'] == self[column+'3'] != ' ':
                return self[column+'1']

    def __vertical_win(self):
        rows = ('1', '2', '3')
        for row in rows:
            if self['A'+row] == self['B'+row] == self['C'+row] != ' ':
                return self['A'+row]

    def __diagonal_win(self):
        if self['A1'] == self['B2'] == self['C3'] != ' ':
            return self['A1']
        elif self['A3'] == self['B2'] == self['C1'] != ' ':
            return self['A3']
