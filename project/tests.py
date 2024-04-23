import unittest
from simulation import Simulation


class TestCases(unittest.TestCase):
    def test_standard_pop(self) -> None:
        DISEASE_NAME = 'test1'

        # matrix constants
        MATRIX_DIMENSION = 45
        INITIAL_POP_DIMENSION = 30
        # infection and mortality probabilities
        INFECTION_PROB = 0.8
        MORTALITY_PROB = 0.5
        # population lifespan mean and standard deviation
        LIFESPAN_MU = 35
        LIFESPAN_SIGMA = 8
        # population age mean and standard deviation
        AGE_MU = 24
        AGE_SIGMA = 6
        # population growth rate
        ANNUAL_POP_GROWTH_RATE = 0.05
        # number of initial contagious people
        NUM_CONTAGIOUS_INITAL = 2
        # number of simulation iterations
        NUM_WEEKS = 50

        FILE_NAME = 'test-1'

        sim = Simulation(MATRIX_DIMENSION)
        sim.set_pop(INITIAL_POP_DIMENSION, INFECTION_PROB, MORTALITY_PROB,
                    LIFESPAN_MU, LIFESPAN_SIGMA, AGE_MU, AGE_SIGMA, ANNUAL_POP_GROWTH_RATE)
        try:
            sim.run_simulation(DISEASE_NAME, NUM_WEEKS,
                               NUM_CONTAGIOUS_INITAL, FILE_NAME)
        except:
            self.fail('Test 1 Failed')

    def test_large_pop(self) -> None:
        DISEASE_NAME = 'test2'

        # matrix constants
        MATRIX_DIMENSION = 160
        INITIAL_POP_DIMENSION = 140
        # infection and mortality probabilities
        INFECTION_PROB = 0.8
        MORTALITY_PROB = 0.5
        # population lifespan mean and standard deviation
        LIFESPAN_MU = 35
        LIFESPAN_SIGMA = 8
        # population age mean and standard deviation
        AGE_MU = 24
        AGE_SIGMA = 6
        # population growth rate
        ANNUAL_POP_GROWTH_RATE = 0.05
        # number of initial contagious people
        NUM_CONTAGIOUS_INITAL = 5
        # number of simulation iterations
        NUM_WEEKS = 208

        FILE_NAME = 'test-2'

        sim = Simulation(MATRIX_DIMENSION)
        sim.set_pop(INITIAL_POP_DIMENSION, INFECTION_PROB, MORTALITY_PROB,
                    LIFESPAN_MU, LIFESPAN_SIGMA, AGE_MU, AGE_SIGMA, ANNUAL_POP_GROWTH_RATE)
        try:
            sim.run_simulation(DISEASE_NAME, NUM_WEEKS,
                               NUM_CONTAGIOUS_INITAL, FILE_NAME)
        except:
            self.fail('Test 2 Failed')

    def test_above_average_pop(self) -> None:

        DISEASE_NAME = 'test-3'

        # matrix constants
        MATRIX_DIMENSION = 70
        INITIAL_POP_DIMENSION = 50
        # infection and mortality probabilities
        INFECTION_PROB = 0.8
        MORTALITY_PROB = 0.7
        # population lifespan mean and standard deviation
        LIFESPAN_MU = 50
        LIFESPAN_SIGMA = 20
        # population age mean and standard deviation
        AGE_MU = 24
        AGE_SIGMA = 15
        # population growth rate
        ANNUAL_POP_GROWTH_RATE = 0.05
        # number of initial contagious people
        NUM_CONTAGIOUS_INITAL = 3
        # number of simulation iterations
        NUM_WEEKS = 52

        FILE_NAME = 'test-3'

        sim = Simulation(MATRIX_DIMENSION)
        sim.set_pop(INITIAL_POP_DIMENSION, INFECTION_PROB, MORTALITY_PROB,
                    LIFESPAN_MU, LIFESPAN_SIGMA, AGE_MU, AGE_SIGMA, ANNUAL_POP_GROWTH_RATE)
        try:
            sim.run_simulation(DISEASE_NAME, NUM_WEEKS,
                               NUM_CONTAGIOUS_INITAL, FILE_NAME)
        except:
            self.fail('Test 3 Failed')


if __name__ == '__main__':
    unittest.main()
