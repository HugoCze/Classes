import wizcoin


class WizardCustomer:
    def __init__(self, name):
        self.name = name
        self.purse = wizcoin.WizCoin(9, 14, 34)


wizard = WizardCustomer("Alicja")
print(f'{wizard.name} ma kwote {wizard.purse.value()} knutow.')
print(
    f'Waga monet nalezacych od {wizard.name} wynosi {wizard.purse.weightInGrams()} gramow.')
