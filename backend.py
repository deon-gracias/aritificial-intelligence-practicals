import random


class TicTacToe2d:
    # " char list containing x and o "
    board = []

    magicSquare = [
        4, 9, 2,
        3, 5, 7,
        8, 1, 6,
    ]
    usedSquarePosition = []
    round = 0
    positionsByCpu = []
    positionsByHuman = []

    def __init__(self):
        self.board = [
            None for i in range(9)
        ]

        for i in range(100):
            self.round = i
            # print(i)
            if i % 2 == 0:
                self.take_user_input()
                if self.hasWon('x'):
                    print(" you won ")
                    break
                elif self.isGameOver():
                    break

            else:
                self.computer_input()
                if self.hasWon('o'):
                    print(" pc won ")
                    break
                elif self.isGameOver():
                    break

    #     user prompt for position( 0.. 9)

    def take_user_input(self):
        print("Your Turn !!")
        ip = int(input(" choose position "))
        # for simplicity assume user is x and runs first
        self.board[ip] = 'x'
        self.usedSquarePosition.append(ip)
        self.positionsByHuman.append(ip)
        self.display_board()

    def display_board(self):
        for i in range(9):
            if i % 3 == 0:
                print()
                print(self.board[i], end=' ')
            else:
                print(self.board[i], end=' ')
        print("\n")


    def computer_input(self):
        print("Computer's turn !!")
        if self.round <= 3:
            print("thinking")
            i = random.randint(0, 8)
            while i in self.usedSquarePosition:
                i = random.randint(0, 8)
            self.board[i] = 'o'
            self.usedSquarePosition.append(i)
            self.positionsByCpu.append(i)
        else :
            move = self.get_winning_move()
            # TODO land here for debuggin winning move
            # print(f"here and move {move}")

            # print(move)
            # win if you can
            if move != -404:
                self.board[move] = 'o'
                self.usedSquarePosition.append(move)
                self.positionsByCpu.append(move)
                #     debugging

            #     otherwise block that person from winning
            else :

                b = self.get_blocking_move()
                # TODO land here for debuggin block move
                # print(f"here and move {b}")

                if b != -404:
                    self.board[b] = 'o'
                    self.usedSquarePosition.append(b)
                    self.positionsByCpu.append(b)
                else:
                    i = random.randint(0, 8)
                    while i in self.usedSquarePosition:
                        i = random.randint(0, 8)
                    self.board[i] = 'o'
                    self.usedSquarePosition.append(i)
                    self.positionsByCpu.append(i)



        print()
        self.display_board()

    def get_blocking_move(self):
        for j in self.positionsByHuman:
            for k in self.positionsByHuman:
                if j != k:
                    for i in range(9):
                        if i not in self.usedSquarePosition:
                            if self.magicSquare[i] + self.magicSquare[j] + self.magicSquare[k] == 15:
                                return i
        return -404

        pass

    def checkWinner(self):
        if self.hasWon('x'):
            print(" X win !!")
        elif self.hasWon('o'):
            print(" O win !!")
        else:
            print(" No winner yet !!")

    def isGameOver(self):
        if None not in self.board:
            return True
        else:
            return False

    def hasWon(self, player):
        # try all combinations 123 , 124,  xyz such as x!= y != z so to get hold of different squares.
        # then check whether triplet completely have been taken by player( x or 0)
        #  then check whether those three points are collinear or not

        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if (i != j and i != k and j != k):
                        if self.board[i] == player and self.board[j] == player and self.board[k] == player:
                            if self.magicSquare[i] + self.magicSquare[j] + self.magicSquare[k] == 15:
                                return True
        return False

    def think(self):
        i = random.randint(0, 8)
        while i in self.usedSquarePosition:
            i = random.randint(0, 8)
        self.board[i] = 'o'
        self.usedSquarePosition.append(i)
        self.positionsByCpu.append(i)
        pass


    def get_winning_move(self):
        print("here")
        for j in self.positionsByCpu:
            for k in self.positionsByCpu:
                if j != k:
                    for i in range(9):
                        if i not in self.usedSquarePosition:
                            if self.magicSquare[i] + self.magicSquare[j] + self.magicSquare[k] == 15:
                                return i
        return -404




if __name__ == "__main__":
    TicTacToe2d()
    pass