"""
    File: employee.py
    Description: Defines an employee class and other subclasses
                as part of an exercise in inheritance, 
                polymorphism, abstraction, and encapsulation.
    Student Name: Preston Cook
    Student UT EID: plc886
    Partner Name: Crystal Hicks
    Partner UT EID: crh4624
    Course Name: CS 313E
    Unique Number: 50775
    Date Created: 30 January 2023
    Date Last Modified: 30 January 2023
"""


class Employee:
    """The base employee class with name, identifier, and salary attributes"""

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.identifier = kwargs.get('identifier')
        self.salary = kwargs.get('salary')

    def cal_salary(self):
        """Returns the salary for base Employee class"""
        return self.salary

    def __str__(self):
        return f'{self.__class__.__name__}\n{self.name}, {self.identifier}, {self.salary}'


############################################################
############################################################
############################################################

class PermanentEmployee(Employee):
    """ 
    A permanent employee class that inherits from the base Employee Class
    with overloaded cal_salary method and new benefits property
    """

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.benefits = kwargs.get('benefits')

    def cal_salary(self):
        """
        Calculates the salary for an instance of PermanentEmployee depending on
        the benefits property
        """
        if 'health_insurance' in self.benefits and 'retirement' in self.benefits:
            return self.salary * 0.7
        if 'health_insurance' in self.benefits:
            return self.salary * 0.9
        if 'retirement' in self.benefits:
            return self.salary * 0.8

        return 0

    def __str__(self):
        return f'{Employee.__str__(self)}, {self.benefits}'

############################################################
############################################################
############################################################


class Manager(Employee):
    """ 
    A manager class that inherits from the base Employee Class with 
    an overloaded cal_salary method and new bonus property
    """

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.bonus = kwargs.get('bonus')

    def cal_salary(self):
        """
        Calculates the salary for an instance of Manager and adding bonus
        """
        return float(self.salary + self.bonus)

    def __str__(self):
        return f'{Employee.__str__(self)}, {self.bonus}'


############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    """
    A temporary employee class that inherits from the base Employee Class
    with an overloaded cal_salary method and new hours property
    """

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.hours = kwargs.get('hours')

    def cal_salary(self):
        """
        Calculates the salary for an instance of TemporaryEmployee by 
        multiplying salary and hours
        """
        return float(self.salary * self.hours)

    def __str__(self):
        return f'{Employee.__str__(self)}, {self.hours}'


############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    """
    A consultant class that inherits from the Temporary Employee Class
    with an overloaded cal_salary method and new travel property
    """

    def __init__(self, **kwargs):
        TemporaryEmployee.__init__(self, **kwargs)
        self.travel = kwargs.get('travel')

    def cal_salary(self):
        """
        Calculates the salary for an instance of Consultant by 
        calling cal_salary from the inherited class and adding travel pay
        """
        return TemporaryEmployee.cal_salary(self) + self.travel * 1000

    def __str__(self):
        return f'{TemporaryEmployee.__str__(self)}, {self.travel}'


############################################################
############################################################
############################################################


class ConsultantManager(Consultant, Manager):
    """
    A consultant manager class that inherits from both the Consultant and 
    Manager classes. No new properties are defined, but the cal_salary method
    is overloaded
    """

    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)

    def cal_salary(self):
        """
        Calculates the salary of a consultant manager by calling cal_salary
        on the Consultant class and adding bonus
        """
        return Consultant.cal_salary(self) + self.bonus

    def __str__(self):
        manage_str = " ".join(Manager.__str__(self).split()[1:])
        return f'{Consultant.__str__(self)}, ConsultantManager\n{manage_str}'


############################################################
############################################################
############################################################


###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                             salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(
        name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4",
                      salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                             salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
    main()
