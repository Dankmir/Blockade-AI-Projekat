class Player:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.walls = 0

    def setPlayerPos(self, x, y):
            self.x = x
            self.y = y

    def move(self, dir, distance, boardWidth, boardHeight):
        if distance <= 0 or distance > 2:
            print("INVALID DISTANCE")
            return False
        prevX = self.x
        prevY = self.y

        if dir == 0:
            self.x += distance
        elif dir == 1:
            self.y += distance
        elif dir == 2:
            self.x -= distance
        elif dir == 3:
            self.y -= distance

        if self.validateMove(self.x, self.y, boardWidth, boardHeight) == False:
            self.x = prevX  
            self.y = prevY 
            return False
        return True

    def validateMove(self, x, y, boardWidth, boardHeight):
        if x * 2 >= boardHeight or x < 0 or y >= boardWidth or y < 0:
            print("INVALID MOVE")
            return False
        return True