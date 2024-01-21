"""
    File: spiral.py
    Description: A program that generates a spiral matrix beginning at the center and traveling
                right, left, down, and up while incrementing the previous value
                in the spiral by one. The sum_sub_grid function sums adjacent numbers given a
                value in the matrix spiral. If the value does not exist, then a 0 is returned.
    Student Name: Preston Cook
    Student UT EID: plc886
    Partner Name: Crystal Hicks
    Partner UT EID: crh4624
    Course Name: CS 313E
    Unique Number: 50775
    Date Created: 18 January 2023
    Date Last Modified: 20 January 2023
    Input: n is an odd integer between 1 and 100
    Output: returns a 2-D list representing a spiral
    if n is even add one to n
"""


def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral diameter"""

    # initialize matrix
    matrix = [[0 for _ in range(dim)] for _ in range(dim)]

    slots = dim ** 2
    multipliers = [1, 1, 2, 2]

    x_val = y_val = dim // 2
    matrix[y_val][x_val] = 1
    cur = matrix[y_val][x_val]
    slots -= 1
    direction = 0

    while cur < slots:

        idx = direction % 4
        cur = matrix[y_val][x_val]
        prev_y, prev_x = y_val, x_val
        mult = multipliers[idx]

        if idx == 0:
            # right

            # prevent spillover in final pass
            while x_val < mult + prev_x and x_val != dim - 1:
                cur += 1
                x_val += 1
                matrix[y_val][x_val] = cur

        elif idx == 1:
            # down
            while y_val < mult + prev_y:
                cur += 1
                y_val += 1
                matrix[y_val][x_val] = cur

        elif idx == 2:
            # left
            while x_val > prev_x - mult:
                cur += 1
                x_val -= 1
                matrix[y_val][x_val] = cur

        elif idx == 3:
            # up
            while y_val > prev_y - mult:
                cur += 1
                y_val -= 1
                matrix[y_val][x_val] = cur

        multipliers[idx] += 2
        direction += 1

    return matrix


def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
    val is a number within the range of numbers in
    the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    n_val = len(grid)

    for row in range(n_val):
        for col in range(n_val):
            if grid[row][col] == val:
                total = 0

                # top-left
                if row - 1 >= 0 and col - 1 >= 0:
                    total += grid[row - 1][col - 1]

                # top-mid
                if row - 1 >= 0:
                    total += grid[row - 1][col]

                # top-right
                if row - 1 >= 0 and col + 1 < n_val:
                    total += grid[row - 1][col + 1]

                # mid-left
                if col - 1 >= 0:
                    total += grid[row][col - 1]

                # mid-right
                if col + 1 < n_val:
                    total += grid[row][col + 1]

                # bottom-left
                if row + 1 < n_val and col - 1 >= 0:
                    total += grid[row + 1][col - 1]

                # bottom-mid
                if row + 1 < n_val:
                    total += grid[row + 1][col]

                # bottom-right
                if row + 1 < n_val and col + 1 < n_val:
                    total += grid[row + 1][col + 1]

                return total

    # value not found
    return 0


def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """
    # read the dimension of the grid and value from input file
    dim = int(input())
    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1
    # create a 2-D list representing the spiral
    mat = create_spiral(dim)
    while True:
        try:
            sum_val = int(input())
        # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)
        # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
