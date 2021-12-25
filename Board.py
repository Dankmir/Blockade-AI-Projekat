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
        self.height = h
        self.startNodes = startPositions
        self.walls = [[numOfWalls, numOfWalls], [numOfWalls, numOfWalls]]
        self.nodes = []
        self.graph = dict()

        self.initializeBoardGraph()


    def initializeBoardGraph(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0:
                    if j == 0:
                        self.graph[(i, j)] = [ (i, j+1), (i+1, j), (i+1, j+1) ]
                    elif j == self.width - 1:
                        self.graph[(i, j)] = [ (i, j-1), (i+1, j), (i+1, j-1) ]
                    else:
                        self.graph[(i, j)] = [ (i, j-1), (i+1, j-1), (i+1, j), (i+1, j+1), (i, j+1) ]
                elif i == self.height - 1:
                    if j == 0:
                        self.graph[(i, j)] = [ (i, j+1), (i-1, j), (i-1, j+1) ]
                    elif j == self.width - 1:
                        self.graph[(i, j)] = [ (i, j-1), (i-1, j), (i-1, j-1) ]
                    else:
                        self.graph[(i, j)] = [ (i, j-1), (i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1) ]
                elif j == 0:
                    self.graph[(i, j)] = [ (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j) ]
                elif j == self.width-1:
                    self.graph[(i, j)] = [ (i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1), (i+1, j) ]
                else:
                    self.graph[(i, j)] = [  (i-1, j-1), (i-1, j),  (i-1, j+1),
                                            (i,   j-1), (i,   j),  (i,   j+1),
                                            (i+1, j-1), (i+1, j),  (i+1, j+1)  ]

    def checkGraphConnection(self, p1, p2):
        return (p2[0], p2[1]) in self.graph[(p1[0], p1[1])]

    def draw(self):
        c = 0
        print('    ', end='')
        print(*self.symbols[:self.width], sep='   ')
        print(*[('  ┏━' if i == 0 else '━━┓' if i == self.width else '━━┳━') for i in range(self.width + 1)], sep='')
        
        n = self.width
        keys = list(self.graph.keys())
        graph = [keys[i * n:(i + 1) * n] for i in range((len(self.graph.keys()) + n - 1) // n )]
        
        for index, row in enumerate(graph):
            l = [((self.getFieldSymbol(node) + self.getWallSymbol(node, 0, 1, '┃'))) for i, node in enumerate(row)]
            l.insert(0, ' ┃')
            l.insert(0, self.symbols[c])
            l.append(' ' + self.symbols[c])
            print(*l, sep='')

            if index != self.height-1:
                l = [((self.getWallSymbol(node, 1, 0, '━━━')+('╋'if i < self.width-1 else ''))) for i, node in enumerate(row)]
                l.insert(0, '  ┣')
                l.append('┫  ')
                print(*l, sep='')
                c += 1

        print(*[('  ┗━' if i == 0 else '━━┛' if i == self.width else '━━┻━') for i in range(self.width + 1)], sep='')
        print('    ', end='')
        print(*self.symbols[:self.width], sep='   ')

    def getWallSymbol(self, node, x, y, symbol):
        hasConnection = self.checkGraphConnection(node, (node[0] + x, node[1] + y))
        inBoard = node[0] + x >= 0 and node[0] + x < self.height-1 and node[1] + y >= 0 and node[1] + y <= self.width-1
        return (Style.DIM if hasConnection or not inBoard else Fore.GREEN if x == 0 else Fore.CYAN) + symbol + Style.RESET_ALL

    def getFieldSymbol(self, node):
        return '   '    

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
        if not self.checkGraphConnection((x, y), (x+1, y)) or not self.checkGraphConnection((x, y), (x+1, y+1)) or not self.checkGraphConnection((x, y+1), (x+1, y+1)):
            print("There is already a wall")
            return

        self.removeGraphConnectionsHorizontal(x, y)
      
    def placeWallVertical(self, x, y):
        if not self.checkGraphConnection((x, y), (x, y+1)) or not self.checkGraphConnection((x, y), (x+1, y+1)) or not self.checkGraphConnection((x+1, y), (x+1, y+1)):
            print("There is already a wall")
            return

        self.removeGraphConnectionsVertical(x, y)

    def removeGraphConnectionsHorizontal(self, x, y):
        if (x+1, y) in self.graph[(x, y)]:
            self.graph[(x, y)].remove((x+1, y))
            self.graph[(x+1 , y)].remove((x, y))

        if (x+1, y+1) in self.graph[(x, y)]:
            self.graph[(x, y)].remove((x+1, y+1))
            self.graph[(x+1, y+1)].remove((x, y))

        if (x+1, y) in self.graph[(x, y+1)]:
            self.graph[(x, y+1)].remove((x+1, y))
            self.graph[(x+1, y)].remove((x, y+1))

        if (x+1, y+1) in self.graph[(x, y+1)]:
            self.graph[(x, y+1)].remove((x+1, y+1))
            self.graph[(x+1, y+1)].remove((x, y+1))

    def removeGraphConnectionsVertical(self, x, y):
        if (x, y+1) in self.graph[(x, y)]:
            self.graph[(x, y)].remove((x, y+1))
            self.graph[(x , y+1)].remove((x, y))

        if (x+1, y+1) in self.graph[(x, y)]:
            self.graph[(x, y)].remove((x+1, y+1))
            self.graph[(x+1, y+1)].remove((x, y))

        if (x, y+1) in self.graph[(x+1, y)]:
            self.graph[(x+1, y)].remove((x, y+1))
            self.graph[(x , y+1)].remove((x+1, y))

        if (x+1, y+1) in self.graph[(x+1, y)]:
            self.graph[(x+1, y)].remove((x+1, y+1))
            self.graph[(x+1, y+1)].remove((x+1, y))

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