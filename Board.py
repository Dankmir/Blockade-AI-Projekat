from Node import Node
from Player import Player
from colorama import *

class Board:
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R' ]

    def __init__(self, w, h):
        self.players = [Player('✖', 3, 3), Player('✖', 3, 7), Player('⬤', 10, 3), Player('⬤', 10, 7)]
        init()
        self.width = w 
        self.height = h * 2
        self.nodes = []

        for i in range(self.height):
            self.nodes.append([])
            for j in range(self.width):
                self.nodes[i].append(Node(i, j, (Style.DIM + '┃' + Style.RESET_ALL) if i % 2 == 0 else (Style.DIM + '━━━' + Style.RESET_ALL)))

    
    def draw(self):
        c = 0
        print('   ', end='')
        print(*self.symbols[:self.width], sep='   ')
        print(*[(' ┏━' if i == 0 else '━━┓' if i == self.width else '━━┳━') for i in range(self.width + 1)], sep='')
        for i in range(self.height - 1):
                l = [((x.s + '╋') if i % 2 != 0 else (self.getPlayerSymbol(i//2,j) + x.s)) for j,x in enumerate(self.nodes[i])]
                l.insert(0, '┃' if i % 2 == 0 else '┣')
                l.insert(0, self.symbols[c] if i % 2 == 0 else ' ')
                a = l.pop()[:-1:]
                l.append(f'{self.getPlayerSymbol(i//2,self.width-1)}┃' if i % 2 == 0 else a + '┫')
                print(*l, sep='')
                if i % 2 == 0:
                    c += 1
        print(*[(' ┗━' if i == 0 else '━━┛' if i == self.width else '━━┻━') for i in range(self.width + 1)], sep='')
        

    def getPlayerSymbol(self, x, y):
        res = list(filter(lambda a: a.x == x and a.y == y, self.players))
        if len(res) > 0:
            return f' {res.pop().symbol} '
        return '   '

    def movePlayer(self, dir, distance, player):
        self.players[player].move(dir, distance, self.width, self.height)
        
    def placeWallHorizontal(self, x, y):
        vX = y*2
        vY = x

        if (self.nodes[vX][vY].hasWall):
            print("THERE IS ALREADY WALL")
            return

        if x > self.width - 2:
            print("HORIZONTAL WALL X OVERFLOW.") 
            return

        if y*2 > self.height - 3:
            print("HORIZONTAL WALL Y OVERFLOW.") 
            return

        x1 = y*2 + 1
        y1 = x
        x2 = y*2 + 1
        y2 = x + 1  
        self.nodes[x1][y1].s = (Fore.RED + '━━━' + Style.RESET_ALL)
        self.nodes[x1][y1].hasWall = True
        self.nodes[x2][y2].s = (Fore.RED + '━━━' + Style.RESET_ALL)
        #self.draw()

    def placeWallVertical(self, x, y):
        hX = y*2 + 1 #1 
        hY = x #1 2

        if (self.nodes[hX][hY].hasWall):
            print("THERE IS ALREADY WALL")
            return

        if x > self.width - 2:
            print("VERTICAL WALL X OVERFLOW.") 
            return

        if y*2 > self.height - 3:
            print("VERTICAL WALL Y OVERFLOW.") 
            return

        x1 = y*2
        y1 = x
        x2 = y*2 + 2
        y2 = x 
        self.nodes[x1][y1].s = (Fore.GREEN + '┃' + Style.RESET_ALL)
        self.nodes[x1][y1].hasWall = True
        self.nodes[x2][y2].s = (Fore.GREEN + '┃' + Style.RESET_ALL)
        #self.draw()
