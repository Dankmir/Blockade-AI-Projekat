from Node import Node

class Board:
    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S' ]

    def __init__(self, w, h):
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
                    l.append('   ║' if i % 2 == 0 else '───╢')
                    print(*l, sep='')

                    if i%2 == 0:
                        counter += 1

        print(*['  ╚═══' if i == 0 else '═══' if i > 0 and i < self.width-1 else '═══╝' for i in range(self.width)], sep='╧')

    def placeWallHorizontal(self, x, y):
        self.nodes[y*2 + 1][x].s = '━━━┼'
        self.nodes[y*2 + 1][x + 1].s = '━━━┼'
        #self.draw()

    def placeWallVertical(self, x, y):
        self.nodes[y*2][x].s = '   ┇'
        self.nodes[y*2 + 2][x].s = '   ┇'
        #self.draw()