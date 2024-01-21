"""
    File: spiral.py
    Description: A program that generates a spiral matrix beginning at the center and traveling right, left, down, and up while incrementing the previous value in the spiral by one. 
                 The sum_sub_grid function sums adjacent numbers given a value in the matrix spiral. If the value does not exist, then a 0 is returned
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

    x = y = dim // 2
    matrix[y][x] = 1
    cur = matrix[y][x]
    slots -= 1
    dir = 0

    while cur < slots:

        idx = dir % 4
        cur = matrix[y][x]
        prev_y, prev_x = y, x
        mult = multipliers[idx]

        if idx == 0:
            # right
            while x < mult + prev_x and x != dim - 1: # prevent spillover in final pass
                cur += 1
                x += 1
                matrix[y][x] = cur
                    
        elif idx == 1:
            # down
            while y < mult + prev_y:
                cur += 1
                y += 1
                matrix[y][x] = cur
                    
        elif idx == 2:
            # left
            while x > prev_x - mult:
                cur += 1
                x -= 1
                matrix[y][x] = cur
                    
        elif idx == 3:
            # up 
            while y > prev_y - mult:
                cur += 1
                y -= 1
                matrix[y][x] = cur

        multipliers[idx] += 2
        dir += 1

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
    n = len(grid)

    for r in range(n):
        for c in range(n):
            if grid[r][c] == val:
                total = 0

                # top-left
                if r - 1 >= 0 and c - 1 >= 0:
                    total += grid[r - 1][c - 1]

                # top-mid
                if r - 1 >= 0:
                    total += grid[r - 1][c]

                # top-right
                if r - 1 >= 0 and c + 1 < n:
                    total += grid[r - 1][c + 1]

                # mid-left
                if c - 1 >= 0:
                    total += grid[r][c - 1]

                # mid-right
                if c + 1 < n:
                    total += grid[r][c + 1]

                # bottom-left
                if r + 1 < n and c - 1 >= 0:
                    total += grid[r + 1][c - 1]

                # bottom-mid
                if r + 1 < n:
                    total += grid[r + 1][c]

                # bottom-right
                if r + 1 < n and c + 1 < n:
                    total += grid[r + 1][c + 1]

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
