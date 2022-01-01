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
        m = self.getInput("Broj kolona table: ", 5, 22)
        n = self.getInput("Broj vrsta table: ", 5, 28)

        numOfWalls = self.getInput("Izaberite broj zidova (preporuceno je 9 a maksimalno 18): ", 4, 18)

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
            
            self.clearConsole()
            # self.playerSymbol = 'O' if self.playerSymbol == 'X' else 'X'
            a = self.minimax(self.states[-1], 2, -99999999, 99999999, False)
            self.states.append(a[1])
            print(f'Minimax result: {a[0]}')
            # a[1].draw()
            self.draw()
            self.states[-1].getWallsLeft()
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
                            played = new_state.playTurn('X' if player == 1 else 'O', pawn, dir, 1, wallColor, wallX, wallY)
                            if played:
                                # new_state.draw()
                                states.append(new_state)
        
        end = time.time()
        print(f'Successfuly generated {len(states)} states in {end-start} seconds.');
        return states
        # Odabir piona: 1 ili 2
        # Odabir smera: 1, 2, 3, 4, 5, 6, 7, 8 ili 9
        # Odabir zida: B ili G
        # Odabir reda za zid: 1 do height
        # Odabir kolone za zid: 1 do width

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
            return (random.randrange(-10, 10), state)
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