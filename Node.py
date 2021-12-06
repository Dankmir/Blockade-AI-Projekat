class Node:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        self.hasWall = False
        self.neighbors = list()

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)