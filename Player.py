from colorama import *

class Player:
    def __init__(self, symbol, pos, board):
        self.symbol = symbol
        self.x = pos[0]
        self.y = pos[1]
        self.walls = 0
        self.board = board

    def setPlayerPos(self, x, y):
            self.x = x
            self.y = y

    def move(self, dir, distance, boardWidth, boardHeight):
        if distance <= 0 or distance > 2:
            print("INVALID DISTANCE")
            return False
            
        tempX = self.x
        tempY = self.y

        i = 0
        while i < distance:
            i += 1
            if dir == 2: # N
                tempX += 1 
                if self.hasWallNorth(tempX, tempY):
                    return False  
            elif dir == 6: # E
                tempY += 1
                if self.hasWallEast(tempX, tempY):
                    return False  
            elif dir == 8: # S
                tempX -= 1
                if self.hasWallSouth(tempX, tempY):
                    return False  
            elif dir == 4: # W
                tempY -= 1
                if self.hasWallWest(tempX, tempY):
                    return False  
            elif dir == 1: # NW
                if not self.hasWallNorth(tempX + 1, tempY) and not self.hasWallWest(tempX + 1, tempY - 1) or not self.hasWallWest(tempX, tempY - 1) and not self.hasWallNorth(tempX + 1, tempY - 1):
                    tempX += 1
                    tempY -= 1
                    i = distance
                else:
                    return False
            elif dir == 3: # NE
                if not self.hasWallNorth(tempX + 1, tempY) and not self.hasWallEast(tempX + 1, tempY + 1) or not self.hasWallEast(tempX, tempY + 1) and not self.hasWallNorth(tempX + 1, tempY + 1):
                    tempX += 1
                    tempY += 1
                    i = distance
                else:
                    return False
            elif dir == 9: # SE
                if not self.hasWallSouth(tempX - 1, tempY) and not self.hasWallEast(tempX - 1, tempY + 1) or not self.hasWallEast(tempX, tempY + 1) and not self.hasWallSouth(tempX - 1, tempY + 1):
                    tempX -= 1
                    tempY += 1
                    i = distance
                else:
                    return False
            elif dir == 7: # SW
                if not self.hasWallSouth(tempX - 1, tempY) and not self.hasWallWest(tempX - 1, tempY - 1) or not self.hasWallWest(tempX, tempY - 1) and not self.hasWallSouth(tempX - 1, tempY - 1):
                    tempX -= 1
                    tempY -= 1
                    i = distance
                else:
                    return False

        if self.validateMove(tempX, tempY, boardWidth, boardHeight):
            self.x = tempX  
            self.y = tempY
            return True 
        return False

    def hasWallNorth(self, x, y):
        return self.board.nodes[x*2 - 1][y].hasWall 
    
    def hasWallEast(self, x, y):
        return self.board.nodes[x*2][y - 1].hasWall  
    
    def hasWallSouth(self, x, y):
        return self.board.nodes[x*2 + 1][y].hasWall  
    
    def hasWallWest(self, x, y):
        return self.board.nodes[x*2][y].hasWall  

    def validateMove(self, x, y, boardWidth, boardHeight):
        if len(list(filter(lambda a: a.x == x and a.y == y, self.board.players))) > 0:
            print("INVALID MOVE (FIELD NOT EMPTY)")
            return False    

        if x * 2 >= boardHeight or x < 0 or y >= boardWidth or y < 0:
            print("INVALID MOVE")
            return False
        return True

    def checkForEnd(self, nodes):
        for n in nodes:
            if n[0] == self.x and n[1] == self.y:
                return True
        return False