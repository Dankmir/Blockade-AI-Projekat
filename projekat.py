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
#game = Game(m, n, startPositions, walls, p)
game = Game(11, 14, [[3, 3], [3, 7], [10, 3], [10, 7]], 10, 'x')

game.draw()

game.placeWallHorizontal(2, 3)
game.placeWallHorizontal(4, 3)
game.placeWallVertical(3, 2)
#game.placeWallVertical(3, 4)

game.playTurn('X', 1, 6, 1, 'G', 3, 4)

game.draw()