from re import purge
import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)
print(purse)
print("G:", purse.galleons, "S:", purse.sickles, "K:", purse.knuts)
print("Całkowita wartość: ", purse.value())
print("Waga: ", purse.weightInGrams(), "grama")
print()
coinJar = wizcoin.WizCoin(13, 0, 0)
print(coinJar)
print("G:", coinJar.galleons, "S:", coinJar.sickles, "K:", coinJar.knuts)
print("Całkowita wartość: ", coinJar.value())
print("Waga: ", coinJar.weightInGrams(), "grama")

