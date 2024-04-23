from status import Status
from person_node import PersonNode
import matplotlib.pyplot as plt
import math
import copy
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
import random as r
from tqdm import tqdm
from collections import deque


class Simulation:
    def __init__(self, matrix_dimension: int) -> None:
        """
        Initializes a Matrix object with a specified dimension.

        Args:
            matrix_dimension (int, optional): The dimension of the matrix.
        """
        self.MATRIX_DIMENSION = matrix_dimension
        self.matrix = [[PersonNode(i, j) for j in range(self.MATRIX_DIMENSION)]
                       for i in range(self.MATRIX_DIMENSION)]

    def set_pop(self, initial_pop_dimension: int, infection_prob: float, mortality_prob: float, lifespan_mu: float, lifespan_sigma: float, age_mu: float, age_sigma: float, pop_growth_rate: float) -> None:
        """
        Sets the initial population parameters.

        Args:
            initial_pop_dimension (int): Initial population dimension.
            infection_prob (float): Infection probability.
            mortality_prob (float): Mortality probability.
            lifespan_mu (float): Mean lifespan.
            lifespan_sigma (float): Standard deviation of lifespan.
            age_mu (float): Mean age.
            age_sigma (float): Standard deviation of age.
            pop_growth_rate (float): Population growth rate.
        """
        self.INITIAL_POP_DIMENSION = initial_pop_dimension
        self.INFECTION_PROB = infection_prob
        self.MORTALITY_PROB = mortality_prob
        self.LIFESPAN_MU = lifespan_mu
        self.LIFESPAN_SIGMA = lifespan_sigma
        self.AGE_MU = age_mu
        self.AGE_SIGMA = age_sigma
        self.POP_GROWTH_RATE = pop_growth_rate
        self.history = []
        self.matrix_history = []

        center_start = (self.MATRIX_DIMENSION -
                        self.INITIAL_POP_DIMENSION) // 2

        center_end = center_start + self.INITIAL_POP_DIMENSION

        for i in range(center_start, center_end):
            for j in range(center_start, center_end):
                person_node = self.matrix[i][j]
                person_node.set_age(self.AGE_MU, self.AGE_SIGMA)
                person_node.status = Status.HEALTHY

    def __set_initial_contagious(self, num_contagious_initial: int) -> None:
        """
        Sets the initial contagious nodes in the matrix.

        Args:
            num_contagious_initial (int): Number of initial contagious nodes.
        """
        center_start = (self.MATRIX_DIMENSION -
                        self.INITIAL_POP_DIMENSION) // 2
        center_end = center_start + self.INITIAL_POP_DIMENSION

        initial_contagious = [(r.randint(center_start, center_end - 1), r.randint(
            center_start, center_end - 1)) for _ in range(num_contagious_initial)]

        for i, j in initial_contagious:
            person_node = self.matrix[i][j]
            person_node.simulate_contagion(0)

    def convert_to_int_matrix(self) -> list[list[int]]:
        """
        Converts the matrix of PersonNode objects to a matrix of integers representing node status.

        Returns:
            List[List[int]]: The converted integer matrix.
        """
        matrix_copy = [
            [0] * self.MATRIX_DIMENSION for _ in range(self.MATRIX_DIMENSION)]

        for i in range(self.MATRIX_DIMENSION):
            for j in range(self.MATRIX_DIMENSION):
                person_node = self.matrix[i][j]
                matrix_copy[i][j] = person_node.status

        return matrix_copy

    def get_adjacent_nodes(self, node: PersonNode) -> list[PersonNode]:
        """
        Returns the adjacent nodes given a node in the matrix.

        Args:
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            List[PersonNode]: List of adjacent nodes.
        """
        rows, cols = self.MATRIX_DIMENSION, self.MATRIX_DIMENSION
        adjacent_nodes = []
        row, col = node.row, node.col

        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                if (i, j) != (row, col):
                    adjacent_nodes.append(self.matrix[i][j])

        return adjacent_nodes
    
    def breadth_first_search(self, start_node):
        """
        Returns a list of perimeter nodes starting from given node in the matrix.

        Args:
            start_node (PersonNode): node in the matrix to start from
        
        Returns:
            List[PersonNode]: List of perimeter nodes.
        """
        queue = deque([start_node])
        visited = set()
        perimeter_nodes = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                adjacent_nodes = self.get_adjacent_nodes(node)
                for adj in adjacent_nodes:
                    if adj not in visited:
                        queue.append(adj)

        for node in visited:
            adjacent_nodes = self.get_adjacent_nodes(node)
            if any(adj.status == Status.EMPTY for adj in adjacent_nodes):
                perimeter_nodes.append(node)

        return perimeter_nodes

    def run_simulation(self, disease_name: str, num_weeks: int, num_contagious_initial: int, output_file: str) -> None:
        """
        Runs the simulation for the specified number of weeks.

        Args:
            disease_name (str): Disease name in simulation
            num_weeks (int): Number of weeks to simulate.
            num_contaigious_initial (int): Number of people initiall contagious in simulation
            output_file (str): Name of output file showing matplotlib animation
        """
        self.disease_name = disease_name
        self.output_file = output_file

        for week in tqdm(range(num_weeks)):
            if week == 0:
                num_annual_babies = math.ceil(
                    (self.INITIAL_POP_DIMENSION ** 2) * (self.POP_GROWTH_RATE))
                babies_per_week = num_annual_babies / 52
                self.__set_initial_contagious(num_contagious_initial)
                carry = babies_per_week
                continue

            empty_nodes, num_alive = self.simulate_week(week)

            if week % 52 == 0:
                num_annual_babies = num_alive * (self.POP_GROWTH_RATE)
                babies_per_week = num_annual_babies / 52
                carry = 0

            carry += babies_per_week

            if carry >= 1:
                num_babies = math.floor(carry)
                carry -= num_babies
                self.simulate_births(num_babies, empty_nodes)

            self.update_counts()

            recent_history = self.history[-1]

            if recent_history[2] == 0 and recent_history[3] == 0:
                break

        self.generate_video()

    def simulate_week(self, week: int) -> tuple[list[PersonNode], int]:
        """
        Simulates a single week of the population model.

        Args:
            week (int): Current week number in the simulation.
        """
        matrix_copy = copy.deepcopy(self.matrix)

        empty_nodes = []
        num_alive = 0

        for i in range(self.MATRIX_DIMENSION):
            for j in range(self.MATRIX_DIMENSION):
                person_node = copy.deepcopy(self.matrix[i][j])
                matrix_copy[i][j] = person_node

                if person_node.status == Status.EMPTY:
                    empty_nodes.append(person_node)
                    continue

                # clear out dead if exists
                elif person_node.status == Status.DEAD and week - person_node.week_dead == 1:
                    matrix_copy[i][j] = PersonNode(i, j)
                    continue

                num_alive += 1

                # check deaths of natural causes
                person_node.simulate_death_by_natural_causes(
                    self.LIFESPAN_MU, self.LIFESPAN_SIGMA, week)

                if person_node.status == Status.DEAD:
                    continue

                # increment weekly age for next week
                person_node.increment_age()

                # simulate infections if healthy
                if person_node.status == Status.HEALTHY:
                    adjacent_nodes = self.get_adjacent_nodes(person_node)

                    for node in adjacent_nodes:
                        if node.status == Status.CONTAGIOUS:
                            person_node.simulate_infection(
                                week, self.INFECTION_PROB)
                            if person_node.status == Status.CONTAGIOUS:
                                break

                    continue

                # update infected to contagious
                if person_node.status == Status.INFECTED and week - person_node.week_infected == 2:
                    person_node.simulate_contagion(week)

                # contagious die or become immune
                elif person_node.status == Status.CONTAGIOUS and week - person_node.week_contagious == 2:
                    person_node.simulate_end_contagion(
                        week, self.MORTALITY_PROB)

        self.matrix = matrix_copy
        return empty_nodes, num_alive

    def simulate_births(self, num_babies: int, empty_nodes: list[PersonNode]) -> None:
        """Finds nodes with adjacent alive nodes and simulates birth"""
        num_births = 0

        perimeter_nodes = self.breadth_first_search(self.matrix[0][0])
        r.shuffle(perimeter_nodes)

        for node in perimeter_nodes:
            adjacent_nodes = self.get_adjacent_nodes(node)
            for adj in adjacent_nodes:
                if num_births == num_babies:
                    break
                if adj.status == Status.EMPTY and node.status not in [Status.EMPTY, Status.DEAD]:
                    adj.simulate_birth()
                    num_births += 1
            perimeter_nodes.remove(node)

    def update_counts(self) -> None:
        """
        Update counts of various population states and record changes over time.

        This method iterates over the population matrix, updating counts for 
        different population states such as alive, healthy, infected, contagious, 
        dead, and immune. It then records these counts along with the previous 
        number of dead individuals in the population history.
        """
        if self.history:
            prev_num_dead = self.history[-1][4]
        else:
            prev_num_dead = 0

        num_alive = 0
        num_healthy = 0
        num_infected = 0
        num_contagious = 0
        num_dead = 0
        num_immune = 0

        matrix_copy = [
            [0] * self.MATRIX_DIMENSION for _ in range(self.MATRIX_DIMENSION)]

        for i in range(self.MATRIX_DIMENSION):
            for j in range(self.MATRIX_DIMENSION):
                val = self.matrix[i][j].status
                matrix_copy[i][j] = val
                if val == 1:
                    num_healthy += 1
                    num_alive += 1
                elif val == 2:
                    num_infected += 1
                    num_alive += 1
                elif val == 3:
                    num_contagious += 1
                    num_alive += 1
                elif val == 4:
                    num_dead += 1
                elif val == 5:
                    num_alive += 1
                    num_immune += 1

        self.history.append((
            num_alive,
            num_healthy,
            num_infected + num_contagious,
            num_contagious,
            prev_num_dead + num_dead,
            num_immune
        ))

        self.matrix_history.append(matrix_copy)

    def generate_video(self) -> None:
        """
        Generate a video visualization of the disease spread.

        This method generates a video visualization of the population matrix, 
        showing how the disease spreads over time. It saves the video as 
        'contagion.mp4' in the current directory.
        """
        colors = ['gray', 'green', 'yellow', 'orange', 'red', 'black']
        values = [0, 1, 2, 3, 4, 5]
        labels = ['Empty', 'Healthy',
                  'Infected', 'Contag.', 'Dead', 'Immune']

        cmap_custom = ListedColormap(colors)
        patches = [mpatches.Patch(color=colors[i], label=labels[i])
                   for i in range(len(values))]

        def generate_frame(frame: int) -> list[list[int]]:
            plt.clf()
            int_matrix = self.matrix_history[frame]
            im = plt.imshow(int_matrix, cmap=cmap_custom, vmin=-
                            0.5, vmax=5.5, interpolation='none')
            plt.title(f'{self.disease_name} Simulation: Week {frame}')
            plt.legend(handles=patches, bbox_to_anchor=(
                1.05, 1), loc=2, borderaxespad=0.0)
            return im

        fig = plt.figure()
        ani = FuncAnimation(fig, generate_frame, frames=len(
            self.matrix_history), repeat=False)
        ani.save(f'{self.output_file}.mp4', fps=5,
                 extra_args=['-vcodec', 'libx264'])
