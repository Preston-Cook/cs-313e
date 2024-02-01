#   File : beverage.py

#   Description: Controls a Fully Automatic Beverage Vending Machine using
#                Beverage and Condiment classes & inheritance

#   Student Name: Crystal Hicks

#   Student UT EID: crh4624

#   Partner Name: Preston Cook

#   Partner UT EID: plc886

#   Course Name: CS 313E

#   Unique Number: 50775

#   Date Created: 2/1/2024

#   Date Last Modified: 2/1/2024

#   Input: User inputs the name of the beverage they want, and units of condiments to add as an int.
#   Output: Outputs the Beverage along with its added Condiments and price
    
class Beverage:
    """Manages all beverages & fetches price based on their base price and condiments"""
    price = 0
    def __init__(self, condiments):
        self.condiments = condiments

    def get_condiments_price(self):
        price = 0
        for condiment in self.condiments:
            price += condiment.get_price()
        return price

    def get_price(self):
        return self.price + self.get_condiments_price()

    def __str__(self):
        string = self.__class__.__name__ + " | ["
        # add condiments
        for condiment in self.condiments:
            string += condiment.__str__() + ", "
        string += "]\n" + "${:.2f}".format(self.get_price())
        return string

############################################################

class RegularCoffee(Beverage):
    """"""
    price = 1.10

############################################################

class Espresso(Beverage):
    """"""
    price = RegularCoffee.price + RegularCoffee.price * .2

############################################################

class Cappucchino(Beverage):
    """"""
    price = Espresso.price + Espresso.price * .15

############################################################
############################################################
        
class Condiment:
    """Manages all condiments, stores number of units and calculates price"""
    price = 0
    def __init__(self, units):
        self.units = units

    def get_price(self):
        return self.price * self.units
    
    def __str__(self):
        return self.__class__.__name__ +": " + str(self.units)

############################################################
        
class Milk(Condiment):
    """"""
    price = .15

############################################################
        
class Sugar(Condiment):
    """"""
    price = .1

############################################################


def main():
    """
    Controls the user input for the beverage machine
    """

    available_beverages = {
        "RegularCoffee": RegularCoffee,
        "Espresso": Espresso,
        "Cappucchino": Cappucchino
    }

    while True:
        for beverage in Beverage.__subclasses__():
            print(beverage.__name__, end = " | ")
        beverage_name = input("\nPlease enter the Beverage you would like: ")
        if beverage_name in available_beverages:
            beverage = available_beverages[beverage_name]
        else:
            print("Beverage not found.\n")
            continue

        beverage_condiments = []
        condiment_total_units = 0
        # determine units for each condiment and add them to list beverage_condiments if it has more than 0 units
        for condiment in Condiment.__subclasses__():

            # stops iterating through condiments if the max unit count has been reached
            if condiment_total_units == 3:
                break

            # skips milk if the beverage is not RegularCoffee or Espresso
            if condiment.__name__ == "Milk" and not (beverage_name == "RegularCoffee" or beverage_name == "Espresso"):
                print("\n")
                continue

            units = int(input("Please enter the number of " + condiment.__name__ + " you would like to add: "))

            # check for valid units value
            if units + condiment_total_units > 3:
                units = 3 - condiment_total_units
                print("Too many units. Units of " + condiment.__name__ + " locked to " + str(units))
            elif units < 0:
                units = 0
                print("Not a valid number. Units of " + condiment.__name__ + " set to 0")
            
            # add condiment to list
            if units > 0:
                beverage_condiments.append(condiment(units))
                condiment_total_units += units

        # make beverage and fetch prices
        beverage = beverage(beverage_condiments)
        print(beverage, "\n")


if __name__ == "__main__":
    main()
