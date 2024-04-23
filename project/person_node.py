from status import Status
import random as r
import numpy as np
from scipy.stats import norm


class PersonNode:
    """
    Represents a node in a network of individuals.

    Attributes:
        row (int): The row index of the node.
        col (int): The column index of the node.
        status (Status): The status of the person node.
        age (int): The age of the person node in weeks.
        week_dead (int): The week in which the person node died.
        week_infected (int): The week in which the person node got infected.
        week_contagious (int): The week in which the person node became contagious.
    """

    def __init__(self, row: int, col: int) -> None:
        """
        Initializes a PersonNode object with the given row and column indices.

        Args:
            row (int): The row index of the node.
            col (int): The column index of the node.
        """
        self.row = row
        self.col = col
        self.status: Status = Status.EMPTY
        self.age = None
        self.week_dead = None
        self.week_infected = None
        self.week_contagious = None

    def simulate_birth(self) -> None:
        """
        Simulates the birth of a person by setting status to HEALTHY and age to 0.
        """
        self.status = Status.HEALTHY
        self.age = 0

    def simulate_infection(self, week: int, infection_prob: float) -> None:
        """
        Simulates the infection of a person based on the given infection probability.

        Args:
            week (int): The current week of simulation.
            infection_prob (float): The probability of infection.
        """
        if not self.status == Status.IMMUNE and r.random() <= infection_prob:
            self.status = Status.INFECTED
            self.week_infected = week

    def simulate_contagion(self, week: int) -> None:
        """
        Simulates the person becoming contagious in the given week.

        Args:
            week (int): The current week of simulation.
        """
        self.status = Status.CONTAGIOUS
        self.week_contagious = week

    def simulate_death_by_natural_causes(self, lifespan_mu: float, lifespan_sigma: float, week: int) -> None:
        """
        Simulates the death of a person by natural causes based on lifespan statistics.

        Args:
            lifespan_mu (float): The mean lifespan in years.
            lifespan_sigma (float): The standard deviation of lifespan in years.
            week (int): The current week of simulation.
        """
        z_score = (self.age - lifespan_mu * 52) / lifespan_sigma * 52
        area = norm.cdf(z_score)

        if r.random() < area:
            self.status = Status.DEAD
            self.week_dead = week

    def set_age(self, age_mu: float, age_sigma: float) -> None:
        """
        Sets the age of the person node based on normal distribution parameters.

        Args:
            age_mu (float): The mean age in years.
            age_sigma (float): The standard deviation of age in years.
        """
        # age in weeks
        arr = np.random.normal(age_mu, age_sigma, size=1) * 52
        val = int(arr[0])
        self.age = val

    def simulate_end_contagion(self, week: int, mortality_rate: float) -> None:
        """
        Simulates the end of contagion, either through death or immunity.

        Args:
            week (int): The current week of simulation.
            mortality_rate (float): The mortality rate among contagious individuals.
        """
        if r.random() < mortality_rate:
            self.status = Status.DEAD
            self.week_dead = week
            return

        # person survived
        self.status = Status.IMMUNE

    def increment_age(self) -> None:
        """
        Increments the age of the person node by one week.
        """
        if self.age is None:
            raise TypeError('Age not set')
        self.age += 1
