from Node import Node
from Player import Player

class Board:
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R' ]

    def __init__(self, w, h):
        self.players = [Player('X', 2, 4), Player('O', 6, 6)]
        self.width = w 
        self.height = h * 2
        self.nodes = []

        for i in range(self.height):
            self.nodes.append([])
            for j in range(self.width):
                self.nodes[i].append(Node(i, j, '   │' if i % 2 == 0 else '───┼')) 
                

    def draw(self):
        top = [f'  {self.symbols[i]} ' for i in range(self.width)]
        top.insert(0, '  ')
        print(*top, sep='')
        print(*['  ╔═══' if i == 0 else '═══' if i > 0 and i < self.width-1 else '═══╗' for i in range(self.width)], sep='╤')
        
        counter = 0
        for i in range(self.height):
                l = [x.s for x in self.nodes[i]]
                if i < self.height - 1:
                    l.insert(0, f'{self.symbols[counter]} ║' if i % 2 == 0 else '  ╟')
                    l.pop()
                    last = '   ║' if i % 2 == 0 else '───╢'
                    if l[len(self.nodes[i]) - 1] == '━━━┼':
                        last = '━━━╢';
                    l.append(last)
                    print(*l, sep='')

                    if i%2 == 0:
                        counter += 1

        print(*['  ╚═══' if i == 0 else '═══' if i > 0 and i < self.width-1 else '═══╝' for i in range(self.width)], sep='╧')

    def placePlayer(self, x, y, player):
        self.nodes[y * 2][x].s = f' {self.players[player].symbol} │'

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
        self.nodes[x1][y1].s = '━━━┼'
        self.nodes[x1][y1].hasWall = True
        self.nodes[x2][y2].s = '━━━┼'
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
        self.nodes[x1][y1].s = '   ┇'
        self.nodes[x1][y1].hasWall = True
        self.nodes[x2][y2].s = '   ┇'
        #self.draw()