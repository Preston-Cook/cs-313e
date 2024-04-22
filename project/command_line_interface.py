class CommandLineInterface:
    def print_title():
        print(f'''
=============================================================================================
  ____        _   _                    _       _____ _                 _       _             
 / __ \      | | | |                  | |     / ____(_)               | |     | |            
| |  | |_   _| |_| |__  _ __ ___  __ _| | __ | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
| |  | | | | | __| '_ \| '__/ _ \/ _` | |/ /  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |__| | |_| | |_| |_) | | |  __/ (_| |   <   ____) | | | | | | | |_| | | (_| | || (_) | |   
 \____/ \__,_|\__|_.__/|_|  \___|\__,_|_|\_\ |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_| 
=============================================================================================
              
''')

    def get_disease_name() -> str:
        disease_name = input('Enter disease name: ')

        while len(disease_name) == 0:
            print('Invalid disease name')
            disease_name = input('Enter disease name: ')

        return disease_name

    def get_matrix_dimension() -> int:
        while (dimension := int(input('Enter matrix dimension: '))) <= 0:
            print('Invalid dimension')

        return dimension

    def get_population_matrix_dimension() -> int:
        while (dimension := int(input('Enter population matrix dimension: '))) <= 0:
            print('Invalid dimension')

        return dimension

    def get_infection_probability() -> float:
        infection_prob = float(input(
            'Enter weekly infection probability: '))

        while not (0 < infection_prob <= 1):
            print('Invalid infection probability')
            infection_prob = float(
                input('Enter weekly infection probability: '))

        return infection_prob

    def get_mortality_probability() -> float:
        mortality_prob = float(input(
            'Enter weekly mortality probability: '))

        while not (0 < mortality_prob <= 1):
            print('Invalid mortality probability')
            mortality_prob = float(
                input('Enter Weekly mortality probability: '))

        return mortality_prob

    def get_age_mean() -> float:
        age_mean = float(input('Enter age mean: '))

        while age_mean < 0:
            print('Invalid age mean')
            age_mean = float(input('Enter age mean: '))

        return age_mean

    def get_age_standard_dev() -> float:
        standard_dev = float(input('Enter age standard deviation: '))

        while standard_dev < 0:
            print('Invalid standard deviation')
            standard_dev = float(input(
                'Enter age standard deviation: '))

        return standard_dev

    def get_lifespan_mean() -> float:
        lifespan_mean = float(input('Enter lifespan mean: '))

        while lifespan_mean < 0:
            print('Invalid lifespan mean')
            lifespan_mean = float(input('Enter lifespan mean: '))

        return lifespan_mean

    def get_lifespan_standard_dev() -> float:
        standard_dev = float(input(
            'Enter lifespan standard deviation: '))

        while standard_dev < 0:
            print('Invalid lifespan standard deviation')
            standard_dev = float(input(
                'Enter lifespan standard deviation: '))

        return standard_dev

    def get_population_growth_rate() -> float:
        growth_rate = float(input('Enter population growth rate: '))

        while growth_rate < 0:
            print('Invalid growth rate')
            growth_rate = float(input(
                'Enter population growth rate: '))

        return growth_rate

    def get_file_name() -> str:
        file_name = input('Enter file name: ')

        while len(file_name) == 0:
            print('Invalid file name')
            file_name = input('Enter file name: ')

        return file_name

    def get_num_weeks() -> int:
        num_weeks = int(input('Enter number of weeks for simulation: '))

        while num_weeks < 0:
            print('Invalid number of weeks')
            num_weeks = int(input(
                'Enter number of weeks for simulation: '))

        return num_weeks

    def get_num_initial_contagious() -> int:
        num_contagious = int(input(
            'Enter initial number of contagious: '))

        while num_contagious < 0:
            print('Invalid number of contagious')
            num_contagious = int(input(
                'Enter initial number of contagious: '))

        return num_contagious
