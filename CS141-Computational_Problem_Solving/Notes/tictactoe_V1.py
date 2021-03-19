class tictactoe():
    def __init__(self):
        self.__board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.__turn = 'X'
        self.__winner = False
        self.__full = False
        self.__results = ''

    def move(self):
        while self.__winner == False and self.__full == False:
            row = int(input('Input row(0-2) for the move: '))
            col = int(input('Input col(0-2) for the move: '))
            if self.__board[row][col] == ' ':
                self.__board[row][col] = self.__turn
                self.print_board()
                if self.__turn == 'X':
                    self.__turn == 'O'
                else:
                    self.__turn = 'X'
            else:
                print('Invalid Move!')
            if self.__board[0][0] != ' ' and self.__board[0][1] != ' '\
            and self.__board[0][2] != ' ' and self.__board[1][0] != ' '\
            and self.__board[1][1] != ' ' and self.__board[1][2] != ' '\
            and self.__board[2][0] != ' ' and self.__board[2][1] != ' '\
            and self.__board[2][2] != ' ':
            self.__full = True

            self.winner_check()
        if self.__winner == True:
            print('Player' + self.__results + ' won!')
        else:
            print('Game Over! Draw! ')
    def winner_check(self):
        # row
        for i in range(3):
            if self.__board[i][0] == self.__board[i][1] == self.__board[i][2] != ' ':
                self.__winner = True
                self.__results = self.__board[i][0]
        # col
        for i in range(3):
            if self.__board[0][i] == self.__board[1][i] == self.__board[2][i] != ' ':
                self.__winner = True
                self.__results = self.__board[0][i]
        # diag
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != ' ':
            self.__winner = True
            self.__results = self.__board[0][0]
        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != ' ':
            self.__winner = True
            self.__results = self.__board[0][2]


    def print_board(self):
        for i in range(2):
            print(self.__board[i][0] + '|' + self.__board[i][1] + '|' + self.__board[i][2])
            print('-----')
        print(self.__board[2][0] + '|' + self.__board[2][1] + '|' + self.__board[0][2])

game = tictactoe()
game.move()
