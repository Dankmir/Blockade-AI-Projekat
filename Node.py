from colorama import *

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hasWall = False
        self.hasPlayer = False

        self.prevX = None
        self.nextX = None
        self.prevY = None
        self.nextY = None

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def getSymbol(self):
        return ((Fore.GREEN if self.hasWall else Style.DIM) + '┃' + Style.RESET_ALL) if self.x % 2 == 0 else ((Fore.CYAN if self.hasWall else Style.DIM) + '━━━' + Style.RESET_ALL)