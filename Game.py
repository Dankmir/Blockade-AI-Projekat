from Board import Board
from colorama import *
import copy
import os

class Game:
    def __init__(self, w, h, startPositions, numOfWalls, playerSymbol):
        self.clearConsole()

        self.width = w
        self.height = h
        self.states = []
        self.states.append(Board(w, h, startPositions, numOfWalls, playerSymbol))
        self.playerSymbol = playerSymbol
        self.draw()

    def initialize(self):
        self.clearConsole()

        startPositions = []

        print("Izaberite igraca")
        playerSymbol = self.getInputString("X ili O: ", ['X', 'O'])

        print("Izaberite velicinu table, preporuceno je 14x11 a maksimalno dozvoljeno 28x22")
        n = self.getInput("Broj vrsta table: ", 14, 28)
        m = self.getInput("Broj kolona table: ", 11, 22)

        numOfWalls = self.getInput("Izaberite broj zidova (preporuceno je 9 a maksimalno 18): ", 9, 18)

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

    def startGame(self):
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
            self.playerSymbol = 'O' if self.playerSymbol == 'X' else 'X'
            self.draw()
            self.states[-1].getWallsLeft()
            if self.isEnd():
                break

    def getInputString(self, text, possibleStrings):
        inp = input(text)
        while inp not in possibleStrings:
            print(Fore.RED + f"Invalid input. ( range{[x for x in possibleStrings]} )" + Style.RESET_ALL)
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