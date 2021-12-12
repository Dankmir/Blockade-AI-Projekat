from Board import Board
#b = Board(11, 14, 3, 3, 3, 7, 10, 3, 10, 7, 1, 1)
b = Board(11, 14, 3, 3, 3, 7, 3, 5, 3, 10, 10, 10)
b.draw()

b.playTurn('O', 1, 8, 1, 'B', 4, 3)
b.playTurn('O', 1, 8, 1, 'B', 4, 4)

b.playTurn('X', 2, 4, 1, 'B', 4, 6)
b.playTurn('X', 2, 4, 1, 'B', 4, 7)

b.isEnd()
b.draw()

'''
- Provera da zidovi ne mogu da se postave oko pocetnih polja
'''