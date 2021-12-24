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