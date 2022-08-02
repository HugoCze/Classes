class ClassWithBadProperty:
    def __init__(self):
        self.someAttribute = 'jakas poczatkowa wartosc'

    @property
    def someAttribute(self):  # To jest metoda gettera.
        # Zapomnielisly o znaku_ w self._someAttribute co spowodowało
        # uzycie wlasciwosci i ponowne wywolanie metody gettera.
        return self.someAttribute  # Ta instrukcja ponownie wywoluje getter!

    @someAttribute.setter
    def someAttribute(self, value):  # To jest metoda "settera".
        self._someAttrobute = value


obj = ClassWithBadProperty()
print(obj.someAttribute)  # Blad poniwaz getter jeszcze raz wywoluje getter
