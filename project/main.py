from command_line_interface import CommandLineInterface
from simulation import Simulation


def main():

    CommandLineInterface.print_title()

    DISEASE_NAME = CommandLineInterface.get_disease_name()
    MATRIX_DIMENSION = CommandLineInterface.get_matrix_dimension()
    POPULATION_MATRIX_DIMENSION = CommandLineInterface.get_population_matrix_dimension()

    INFECTION_PROB = CommandLineInterface.get_infection_probability()
    MORTALITY_PROB = CommandLineInterface.get_mortality_probability()

    LIFESPAN_MU = CommandLineInterface.get_lifespan_mean()
    LIFESPAN_SIGMA = CommandLineInterface.get_lifespan_standard_dev()

    AGE_MU = CommandLineInterface.get_age_mean()
    AGE_SIGMA = CommandLineInterface.get_age_standard_dev()

    POPULATION_GROWTH_RATE = CommandLineInterface.get_population_growth_rate()

    NUM_WEEKS = CommandLineInterface.get_num_weeks()
    GET_INITIAL_NUM_CONTAGIOUS = CommandLineInterface.get_num_initial_contagious()

    FILE_NAME = CommandLineInterface.get_file_name()

    sim = Simulation(MATRIX_DIMENSION)
    sim.set_pop(POPULATION_MATRIX_DIMENSION, INFECTION_PROB,
                MORTALITY_PROB, LIFESPAN_MU, LIFESPAN_SIGMA, AGE_MU, AGE_SIGMA, POPULATION_GROWTH_RATE)

    sim.run_simulation(DISEASE_NAME, NUM_WEEKS,
                       GET_INITIAL_NUM_CONTAGIOUS, FILE_NAME)


if __name__ == '__main__':
    main()
