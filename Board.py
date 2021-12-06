from Node import Node

class Board:
    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'  ]

    def __init__(self, w, h):
        self.width = w 
        self.height = h * 2
        self.nodes = []

        for i in range(self.height):
            self.nodes.append([])
            for j in range(self.width):
                self.nodes[i].append(Node(i, j, '    |' if i % 2 == 0 else '---  ')) 
                

    def draw(self):
        for i in range(self.height):
                print(*[x.s for x in self.nodes[i]]) #f'({self.nodes[i][j].x}, {self.nodes[i][j].y})'
