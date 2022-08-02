class ParentClass:
    def printHello(self):
        print("Witaj, swiecie!")


class ChildClass(ParentClass):
    def someNewMethod(self):
        print("Obiekty klasy ParentClass nie maja tej metody.")


class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print("Te metode maja tylko obiekty klasy GrandchildClass.")


print("Utworz obiket klasy parent i wywolaj jego metode")
parent = ParentClass()
parent.printHello()

print("Utworz obiekt klasy ChildClass i wywolaj jego metode")
child = ChildClass()
child.printHello()
child.someNewMethod()

print("Utworz obiekt klasy GrandchildClass i wywolaj jego metode")
grandChild = GrandchildClass()
grandChild.printHello()
grandChild.someNewMethod()
grandChild.anotherNewMethod()

print("Blad: ")
parent.someNewMethod()
