from colorama import *

class Player:
    def __init__(self, symbol, pos, board):
        self.symbol = symbol
        self.x = pos[0]
        self.y = pos[1]
        self.board = board

    def move(self, dir, distance, boardWidth, boardHeight):
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
            
            if distance == 2:
                for n in self.board.startNodes[0:2] if self.symbol == 'O' else self.board.startNodes[2:4]:
                    if n[0] == tempX and n[1] == tempY:
                        return False

        if self.validateMove(tempX, tempY, boardWidth, boardHeight):
            self.x = tempX  
            self.y = tempY
            return True 
        return False

    def hasWallNorth(self, x, y):
        return not self.board.checkGraphConnection((x,y), (x - 1, y))
    
    def hasWallEast(self, x, y):
        return not self.board.checkGraphConnection((x,y), (x, y - 1))
    
    def hasWallSouth(self, x, y):
        return not self.board.checkGraphConnection((x,y), (x + 1, y))
    
    def hasWallWest(self, x, y):
        return not self.board.checkGraphConnection((x,y), (x, y + 1))

    def validateMove(self, x, y, boardWidth, boardHeight):
        if len(list(filter(lambda a: a.x == x and a.y == y, self.board.players))) > 0:
            if len(list(filter(lambda a: a[0] == x and a[1] == y, self.board.startNodes))) == 0:
            # print(Fore.RED + "Invalid move. (Field not empty)" + Style.RESET_ALL)
                return False    

        if x >= boardHeight or x < 0 or y >= boardWidth or y < 0:
            # print(Fore.RED + "Invalid move. (Position out of board)" + Style.RESET_ALL)
            return False
        return True

    def checkForEnd(self, nodes):
        for n in nodes:
            if n[0] == self.x and n[1] == self.y:
                return True
        return False