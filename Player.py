class Player:
    def __init__(self, symbol, p1x, p1y, p2x, p2y):
        self.symbol = symbol
        self.positions = [[p1x, p1y], [p2x, p2y]]
        self.walls = 0

    def setPlayerPos(self, x, y, id):
        if id == 0:
            self.positions[0][0] = x
            self.positions[0][1] = y
        elif id == 1:
            self.positions[1][0] = x
            self.positions[1][1] = y

    def move(self, dir, distance, id, boardWidth, boardHeight):
        if distance <= 0 or distance > 2:
            print("INVALID DISTANCE")
            return False
        prevPos = self.positions[id].copy()

        if dir == 0:
            self.positions[id][0] += distance
        elif dir == 1:
            self.positions[id][1] += distance
        elif dir == 2:
            self.positions[id][0] -= distance
        elif dir == 3:
            self.positions[id][1] -= distance

        if self.validateMove(self.positions[id][0], self.positions[id][1], boardWidth, boardHeight) == False:
            self.positions[id] = prevPos.copy()
            return False

        return True

    def validateMove(self, x, y, boardWidth, boardHeight):
        if x >= boardWidth or x < 0 or y * 2 >= boardHeight or y < 0:
            print("INVALID MOVE")
            return False
        return True