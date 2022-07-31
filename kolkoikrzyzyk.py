
ALL_SPACES = list('123456789') #Klucze slownika planszy kik
X, O, BLANK = 'X', 'O', ' ' # Stale reprezentujace wartosci tekstowe

def main():
    """ Rozgrywka w kolko i krzyzyk """
    print("Witaj w grze kolko i krzyzyk.")
    gameBoard = getBlankBoard() # Utworz Slownik Planszy kik 
    currentPlayer, nextPlayer, = X, O # X wykonuje ruch jako pierwszy O jako nastepny 
    
    while True:
        print(getBoardStr(gameBoard)) # Wyswietl plansze na ekranie 

        # Zadaj graczowi pytanie, az wprowadzi prawidlowa liczbe od 1 do 9
        move = None
        while not isValidSpace(gameBoard, move):
            print(f'Jaki jest ruch gracza {currentPlayer}? (1-9)')
            move = input()
        updateBoard(gameBoard, move, currentPlayer) # Wykoananie ruchu 

        if isWinner(gameBoard, currentPlayer): #Sprawdzenie kto wygral
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' wygral gre!')
            break
        elif isBoardFull(gameBoard): #Sprawdzenie remisu
            print(getBoardStr(gameBoard))
            print('Gra zakonczyla sie remisem!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer # zmiana gracza
    print('Dziekuje za gre!')

def getBlankBoard():
        """Tworzy nowa pusta plansze gry w kolko i krzyzyk"""
        board = {} # Plansza jest reprezentowana przez slownik Pythona.
        for space in ALL_SPACES:
            board[space] = BLANK # Wszystkie pola na poczatku są puste.
        return board

def getBoardStr(board):
        """Zwraca tekstowa reprezentacje planszy"""
        return f'''
        {board['1']}|{board['2']}|{board['3']} 1 2 3
        -+-+-
        {board['4']}|{board['5']}|{board['6']} 4 5 6     
        -+-+-
        {board['7']}|{board['8']}|{board['9']} 7 8 9'''

def isValidSpace(board, space):
        """Zwraca True jest pole na planszy ma prawidlowy numer i pole jest puste"""
        if space is None:
            return False
        return space in ALL_SPACES or board[space] == BLANK

def isWinner(board, player):
        """Zwraca True jest gracz jest zwyciezca planszy kik"""
        b, p = board, player # krotsze nazwy jako skladniowy cukier
        # Sprawdzenie czy trzy takie same znaki wystepuja w wierszach, kolumnach i po przekatnych.
        return ((b['1'] == b['2'] == b['3'] == p) or #poziomo na gorze
                (b['4'] == b['5'] == b['6'] == p) or #poziomo na srodku
                (b['7'] == b['8'] == b['9'] == p) or #poziomo u dolu
                (b['1'] == b['4'] == b['7'] == p) or #pionowo u lewej
                (b['2'] == b['5'] == b['8'] == p) or #pionowo w srodku
                (b['3'] == b['6'] == b['9'] == p) or #pionowo z prawej 
                (b['3'] == b['5'] == b['7'] == p) or #przekatna 1
                (b['1'] == b['5'] == b['9'] == p)) #przekatna 2

def isBoardFull(board):
        """Zwraca True jesli wszystkie pola na planszy sa zajete"""
        for space in ALL_SPACES:
            if board[space] == BLANK:
                return False # Jeśli nawet jedno pole jest puste zwracaj falsz
        return True # Nie ma wolnych pol, zatem zwroci true
    
def updateBoard(board, space, mark):
        """Ustawia pole na planszy na podany znak"""
        board[space] = mark
    
if __name__ == '__main__':
    main() # wywołaj main(), jesli ten modul zostal uruchomiony a nie zaimporotwany 

