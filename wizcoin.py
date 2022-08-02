import collections.abc
import operator


class WizCoinException(Exception):
    """Modul wizcoin zglasza ten wyjatek w przypadku nieprawidlowego uzycia modulu"""
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Tworzy obiekt WizCoin z monetami: knutami, syklami, galeonami"""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # Uwaga: metody __init__() nigdy nie zawieraja instrukcji return

    @property
    def galleons(self):
        """Zawiera liczbe monet(galleonow) zapisanych w tym obiekcie"""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'atrybut galleons musi byc ustawiony \n na wartosc int, a nie na ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException(
                "atrybut galleons musi byc liczba dodatnia \n int a nie liczba " + value.__class__.__qualname__)
        self._galleons = value

    @property
    def knuts(self):
        """Zawiera liczbe monet(knutów) zapisanych w tym obiekcie"""
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'atrybut knuty musi byc ustawiony \n na wartosc int, a nie na ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException(
                "atrybut knuty musi byc liczba dodatnia \n int a nie liczba " + value.__class__.__qualname__)
        self._knuts = value

    @property
    def sickles(self):
        """Zawiera liczbe monet(sykli) zapisanych w tym obiekcie"""
        return self._sickles

    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'atrybut sykle musi byc ustawiony \n na wartosc int, a nie na ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException(
                "atrybut sykle musi byc liczba dodatnia \n int a nie liczba " + value.__class__.__qualname__)
        self._sickles = value

    @property
    def total(self):
        """Wartosc (w knutach) wszystkich monet w tym obiekcie WizCoin"""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def __repr__(self):
        """Zwraca ciag wyrazen, ktore odtwarza ten obiekt"""
        return f'{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})'

    def __str__(self):
        """Zwraca czytelna dla czlowieka reprezentacje obiektu"""
        return f'{self.galleons}g, {self.sickles}s, {self.knuts}k'

    def __add__(self, other):
        """Dodawanie liczby monet w dwoch obiektach WizCoin"""
        if not isinstance(other, WizCoin):
            return NotImplemented
        return WizCoin(other.galleons + self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)

    def __mul__(self, other):
        """Mnozy kwoty monet przez nieujemna liczbe calkowita"""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # Pomnozenie przez ujemna liczbe calkowita zwraca nieprawidlowa liczbe monet
            raise WizCoinException(
                'mnozenie przez ujemne liczby calkowite jest nieodzwolone')
        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def __rmul__(self, other):
        """Mnozy kwoty monet przez nieujemna liczbe calkowita"""
        return self.__mul__(other)

    def __iadd__(self, other):
        """Dodawanie kwoty z innego obiektu WizCoin do tego obiektu"""
        if not isinstance(other, WizCoin):
            return NotImplemented

        # Modyfikujemy obiket self w miejsu:
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts
        return self  # Metody dunder w miejscu prawie zawsze zwracaja self.

    def __imul__(self, other):
        """Mnozy kwoty galleonow, sykli i knotow zapisane w tym obiekcie przez nieujemna liczbe calkowita"""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException(
                'nie mozna mnozyc obiekty WizCoin przez ujemne liczby calkowite')

        # Klasa WizCoin tworzy obikety mutowalne, zatem nie tworz
        # nowych obiektow jak w ponizszym zakomentowanym kodzie:
        # return WizCoin(self.galleons * other, self.sickles * etc...)
        # Obiekt self modifikujemy w miejscu
        self.galleons *= other
        self.knuts *= other
        self.sickles *= other
        return self  # Metody dunder w miejscu prawie zawsze zwracaja self

    def _comparisonOperatorHelper(self, operatorFunc, other):
        """Metoda pomocnicza dla metody dunder porownan"""

        if isinstance(other, WizCoin):
            return operatorFunc(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operatorFunc(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            otherValue = (other[0]*17*29) + (other[1]*29) + other[2]
            return operatorFunc(self.total, otherValue)
        elif operatorFunc == operator.eq:
            return False
        elif operatorFunc == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):  # eq oznacza EQual
        return self._comparisonOperatorHelper(operator.eq, other)

    def __ne__(self, other):  # ne oznacza NotEqual
        return self._comparisonOperatorHelper(operator.ne, other)

    def __lt__(self, other):  # lt oznacza less than
        return self._comparisonOperatorHelper(operator.lt, other)

    def __le__(self, other):  # le oznacza less or equal
        return self._comparisonOperatorHelper(operator.le, other)

    def __gt__(self, other):  # gt oznacza greater than
        return self._comparisonOperatorHelper(operator.gt, other)

    def __ge__(self, other):  # ge oznacza greater than or equal
        return self._comparisonOperatorHelper(operator.ge, other)
