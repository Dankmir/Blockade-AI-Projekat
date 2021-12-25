from Board import Board
import copy

class Game:
    def __init__(self, w, h, startPositions, numOfWalls, whoPlaysFirst):
        self.states = []
        self.states.append(Board(w, h, startPositions, numOfWalls, whoPlaysFirst))

    def playTurn(self, player, pawn, dir, steps, wallColor, wallX, wallY):
        new_board = copy.copy(self.states[-1])
        played = new_board.playTurn(player, pawn, dir, steps, wallColor, wallX, wallY)
        if (played):
            self.states.append(new_board)

    def draw(self):
        self.states[-1].draw()

    def placeWallVertical(self, x, y):
        self.states[-1].placeWallVertical(x-1, y-1)

    def placeWallHorizontal(self, x, y):
        self.states[-1].placeWallHorizontal(x-1, y-1)