import time
from marbleSolitaire import Board

# setup and visualize board, save moves to array
startpos = 4
board = Board(startpos)
board.visualize()
moves = board.moves

# find first move index
firstval = moves[0]
for i in moves:
    if i.end == startpos:
        firstval = i
        break

# start BFS
debug = 0
opened = [firstval]
closed = []
completed = False
while opened:
    X = opened.pop(0)

    board.makeMove(X.start, X.end)
    print('Tried move from', X.start, 'to', X.end)

    if board.checkWin():
        completed = True
        break
    else:
        temp = board.nextMoves()
        closed.append(X)
        for i in temp:
            if i not in opened and i not in closed:
                opened.append(i)

    if debug:
        print('X', X.toString())
        print('temp')
        for i in temp:
            print(i.toString(), end = ', ')
        print('\nopened')
        for i in opened:
            print(i.toString(), end = ', ')
        print('\nclosed')
        for i in closed:
            print(i.toString(), end = ', ')

    time.sleep(0.1)
    board.visualize()
print('Completed marble solitaire:', completed)
# end BFS