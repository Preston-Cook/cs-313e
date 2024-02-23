import itertools


class VendingMachine:

    def __init__(self) -> None:
        self.condiments = []
        self.beverages = []
        return

    def display_menu():
        ...


class Menu:
    def __init__(self):
        self.beverages = [cls for cls in Beverage.__subclasses__()]
        self.condiments = [cls for cls in Condiment.__subclasses__()]

    def display(self):
        formatted_beverages = '\n'.join(self.beverages)
        formatted_condiments = '\n'.join(self.condiments)
        return f'''
Beverages:
{formatted_beverages}

Condiments:
{formatted_condiments}
'''


class Condiment:
    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = price
        return

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> str:
        return self.__price

    def __str__(self) -> str:
        return f'Name: {self.name}, Price: {self.price}'


class Milk(Condiment):
    __PRICE = 0.15
    __NAME = 'Milk'

    def __init__(self) -> None:
        super().__init__(self, Milk.__NAME, Milk.__PRICE)
        return


class Sugar(Condiment):
    __PRICE = 0.10
    __NAME = 'Sugar'

    def __init__(self) -> None:
        super().__init__(Sugar.__NAME, Sugar.__PRICE)
        return


class Beverage:
    def __init__(self, name: str, base_price: float) -> None:
        self.__name = name
        self.__BASE_PRICE = base_price
        self.__total_price = base_price
        self.__condiments: list[Milk | Sugar] = []
        self.__num_condiments = 0
        return

    def add_condiment(self, condiment: Milk | Sugar) -> None:
        if self.num_condiments == 3:
            raise Exception('Condiment Max Exceeded')

        self.condiments.append(condiment)
        self.total_price += condiment.price
        self.num_condiments += 1
        return

    def get_price(self) -> float:
        return self.total_price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def base_price(self) -> float:
        return self.__BASE_PRICE

    @property
    def total_price(self) -> float:
        return self.__total_price

    @property
    def condiments(self) -> list[Milk | Sugar]:
        return self.__condiments

    @property
    def num_condiments(self) -> int:
        return self.__num_condiments

    def __str__(self) -> str:
        return f''


class RegularCoffee(Beverage):
    BASE_PRICE = 1.10
    __NAME = 'Regular Coffee'

    def __init__(self) -> None:
        super().__init__(RegularCoffee.__NAME, RegularCoffee.BASE_PRICE)
        return


class Espresso(Beverage):
    BASE_PRICE = RegularCoffee.BASE_PRICE * 1.2
    __NAME = 'Espresso'

    def __init__(self) -> None:
        super().__init__(Espresso.__NAME, Espresso.BASE_PRICE)
        return


class Capuccino(Beverage):
    BASE_PRICE = Espresso.BASE_PRICE * 1.15
    __NAME = 'Capuccino'

    def __init__(self) -> None:
        super().__init__(Capuccino.__NAME, Capuccino.BASE_PRICE)
        return

    # overload method from parent class
    def add_condiment(self, condiment: Milk | Sugar) -> None:
        # TODO
        ...


def main():
    """Main Function for Program"""
    ...


if __name__ == '__main__':
    main()
