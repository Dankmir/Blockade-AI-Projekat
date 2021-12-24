from Node import Node
from Player import Player
from colorama import *
from functools import *

class Board:
    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S' ]

    def __init__(self, w, h, startPositions, numOfWalls, whoPlaysFirst):
        self.players = [Player('X', startPositions[0], self), Player('X', startPositions[1], self), Player('O', startPositions[2], self), Player('O', startPositions[3], self)]
        init()
        self.width = w 
        self.height = h * 2
        self.startNodes = startPositions
        self.walls = [[numOfWalls, numOfWalls], [numOfWalls, numOfWalls]]
        self.nodes = []

        for i in range(self.height):
            self.nodes.append([])
            for j in range(self.width):
                self.nodes[i].append(Node(i, j))

    def draw(self):
        c = 0
        print('    ', end='')
        print(*self.symbols[:self.width], sep='   ')
        print(*[('  ┏━' if i == 0 else '━━┓' if i == self.width else '━━┳━') for i in range(self.width + 1)], sep='')
        for i in range(self.height - 1):
                l = [((x.getSymbol() + '╋') if i % 2 != 0 else (self.getPlayerSymbol(i//2,j) + x.getSymbol())) for j,x in enumerate(self.nodes[i])]
                l.insert(0, ' ┃' if i % 2 == 0 else ' ┣')
                l.insert(0, self.symbols[c] if i % 2 == 0 else ' ')
                a = l.pop()[:-1:]
                l.append(f'{self.getPlayerSymbol(i//2,self.width-1)}┃' if i % 2 == 0 else a + '┫')
                l.append(' ' + self.symbols[c] if i % 2 == 0 else ' ')
                print(*l, sep='')
                if i % 2 == 0:
                    c += 1
        print(*[('  ┗━' if i == 0 else '━━┛' if i == self.width else '━━┻━') for i in range(self.width + 1)], sep='')
        print('    ', end='')
        print(*self.symbols[:self.width], sep='   ')

    def getPlayerSymbol(self, x, y):
        res = list(filter(lambda a: a.x == x and a.y == y, self.players))
        if len(res) > 0:
            return f' {res.pop().symbol} '
        return self.checkForStartingPosition(x, y)

    def checkForStartingPosition(self, x, y):
        res = list(filter(lambda a: a[0] == x and a[1] == y, self.startNodes))
        if len(res) > 0:
            index = self.startNodes.index([x, y])
            return (Fore.YELLOW if index < 2 else Fore.RED) + ' ⦿ ' + Style.DIM + Style.RESET_ALL
        else:
            return '   '

    def movePlayer(self, dir, distance, player):
        return self.players[player].move(dir, distance, self.width, self.height)
        
    def placeWallHorizontal(self, x, y):
        x1 = y*2 + 1
        y1 = x
        x2 = y*2 + 1
        y2 = x + 1  
        vX1 = y*2
        vY1 = x
        vX2 = y*2 + 2
        vY2 = x

        if (self.nodes[vX1][vY1].hasWall and self.nodes[vX2][vY2].hasWall or self.nodes[x1][y1 + 1].hasWall or self.nodes[x1][y1].hasWall):
            print("[Horizontal Wall] THERE IS ALREADY WALL")
            return False

        if x > self.width - 2:
            print("HORIZONTAL WALL X OVERFLOW.") 
            return False

        if y*2 > self.height - 3:
            print("HORIZONTAL WALL Y OVERFLOW.") 
            return False

        self.nodes[x1][y1].hasWall = True
        self.nodes[x2][y2].hasWall = True

        return True

    def placeWallVertical(self, x, y):
        hX1 = y*2 + 1 
        hY1 = x
        hX2 = y*2 + 1 
        hY2 = x + 1

        if (self.nodes[hX1][hY1].hasWall and self.nodes[hX2][hY2].hasWall or self.nodes[y*2][x].hasWall or self.nodes[(y+1)*2][x].hasWall):
            print("[Vertical Wall] THERE IS ALREADY WALL")
            return False

        if x > self.width - 2:
            print("VERTICAL WALL X OVERFLOW.") 
            return False

        if y*2 > self.height - 3:
            print("VERTICAL WALL Y OVERFLOW.") 
            return False

        x1 = y*2
        y1 = x
        x2 = y*2 + 2
        y2 = x 
        self.nodes[x1][y1].hasWall = True
        self.nodes[x2][y2].hasWall = True

        return True

    def playTurn(self, player, pawn, dir, steps, wallColor, wallX, wallY):
        playerIndex = (0 if player == 'X' else 2) + pawn-1
        wallIndex = 0 if player == 'X' else 1
        playerMoved = self.movePlayer(dir, steps, playerIndex)
        
        wallPlaced = False
        noWallsLeft = False
        if not playerMoved:
            print("Unable to move player!")
            return False
        if wallColor == 'G':
            if self.walls[wallIndex][0] > 0:
                wallPlaced = self.placeWallVertical(wallX - 1, wallY - 1)
                if wallPlaced:
                    self.walls[wallIndex][0] -= 1
                    print(self.walls)
            else:
                print(f"[Player {playerIndex+1}] No green walls left.")
                noWallsLeft = True
        elif wallColor == 'B':
            if self.walls[wallIndex][1] > 0:
                wallPlaced = self.placeWallHorizontal(wallX - 1, wallY - 1)
                if wallPlaced:
                    self.walls[wallIndex][1] -= 1
                    print(self.walls)
            else:
                print(f"[Player {playerIndex+1}] No blue walls left.")
                noWallsLeft = True
        if (not wallPlaced or noWallsLeft) and playerMoved:
            self.movePlayer(10 - dir, steps, playerIndex)
            return False
        return True

    def isEnd(self):
        if self.players[0].checkForEnd(self.startNodes[2:3]) or self.players[1].checkForEnd(self.startNodes[2:3]):
            print("X HAS WON!")
        elif self.players[2].checkForEnd(self.startNodes[0:1]) or self.players[3].checkForEnd(self.startNodes[0:1]):
            print("O HAS WON!")
            