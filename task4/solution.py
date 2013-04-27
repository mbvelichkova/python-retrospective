class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass


class InvalidMove(Exception):
    pass


class TicTacToeBoard(dict):
    _coordinates = ('A1', 'A2', 'A3',
                   'B1', 'B2', 'B3',
                   'C1', 'C2', 'C3')
    _pulls = ('O', 'X')

    def __init__(self):
        self.last_turn = ' '
        self.winner = ''
        dict.__init__(self)
        for key in TicTacToeBoard._coordinates:
            dict.__setitem__(self, key, ' ')

    def __getitem__(self, key):
        value = dict.__getitem__(self, key)
        return value

    def __setitem__(self, key, value):
        if key not in TicTacToeBoard._coordinates:
            raise InvalidKey
        elif value not in TicTacToeBoard._pulls:
            raise InvalidValue
        elif not self._is_your_turn(value):
            raise NotYourTurn
        elif self[key] != ' ':
            raise InvalidMove
        else:
            dict.__setitem__(self, key, value)
            if self._win():
                self._set_winner()

    def __str__(self):
        _board = '\n  -------------\n' +\
            '3 | '+self['A3']+' | '+self['B3']+' | '+self['C3']+' |\n' +\
            '  -------------\n' +\
            '2 | '+self['A2']+' | '+self['B2']+' | '+self['C2']+' |\n' +\
            '  -------------\n' +\
            '1 | '+self['A1']+' | '+self['B1']+' | '+self['C1']+' |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'
        return _board

    def game_status(self):
        if self._win():
            return self._get_winner()+' wins!'
        elif self._done():
            return 'Draw!'
        else:
            return 'Game in progress.'

    def _done(self):
        return all(value != ' ' for value in self.values())

    def _win(self):
        if self._horizontal_win():
            return self._horizontal_win()
        elif self._vertical_win():
            return self._vertical_win()
        elif self._diagonal_win():
            return self._diagonal_win()

    def _set_winner(self):
        if self.winner == '':
            self.winner = self._win()

    def _get_winner(self):
        return self.winner

    def _is_your_turn(self, value):
        if self.last_turn == ' ':
            self.last_turn = value
            return True
        elif self.last_turn != value:
            self.last_turn = value
            return True
        else:
            return False

    def _horizontal_win(self):
        columns = ('A', 'B', 'C')
        for column in columns:
            if self[column+'1'] == self[column+'2'] == self[column+'3'] != ' ':
                return self[column+'1']

    def _vertical_win(self):
        rows = ('1', '2', '3')
        for row in rows:
            if self['A'+row] == self['B'+row] == self['C'+row] != ' ':
                return self['A'+row]

    def _diagonal_win(self):
        if self['A1'] == self['B2'] == self['C3'] != ' ':
            return self['A1']
        elif self['A3'] == self['B2'] == self['C1'] != ' ':
            return self['A3']