
#14 x 11, n = 14, m = 11
tabla = [
    ['   ', '1  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  ', '8  ', '9  ', 'A  ', 'B  ', 'C  ', 'D  ', 'E  '],
    ['   ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ',],
    ['1||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||1'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['2||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||2'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['3||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||3'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['4||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||4'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['5||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||5'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['6||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||6'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['7||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||7'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['8||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||8'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['9||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||9'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['A||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||A'],
    ['   ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  ', '-  '],
    ['B||', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |', '  |',  '  ||B'],
    ['   ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ', '=  ',],
    ['   ', '1  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  ', '8  ', '9  ', 'A  ', 'B  ', 'C  ', 'D  ', 'E  ']
]

"""
def drawFrame(n, tabla : list, reverse):
    lista1 = []
    lista2 = []
    pom = 0
    listaSlova = ['1  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  ', '8  ', '9  ', 'A  ', 'B  ', 'C  ', 'D  ', 'E  ', 'F  ', 
    'G  ', 'H  ', 'I  ']

    lista1.append('   ')
    lista2.append('   ')
    for i in range(1, n + 1):
            lista1.append(listaSlova[pom])
            pom += 1
            lista2.append('=  ')
    if reverse == False:
        tabla.append(lista1)
        tabla.append(lista2)
    else:
        tabla.append(lista2)
        tabla.append(lista1)

    return


def drawTable(n, m, firstX, secondX, firstO, secondO):
    tabla = []
    listaSlova = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    pom = 0
    lista1 = []
    lista2 = []
    lista2.append('   ')

    drawFrame(n, tabla, False)

    for i in range(0, m):
        for j in range(0, n + 1):
            if j == 0:
                lista1.append(listaSlova[pom] + '||')
            elif j == n:
                lista1.append('  ||' + listaSlova[pom])
                pom += 1
            else:
                lista1.append('  |')
            lista2.append('-  ')
        if i == m - 1:
            tabla.append(lista1.copy())
        else:
            lista2.pop()
            tabla.append(lista1.copy())
            tabla.append(lista2.copy())
        
        lista1.clear()
        lista2.clear()
        lista2.append('   ')


    drawFrame(n, tabla, True)
    initialState(firstX, secondX, firstO, secondO, tabla)
    stampaj(tabla)
    return tabla

def stampaj(tabla):
    print("")
    for x in tabla:
        print(*x) 

def initialState(firstX, secondX, firstO, secondO, tabla):
    tabla[firstX[0] * 2][firstX[1]] = 'X |'
    tabla[secondX[0] * 2][secondX[1]] = 'X |'
    tabla[firstO[0] * 2][firstO[1]] = 'O |'
    tabla[secondO[0] * 2][secondO[1]] = 'O |'
    return 

def play(pesak, potez, zid, pos, tabla, n):
    pos[0] *= 2
    potez[0] *= 2
    zid[1] *= 2

    valid = isValidMove(pos, potez, n)

    if valid == True:

        if pesak[0] == 'X':
            if(pesak[1] == 1):
                tabla[pos[0]][pos[1]] = tabla[pos[0]][pos[1]].replace('X', ' ')
                tabla[potez[0]][potez[1]] = tabla[potez[0]][potez[1]][:0] + 'X' + tabla[potez[0]][potez[1]][1:]
            else:
                tabla[pos[0]][pos[1]] = tabla[pos[0]][pos[1]].replace('X', ' ')
                tabla[potez[0]][potez[1]] = tabla[potez[0]][potez[1]][:0] + 'X' + tabla[potez[0]][potez[1]][1:]
        else:
            if(pesak[1] == 1):
                tabla[pos[0]][pos[1]] = tabla[pos[0]][pos[1]].replace('O', ' ')
                tabla[potez[0]][potez[1]] = tabla[potez[0]][potez[1]][:0] + 'O' + tabla[potez[0]][potez[1]][1:]
            else:
                tabla[pos[0]][pos[1]] = tabla[pos[0]][pos[1]].replace('O', ' ')            
                tabla[potez[0]][potez[1]] = tabla[potez[0]][potez[1]][:0] + 'O' + tabla[potez[0]][potez[1]][1:]
    else:
        print("Player " + pesak[0] + " made invalid move!")
        return
    
    #da vrati novu poziciju pijuna
    pos[0] = potez[0] // 2
    pos[1] = potez[1]

    if zid[0] == "P":
        tabla[zid[1] + 1][zid[2]] = '=  ' 
        tabla[zid[1] + 1][zid[2] + 1] = '=  '
    else:
        strPom = tabla[zid[1]][zid[2]]
        strPom = strPom.replace("|", "I")
        tabla[zid[1]][zid[2]] = strPom
        strPom = tabla[zid[1] + 2][zid[2]]
        strPom = strPom.replace("|", "I")
        tabla[zid[1] + 2][zid[2]] = strPom
    
    stampaj(tabla)
    
    isOver(tabla)

    return

def isOver(tabla):
    if tabla[initialO1[0] * 2][initialO1[1]][0] == 'X' or tabla[initialO2[0] * 2][initialO2[1]][0] == 'X':
        print("Winner is player X")
    if tabla[initialX1[0] * 2][initialX1[1]][0] == 'O' or tabla[initialX2[0] * 2][initialX2[1]][0] == 'O':
        print("Winner is player O")
    return

def isValidMove(pos, move, n):
    all_possible_moves = [
        [pos[0] - 4, pos[1]], [pos[0] - 2, pos[1] + 1],
        [pos[0], pos[1] + 2], [pos[0] + 2, pos[1] + 1],
        [pos[0] + 4, pos[1]], [pos[0] + 2, pos[1] - 1],
        [pos[0], pos[1] - 2], [pos[0] - 2, pos[1] - 1]
    ]
    if move in all_possible_moves and valid(move, n) == True:
        return True
    return False

def valid(move, n):
    if move[0] <= 0 or move[0] % 2 != 0 or move[0] >= n + 10 or move[1] <= 0 or move[1] >= n:
        return False
    return True
"""
"""
blockade = []
print("Izaberite velicinu table, preporuceno je 11x14 a maksimalno dozvoljeno 22x28")
n = int(input("Broj vrsta table: "))
m = int(input("Broj kolona table: "))
zidovi = int(input("Izaberite broj zidova (preporuceno je 9 a maksimalno 18): "))
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
print(" ")
"""
"""
blockade = []
n = 14
m = 11
zidovi = 9
firstX = [4, 4]
secondX = [8, 4]
firstO = [4, 11]
secondO = [8, 11]

initialX1 = [4, 4]
initialX2 = [8, 4]
initialO1 = [4, 11]
initialO2 = [8, 11]

blockade = drawTable(n, m, firstX, secondX, firstO, secondO)
play(["X", 1], [3, 5], ["Z", 1, 6], firstX, blockade, n)
play(["O", 1], [1, 5], ["P", 4, 5], firstO, blockade, n)
"""

from Board import Board

b = Board(11, 14)

b.placeWallHorizontal(0, 0)
b.placeWallHorizontal(9, 0)
b.placeWallHorizontal(0, 12)
b.placeWallHorizontal(9, 12)

b.placeWallVertical(1, 1)
b.placeWallVertical(8, 1)
b.placeWallVertical(1, 11)
b.placeWallVertical(8, 11)

b.placePlayer(3, 3, 0)
b.placePlayer(7, 3, 0)

b.placePlayer(3, 10, 1)
b.placePlayer(7, 10, 1)

b.draw()