"""
sys - read in test cases from stdin
time - used to time differences between linear and binary search
"""
import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v: int, k: int) -> int:
    """
      Computes the series of v // k ** p
      while the result > 0
    """

    total = 0
    p = 0

    while (lines := v // k ** p) != 0:
        total += lines
        p += 1

    return total


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search(n: int, k: int) -> int:
    """
    Uses linear search to find the minimum
    value of v that >= n
    """
    for v in range(1, n + 1):
        if sum_series(v, k) >= n:
            return v

    return -1

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search


def binary_search(n: int, k: int) -> int:
    """
    Uses binary search to find the minimum
    value of v that >= n
    """

    l = 1
    r = n

    min_lines = n

    while l <= r:
        mid = (l + r) // 2
        lines = sum_series(mid, k)

        if lines < n:
            l = mid + 1
        else:
            min_lines = min(min_lines, mid)
            r = mid - 1

    return min_lines


def main() -> None:
    """
    Reads in test cases from stdin and 
    times linear vs binary search.
    Logs results to console
    """

    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for _ in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()
