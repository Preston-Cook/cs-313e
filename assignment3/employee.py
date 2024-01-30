

class Employee:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.identifier = kwargs.get('identifier')
        self.salary = kwargs.get('salary')

    def __str__(self):
        return f'{self.__class__.__name__}\n{self.name}, {self.identifier}, {self.salary}'


############################################################
############################################################
############################################################

class PermanentEmployee(Employee):
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.benefits = kwargs.get('benefits')

    def cal_salary(self):
        if 'health_insurance' in self.benefits and 'retirement' in self.benefits:
            return f'{self.salary * 0.7}'
        elif 'health_insurance' in self.benefits:
            return f'{self.salary * 0.9}'
        elif 'retirement' in self.benefits:
            return f'{self.salary * 0.8}'

    def __str__(self):
        return f'{Employee.__str__(self)}, {self.benefits}'

############################################################
############################################################
############################################################


class Manager(Employee):
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.bonus = kwargs.get('bonus')

    def cal_salary(self):
        return f'{self.salary + self.bonus:.1f}'

    def __str__(self):
        return f'{Employee.__str__(self)}, {self.bonus}'


############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    def __init__(self, **kwargs):

        Employee.__init__(self, **kwargs)
        self.hours = kwargs.get('hours')

    def cal_salary(self):
        return f'{self.salary * self.hours:.1f}'

    def __str__(self):
        return f'{Employee.__str__(self)}, {self.hours}'


############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    def __init__(self, **kwargs):
        TemporaryEmployee.__init__(self, **kwargs)
        self.travel = kwargs.get('travel')

    def cal_salary(self):
        return f'{float(TemporaryEmployee.cal_salary(self)) + self.travel * 1000:.1f}'

    def __str__(self):
        return f'{TemporaryEmployee.__str__(self)}, {self.travel}'


############################################################
############################################################
############################################################


class ConsultantManager(Consultant, Manager):
    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)

    def cal_salary(self):
        return f'{float(Consultant.cal_salary(self)) + self.bonus:.1f}'

    def __str__(self):
        return f'{Consultant.__str__(self)}, ConsultantManager\n{" ".join(Manager.__str__(self).split()[1:])}'


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
