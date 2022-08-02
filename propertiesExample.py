from msilib.schema import Class


class ClassWithProperties:
    def __init__(self):
        self.someAttribute = "Jakas wartosc poczatkowa"

    @property
    def someAttribute(self):  # To jest metoda gettera
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value):  # To jest metoda "settera".
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self):  # to jest metod deletera
        del self._someAttribute


obj = ClassWithProperties()
print(obj.someAttribute)  # wyswietla 'jakas wartosc poczatkowa'.
obj.someAttribute = 'zmieniona wartosc'
print(obj.someAttribute)  # wyswietla 'zmieniona wartosc'
del obj.someAttribute  # Usuwa atrybut someAttribute

# obj = ClassWithRegularAttributes('jakas wartosc poczatkowa')
# print(obj.someAttribute)  # wyswietla 'jakas wartosc poczatkowa'.
# obj.someAttribute = 'wartosc zmieniona'
# print(obj.someAttribute)  # wyswietla 'wartosc zmieniona'.
# del obj.someAttribute  # usuwa atrybut someAttribute
