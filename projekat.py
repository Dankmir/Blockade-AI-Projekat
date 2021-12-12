from Board import Board


print("Izaberite velicinu table, preporuceno je 11x14 a maksimalno dozvoljeno 22x28")
n = int(input("Broj vrsta table: "))
m = int(input("Broj kolona table: "))
walls = int(input("Izaberite broj zidova (preporuceno je 9 a maksimalno 18): "))
print("Izaberite pocetna polja pesaka")
print("Prvi pesak igraca X")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
firstX = [x1, y1]
print("Drugi pesak igraca X")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
secondX = [x1, y1]
print("Prvi pesak igraca O")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
firstO = [x1, y1]
print("Drugi pesak igraca O")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
secondO = [x1, y1]

#b = Board(11, 14, 3, 3, 3, 7, 10, 3, 10, 7, 1, 1)
b = Board(m, n, firstX, secondX, firstO, secondO, walls)
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