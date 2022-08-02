
import copy
from tkinter import ALL
from tkinter.tix import Tree


ALL_SPACES = list('123456789')  # Klucze slownika planszy kik
X, O, BLANK = 'X', 'O', ' '  # Stale reprezentujace wartosci tekstowe


def main():
    """ Rozgrywka w kolko i krzyzyk """
    print("Witaj w grze kolko i krzyzyk.")

    # if input("Uzyc wersji miniplanszy? T/N: ").lower().startswith('t'):
    #     gameBoard = MiniBoard()
    # else:
    #     gameBoard = HintBoard()  # Stworz obiekt planszy KIK

    gameBoard = HybridBoard()

    currentPlayer, nextPlayer, = X, O  # X wykonuje ruch jako pierwszy O jako nastepny

    while True:
        print(gameBoard.getBoardStr())  # Wyswietl plansze na ekranie

        # Zadaj graczowi pytanie, az wprowadzi prawidlowa liczbe od 1 do 9
        move = None
        while not gameBoard.isValidSpace(move):
            print(f'Jaki jest ruch gracza {currentPlayer}? (1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer)  # wykonaj ruch

        if gameBoard.isWinner(currentPlayer):  # Sprawdzenie kto wygral
            print(gameBoard.getBoardStr())
            print(currentPlayer + ' wygral!')
            break
        elif gameBoard.isBoardFull():  # Sprawdzenie remisu
            print(gameBoard.getBoardStr())
            print('Gra zakonczyla sie remisem!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # zmiana gracza
    print('Dziekuje za gre!')


class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Tworzy nowa pusta plansze do gry w kolko i krzyzyk."""
        self._spaces = {}  # Plansza jest reprezentowana przez słownik Python
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # Na poczatku wszystkie pola sa puste

    def getBoardStr(self):
        """Zwraca tekstowa reprezentacje planszy"""
        return f"""
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
        -+-+-
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
        -+-+-
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9"""

    def isValidSpace(self, space):
        """Zwraca true, jeśli space jest prawidłowym numerem pola na planszy i pole na planszy jest puste"""
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        """Zwraca True, jesli gracz jest zwyciezca tej planszy KIK"""
        s, p = self._spaces, player
        # Sprawdz czy wystepuja trzy znaki w wierszach, kolumnach i po przekatnych
        return ((s['1'] == s['2'] == s['3'] == p) or  # poziomo na gorze
                (s['4'] == s['5'] == s['6'] == p) or  # poziomo na srodku
                (s['7'] == s['8'] == s['9'] == p) or  # poziomo u dolu
                (s['1'] == s['4'] == s['7'] == p) or  # pionowo u lewej
                (s['2'] == s['5'] == s['8'] == p) or  # pionowo w srodku
                (s['3'] == s['6'] == s['9'] == p) or  # pionowo z prawej
                (s['3'] == s['5'] == s['7'] == p) or  # przekatna 1
                (s['1'] == s['5'] == s['9'] == p))  # przekatna 2

    def isBoardFull(self):
        """Zwraca True jesli wszystkie pola na planszy sa zajete"""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # Jesli nawet jedno pole jest puste zwracaj False
        return True

    def updateBoard(self, space, player):
        """Ustawia pole na planszy na podany znak"""
        self._spaces[space] = player


class MiniBoard(TTTBoard):

    def getBoardStr(self):
        """Zwraca tekstowa reprezentacje mniejszej wersji planszy"""
        # Zastap puste pola znakiem'.'
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                self._spaces[space] = '.'

        boardStr = f"""
            {self._spaces['1']}{self._spaces['2']}{self._spaces['3']} 123
            {self._spaces['4']}{self._spaces['5']}{self._spaces['6']} 456
            {self._spaces['7']}{self._spaces['8']}{self._spaces['9']} 789"""

        # Zastap znak '.' ponownie pustymi polami.
        for space in ALL_SPACES:
            if self._spaces[space] == '.':
                self._spaces[space] = BLANK
        return boardStr


class HintBoard(TTTBoard):
    def getBoardStr(self):
        """Zwraca tekstowa reprezentacje planszy z podpowiedziami."""
        boardStr = super().getBoardStr()  # wywolaj metode getBoardStr() klasy TTTBoard

        xCanWin = False
        oCanWin = False
        orginalSpaces = self._spaces  # Przechowaj _spaces
        for space in ALL_SPACES:  # Sprawdzaj wszytkie pola:
            # Symuluj ruch X dla tego pola:
            self._spaces = copy.copy(orginalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.isWinner(X):
                xCanWin = True
            # Symuluj ruch O dla tego pola:
            self._spaces = copy.copy(orginalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.isWinner(O):
                oCanWin = True
        if xCanWin:
            boardStr += '\nGracz X moze wygrac po jednym dodatkowym ruchu.'
        if oCanWin:
            boardStr += '\nGracz O moze wygrac po jednym dodatkowym ruchu.'
        self._spaces = orginalSpaces
        return boardStr


class HybridBoard(HintBoard, MiniBoard):
    pass


if __name__ == '__main__':
    main()
