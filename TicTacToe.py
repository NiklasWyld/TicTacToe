class Board:
    def __init__(self):
        self.state = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]

    def isTurnPossible(self, turn: int):
        if self.state[turn] == 0:
            return True
        else:
            return False

    def makeTurn(self, turn, symbol):
        if self.isTurnPossible(turn):
            self.state[turn] = symbol
            return True
        return False

    def isFull(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def checkWin(self, player):
        s = player.symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def getSymbol(self, n: int):
        if n == 0:
            return ' '
        elif n == 1:
            return 'X'
        elif n == -1:
            return 'O'

    def printBoard(self):
        print(f' {self.getSymbol(self.state[0])} | {self.getSymbol(self.state[1])} | {self.getSymbol(self.state[2])} \n'
              f' {self.getSymbol(self.state[3])} | {self.getSymbol(self.state[4])} | {self.getSymbol(self.state[5])} \n'
              f' {self.getSymbol(self.state[6])} | {self.getSymbol(self.state[7])} | {self.getSymbol(self.state[8])} ')

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

if __name__ == '__main__':
    player_x = Player(1)
    player_o = Player(-1)
    board = Board()
    active_player = player_x

    while not board.isFull():
        board.printBoard()

        try:
            turn = int(input(f'{board.getSymbol(active_player.symbol)} [1-9]: '))
        except ValueError:
            continue

        turn = turn - 1

        if turn < 0 or turn > 8:
            print('Enter a number between 1 and 9!')
            continue

        if not board.makeTurn(turn, active_player.symbol):
            print('Invalid move!')
            continue

        if board.checkWin(active_player):
            board.printBoard()
            print('You won!')
            exit()

        if active_player == player_x:
            active_player = player_o
        else:
            active_player = player_x

    print('Tie')