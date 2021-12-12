from Board import Board


startPositions = []

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

#b = Board(11, 14, [[3, 3], [3, 7], [10, 3], [10, 7]], 10)
b = Board(m, n, startPositions, walls, p)
b.draw()

b.playTurn('O', 1, 8, 1, 'B', 1, 1)
b.playTurn('O', 1, 8, 1, 'B', 1, 2)
b.playTurn('O', 1, 8, 1, 'B', 1, 3)
b.playTurn('O', 2, 8, 1, 'B', 1, 4)

b.playTurn('X', 1, 8, 1, 'G', 2, 2)
b.playTurn('X', 1, 8, 1, 'G', 3, 2)
b.playTurn('X', 1, 8, 1, 'G', 4, 2)
b.playTurn('X', 1, 8, 1, 'G', 5, 2)
b.playTurn('X', 2, 4, 1, 'G', 8, 2)


b.isEnd()
b.draw()

'''
'''