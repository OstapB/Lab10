from builtins import staticmethod


class MuseumSculpture:
    amount_of_sculptures = 0

    def __init__(self, year_of_foundation=1768, name="Cisar", material="clay", height=200, price=17500):
        self.year_of_foundation = year_of_foundation

        self.name = name
        self.material = material
        self.height = height
        self.price = price

    def __del__(self):
        print("Destructor " + self.name + " deleted")

    def __repr__(self):
        return str(self.__dict__)


@staticmethod
def output_static_field():
    return MuseumSculpture.amount_of_sculptures
