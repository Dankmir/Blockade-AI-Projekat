from Board import Board
from Game import Game
import copy 

startPositions = []
'''
print("Izaberite igraca")
p = input("X ili O: ")

print("Izaberite velicinu table, preporuceno je 11x14 a maksimalno dozvoljeno 22x28")
n = int(input("Broj vrsta table: "))
m = int(input("Broj kolona table: "))

walls = int(input("Izaberite broj zidova (preporuceno je 9 a maksimalno 18): "))

print("Izaberite pocetna polja pesaka")

print("Prvi pesak igraca X")
x = int(input("x = "))
y = int(input("y = "))
startPositions.append([x - 1, y - 1])

print("Drugi pesak igraca X")
x = int(input("x = "))
y = int(input("y = "))
startPositions.append([x - 1, y - 1])

print("Prvi pesak igraca O")
x = int(input("x = "))
y = int(input("y = "))
startPositions.append([x - 1, y - 1])

print("Drugi pesak igraca O")
x = int(input("x = "))
y = int(input("y = "))
startPositions.append([x - 1, y - 1])
'''

game = Game(11, 14, [[3, 3], [3, 7], [10, 3], [10, 7]], 10, 'x')
'''
game.playTurn('O', 1, 8, 1, 'B', 1, 1)
game.playTurn('O', 2, 8, 1, 'B', 1, 4)
'''
game.draw()
game.placeWallVertical(5, 5)
game.placeWallVertical(5, 5)
game.placeWallVertical(6, 5)
game.placeWallVertical(4, 5)


game.placeWallHorizontal(3, 3)
game.placeWallHorizontal(3, 3)
game.placeWallHorizontal(3, 4)
game.placeWallHorizontal(3, 2)


game.placeWallVertical(3, 2)
game.placeWallVertical(3, 3)
game.placeWallVertical(3, 4)

game.placeWallHorizontal(1, 11)
game.draw()
'''
game.states[-1].checkGraphConnection((0, 0), (1, 0))
game.states[-1].checkGraphConnection((0, 0), (1, 1))
game.states[-1].checkGraphConnection((0, 1), (1, 0))
game.states[-1].checkGraphConnection((0, 1), (1, 1))

game.states[-1].placeWallVertical(0, 0)
game.states[-1].placeWallHorizontal(1, 1)
game.states[-1].placeWallVertical(2, 0)
game.states[-1].placeWallVertical(0, 2)
game.states[-1].placeWallVertical(2, 2)

game.states[-1].checkGraphConnection((0, 0), (1, 0))
game.states[-1].checkGraphConnection((0, 0), (1, 1))
game.states[-1].checkGraphConnection((0, 1), (1, 0))
game.states[-1].checkGraphConnection((0, 1), (1, 1))
game.draw()
#b = Board(11, 14, [[3, 3], [3, 7], [10, 3], [10, 7]], 10, 'x')

'''
#b = Board(m, n, startPositions, walls, p)


'''
b.playTurn('O', 1, 8, 1, 'B', 1, 1)
b.playTurn('O', 1, 8, 1, 'B', 1, 2)
b.playTurn('O', 1, 8, 1, 'B', 1, 3)
b.playTurn('O', 2, 8, 1, 'B', 1, 4)

b.playTurn('X', 1, 8, 1, 'G', 2, 2)
b.playTurn('X', 1, 8, 1, 'G', 3, 2)
b.playTurn('X', 1, 8, 1, 'G', 4, 2)
b.playTurn('X', 1, 8, 1, 'G', 5, 2)
b.playTurn('X', 2, 4, 1, 'G', 8, 2)
'''