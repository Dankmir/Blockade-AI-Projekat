from Board import Board
from colorama import *
import copy
import os
import time
import random

class Game:
    def __init__(self):
        self.clearConsole()
        
        startPositions = []

        print("Izaberite igraca")
        playerSymbol = self.getInputString("X ili O: ", ['X', 'O'])

        print("Izaberite velicinu table, preporuceno je 11x14 a maksimalno dozvoljeno 22x28")
        m = self.getInput("Broj kolona table: ", 3, 22)
        n = self.getInput("Broj vrsta table: ", 3, 28)

        numOfWalls = self.getInput("Izaberite broj zidova (preporuceno je 9 a maksimalno 18): ", 1, 18)

        print("Izaberite pocetna polja pesaka")

        print("Prvi pesak igraca X")
        x = self.getInput("x = ", 1, n)
        y = self.getInput("y = ", 1, m)
        startPositions.append([x - 1, y - 1])

        print("Drugi pesak igraca X")
        x = self.getInput("x = ", 1, n)
        y = self.getInput("y = ", 1, m)
        startPositions.append([x - 1, y - 1])

        print("Prvi pesak igraca O")
        x = self.getInput("x = ", 1, n)
        y = self.getInput("y = ", 1, m)
        startPositions.append([x - 1, y - 1])

        print("Drugi pesak igraca O")
        x = self.getInput("x = ", 1, n)
        y = self.getInput("y = ", 1, m)
        startPositions.append([x - 1, y - 1])

        self.width = m
        self.height = n
        self.states = []
        self.states.append(Board(m, n, startPositions, numOfWalls, playerSymbol))
        self.playerSymbol = playerSymbol
        self.turn = 'X'
        self.aiMovementMoves = self.generateMovementMoves()
        self.aiWallPlacementPositions = self.generateWallMoves()
        
        self.clearConsole()
        self.draw()

    def start(self):
        while True:
            turn = False
            while not turn and self.turn == self.playerSymbol:
                pawnID    = self.getInput("Unesite sa kojim pionom hoćete da igrate: ", 1, 2)
                direction = self.getInput("Unesite smer kretanja: ", 1, 9)
                steps     = self.getInput("Unesite broj koraka: ", 1, 2) if direction not in [7, 9, 1, 3] else 1
                wall      = self.getInputString("Boja zida koji se postavlja (B ili G): ", ['B', 'G'])
                wallX     = self.getInput("Unesite broj reda u kom želite da smestite zid: ", 1, self.height)
                wallY     = self.getInput("Unesite broj kolone u kojoj želite da smestite zid: ", 1, self.width)

                turn = self.playTurn(self.playerSymbol, pawnID, direction, steps, wall, wallX, wallY)
                if turn:
                    self.removeWallMove(wallX, wallY)
                    self.turn = 'O' if self.turn == 'X' else 'X'
                    
            self.clearConsole()

            # self.playerSymbol = 'O' if self.playerSymbol == 'X' else 'X'
            
            print(f'Minimax started...')
            start   = time.time()
            result  = self.minimax(self.states[-1], 2, -99999999, 99999999, self.playerSymbol == 'O')
            end     = time.time()
            print(f'Minimax finished in {end - start} seconds with result {result[0]}.')

            self.states.append(result[1])
            self.draw()
            self.states[-1].getWallsLeft()
            self.removeWallMove(self.states[-1].lastMovePlayed[5], self.states[-1].lastMovePlayed[6])
            self.turn = 'O' if self.turn == 'X' else 'X'

            if self.isEnd():
                break

    def getInputString(self, text, possibleStrings):
        inp = input(text)
        while inp not in possibleStrings:
            print(Fore.RED + f"Invalid input. ( range{possibleStrings} )" + Style.RESET_ALL)
            inp =  input(text)
        return inp

    def getInput(self, text, min, max):
        inp = int(input(text))
        while inp < min or inp > max:
            print(Fore.RED + f"Invalid input. ( range[{min}, {max}] )" + Style.RESET_ALL)
            inp =  int(input(text))
        return inp

    def playTurn(self, player, pawn, dir, steps, wallColor, wallX, wallY):
        new_board = copy.deepcopy(self.states[-1])
        played = new_board.playTurn(player, pawn, dir, steps, wallColor, wallX, wallY)
        if (played):
            self.states.append(new_board)
            return True
        return False

    def generateStates(self, state, player):
        start = time.time()
        states = []
        for pawn in range(1, 3):
            for dir in range(1, 10):
                for wallColor in ['B', 'G']:
                    for wallX in range(1, self.height+1):
                        for wallY in range(1, self.width+1):
                            new_state = copy.deepcopy(state)
                            played = new_state.playTurn(player, pawn, dir, 1, wallColor, wallX, wallY)
                            if played:
                                # new_state.draw()
                                states.append(new_state)
        
        end = time.time()
        print(f'Successfuly generated {len(states)} states in {end-start} seconds.');
        return states

    def draw(self):
        self.states[-1].draw()

    def isEnd(self):
        return self.states[-1].isEnd()

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        os.system(command)

    def generateMovementMoves(self):
        moves = []
        for pawn in [1, 2]:
            for dir in [1, 2, 3, 4, 6, 7, 8, 9]:
                moves.append((pawn, dir))
        return moves

    def generateWallMoves(self):
        moves = []
        for wallX in range(1, self.height):
            for wallY in range(1, self.width):
                moves.append((wallX, wallY))
        return moves

    def removeWallMove(self, x, y):
        if (x, y) in self.aiWallPlacementPositions:
            self.aiWallPlacementPositions.remove((x, y))
    
    def generateMove(self, player):
        wallsLeft = self.states[-1].walls[0 if player == 'X' else 1]
        for movement in self.aiMovementMoves:
            if wallsLeft[0] > 0 or wallsLeft[1] > 0:
                if wallsLeft[1] > 0:
                    for wallPos in self.aiWallPlacementPositions:
                        yield (movement[0], movement[1], 'B', wallPos[0], wallPos[1])
                else:
                    yield (movement[0], movement[1], 'B', 1, 1)
                if wallsLeft[0] > 0:
                    for wallPos in self.aiWallPlacementPositions:
                        yield (movement[0], movement[1], 'G', wallPos[0], wallPos[1])
                else:
                    yield (movement[0], movement[1], 'G', 1, 1)
            else:
                yield (movement[0], movement[1], 'B', 1, 1)

    def minimax(self, state, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.isEnd():
            return (random.randrange(-100, 100), copy.deepcopy(state))

        if maximizingPlayer:
            maxEval = -99999999
            for move in self.generateMove('X'):   
                new_state = copy.deepcopy(state)
                if new_state.playTurn('X', move[0], move[1], 1, move[2], move[3], move[4]):            
                    eval = self.minimax(new_state, depth - 1, alpha, beta, False)
                    maxEval = max(maxEval, eval[0])
                    if maxEval == eval[0]:
                        out_state = copy.deepcopy(new_state)
                    alpha = max(alpha, eval[0])
                    if beta <= alpha:
                        break;
            return (maxEval, out_state)
        else:
            minEval = 99999999
            for move in self.generateMove('O'):   
                new_state = copy.deepcopy(state)
                if new_state.playTurn('O', move[0], move[1], 1, move[2], move[3], move[4]):            
                    eval = self.minimax(new_state, depth - 1, alpha, beta, True)
                    minEval = min(minEval, eval[0])
                    if minEval == eval[0]:
                        out_state = copy.deepcopy(new_state)
                    beta = min(beta, eval[0])
                    if beta <= alpha:
                        break;
            return (minEval, out_state)