from colorama import *

class Player:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.walls = 0

    def setPlayerPos(self, x, y):
            self.x = x
            self.y = y

    def move(self, dir, distance, boardWidth, boardHeight, players, nodes):
        if distance <= 0 or distance > 2:
            print("INVALID DISTANCE")
            return False
        tempX = self.x
        tempY = self.y

        for i in range(distance):
            if dir == 0:
                tempX += 1 
                if nodes[tempX*2 - 1][tempY].hasWall:
                    return False  
            elif dir == 1:
                tempY += 1
                if nodes[tempX*2][tempY - 1].hasWall:
                    return False  
            elif dir == 2:
                tempX -= 1
                if nodes[tempX*2 + 1][tempY].hasWall:
                    return False  
            elif dir == 3:
                tempY -= 1
                if nodes[tempX*2][tempY].hasWall:
                    return False  

        if self.validateMove(tempX, tempY, boardWidth, boardHeight, players):
            self.x = tempX  
            self.y = tempY
            return True 
        return False

    def validateMove(self, x, y, boardWidth, boardHeight, players):
        if len(list(filter(lambda a: a.x == x and a.y == y, players))) > 0:
            print("INVALID MOVE (FIELD NOT EMPTY)")
            return False    

        if x * 2 >= boardHeight or x < 0 or y >= boardWidth or y < 0:
            print("INVALID MOVE")
            return False
        return True