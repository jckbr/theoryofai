# Support file for BFS implementation (BFS.py)

class Move: # Move object declaration
    def __init__(self, start, mid, end):
        self.start = start
        self.mid = mid
        self.end = end
    def toString(self):
        return "S:{0},M:{1},E:{2}".format(self.start, self.mid, self.end)

class Board: # Board object declaration
    def __init__(self, start):
        self.board = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
        self.moves = [Move(0, 1, 3), Move(0, 2, 5), Move(1, 3, 6), Move(1, 4, 8), Move(2, 4, 7), Move(2, 5, 9), Move(3, 1, 0), Move(3, 4, 5), Move(3, 7, 2), Move(3, 6, 10), Move(4, 7, 11), Move(4, 8, 13), Move(5, 2, 0), Move(5, 4, 3), Move(5, 8, 2), Move(5, 9, 14), Move(6, 3, 1), Move(6, 7, 8), Move(7, 4, 2), Move(7, 8 ,9), Move(8, 4, 1), Move(8, 7, 6), Move(9, 5, 2), Move(9, 8, 7), Move(10, 6, 3), Move(10, 11, 12), Move(11, 7, 4), Move(11, 12, 13), Move(12, 11, 10), Move(12, 7, 3), Move(12, 8, 5), Move(12, 13, 14), Move(13, 12, 11), Move(13, 8, 4), Move(14, 9, 5), Move(14, 13, 12)]
        self.board[start] = 0

    def moves(self):
        return self.moves

    def checkWin(self):
        if self.board.count(1) == 1:
            return 1
        else:
            return 0

    def makeMove(self, start, end): # checks if move is valid, if so make move
        for i in range(0, len(self.moves)):
            if self.moves[i].start == start and self.moves[i].end == end:
                if self.board[start] == 1 and self.board[self.moves[i].mid] == 1 and self.board[end] == 0:
                    self.board[self.moves[i].start] = 0
                    self.board[self.moves[i].mid] = 0
                    self.board[self.moves[i].end] = 1

    def nextMoves(self): # returns list of moves available
        temp = []
        for i in range(0, len(self.board)):
            if self.board[i] == 0:
                for j in self.moves:
                    if j.end == i:
                        temp.append(j)

        return temp

    def visualize(self, debug = 0): # visualizes the marble solitaire board
        tempVal = 0

        for i in range(0, 5):
            for k in range(0, 4 - i):
                print(end = ' ')

            for j in range(0, i + 1):
                if debug:
                    print(self.indices[tempVal], end = ' ')
                else:
                    print(self.board[tempVal], end = ' ')
                tempVal += 1
            print('')