class Airplane:
    def flyIntheAir(self):
        print("Latam...")


class Ship:
    def floatOnTheWater(self):
        print("Plywam...")


class FlyingBoat(Airplane, Ship):
    pass
