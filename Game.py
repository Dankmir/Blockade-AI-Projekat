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

        self.clearConsole()

        self.width = m
        self.height = n
        self.states = []
        self.states.append(Board(m, n, startPositions, numOfWalls, playerSymbol))
        self.playerSymbol = playerSymbol
        self.movesTable = self.generatePossibleMoves()
        # self.removeWallMoves()
        self.draw()

    def start(self):
        while True:
            turn = False
            while not turn:
                pawnID    = self.getInput("Unesite sa kojim pionom hoćete da igrate: ", 1, 2)
                direction = self.getInput("Unesite smer kretanja: ", 1, 9)
                steps     = self.getInput("Unesite broj koraka: ", 1, 2) if direction not in [7, 9, 1, 3] else 1
                wall      = self.getInputString("Boja zida koji se postavlja (B ili G): ", ['B', 'G'])
                wallX     = self.getInput("Unesite broj reda u kom želite da smestite zid: ", 1, self.height)
                wallY     = self.getInput("Unesite broj kolone u kojoj želite da smestite zid: ", 1, self.width)

                turn = self.playTurn(self.playerSymbol, pawnID, direction, steps, wall, wallX, wallY)
                if turn:
                    self.removeWallMove(self.states[-1].lastMovePlayed[4:7])

            self.clearConsole()

            # self.playerSymbol = 'O' if self.playerSymbol == 'X' else 'X'
            
            print(f'Minimax started...')
            start   = time.time()
            result  = self.minimax(self.states[-1], 2, -99999999, 99999999, False)
            end     = time.time()
            print(f'Minimax finished in {end - start} seconds with result {result[0]}.')


            self.states.append(result[1])
            self.draw()
            self.states[-1].getWallsLeft()
            self.removeWallMove(self.states[-1].lastMovePlayed[4:7])

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

    def placeWallVertical(self, x, y):
        self.states[-1].placeWallVertical(x-1, y-1)

    def placeWallHorizontal(self, x, y):
        self.states[-1].placeWallHorizontal(x-1, y-1)

    def checkPath(self, p1, p2):
        print(self.states[-1].checkPath(p1, p2))

    def isEnd(self):
        return self.states[-1].isEnd()

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        os.system(command)

    def minimax(self, state, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.isEnd():
            return (random.randrange(-100, 100), copy.deepcopy(state))

        if maximizingPlayer:
            maxEval = -99999999
            for move in self.movesTable:   
                new_state = copy.deepcopy(state)
                if new_state.playTurn('X', move[0], move[1], 1, move[2], move[3], move[4]):            
                    eval = self.minimax(new_state, depth - 1, alpha, beta, False)
                    maxEval = max(maxEval, eval[0])
                    if maxEval == eval[0]:
                        print(f"[Maximizing] New maxEval = {maxEval}")
                        out_state = copy.deepcopy(new_state)
                    alpha = max(alpha, eval[0])
                    if alpha == eval[0]:
                        print(f'[Maximizing] New Alpha = {alpha}')
                    if beta <= alpha:
                        print(f"[Maximizing] Pruned. Alpha = {alpha}; beta = {beta}")
                        break;
            return (maxEval, out_state)
        else:
            minEval = 99999999
            for move in self.movesTable:   
                new_state = copy.deepcopy(state)
                if new_state.playTurn('O', move[0], move[1], 1, move[2], move[3], move[4]):            
                    eval = self.minimax(new_state, depth - 1, alpha, beta, True)
                    minEval = min(minEval, eval[0])
                    if minEval == eval[0]:
                        print(f"[Minimizing] New minEval = {minEval}")
                        out_state = copy.deepcopy(new_state)
                    beta = min(beta, eval[0])
                    if beta == eval[0]:
                        print(f'[Minimizing] New Beta = {beta}')
                    if beta <= alpha:
                        print(f"[Minimizing] Pruned. Alpha = {alpha}; beta = {beta}")
                        break;
            return (minEval, out_state)

    def generatePossibleMoves(self):
        movesTable = []
        for pawn in range(1, 3):
                for dir in range(1, 10):
                    for wallColor in ['B', 'G']:
                        for wallX in range(1, self.height+1):
                            for wallY in range(1, self.width+1):
                                movesTable.append((pawn, dir, wallColor, wallX, wallY))    
        return movesTable

    def removeWallMove(self, input):
        wallMoves = list(filter(lambda x : x[2] == input[0] and x[3] == input[1] and x[4] == input[2], self.movesTable))
        for move in wallMoves:
            self.movesTable.remove(move)

    def removeWallMoves(self):
        wallMoves = list(filter(lambda x : x[2] == 'G' or (x[2] == 'B' and x[3] != 1 or x[4] != 1), self.movesTable))
        for move in wallMoves:
            self.movesTable.remove(move)
        return wallMoves

'''

    def minimax(self, state, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.isEnd():
            return (random.randrange(-10, 10), copy.deepcopy(state))
        states = [] 
        if maximizingPlayer:
            states = self.generateStates(state, 'X')
            print(f"[Maximizing] Generated states at depth: {depth}")
            maxEval = -99999999
            for s in states:
                eval = self.minimax(s, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval[0])
                if maxEval == eval[0]:
                    out_state = copy.deepcopy(s)
                alpha = max(alpha, eval[0])
                if beta <= alpha:
                    break
            return (maxEval, out_state)
        else:
            states = self.generateStates(state, 'O')
            print(f"[Minimizing] Generated states at depth: {depth}")
            minEval = 99999999
            for s in states:
                eval = self.minimax(s, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval[0])
                if minEval == eval[0]:
                    out_state = copy.deepcopy(s)
                beta = min(beta, eval[0])
                if beta <= alpha:
                    break
            return (minEval, out_state)

'''            

