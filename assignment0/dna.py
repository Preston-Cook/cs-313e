# File: dna.py

# Description:
# This solution uses a dynamic programming approach to create a matrix of common substrings.
# If longer than or equal to the current max, the substring is added to a hashset

# Student Name: Preston Cook

# Student UT EID: plc886

# Partner Name: Crystal Hicks

# Partner UT EID: crh4624

# Course: CS 313E

# Unique Number: 50775

# Date Created: 16 January 2023

# Last Date Modified: 16 January 2023

# Input: str_1 and str_2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
# common subsequence. The list is empty if there are no
# common subsequences.
import sys


def longest_subsequence(str_1: str, str_2: str):
    """
        Returns a sorted list containing the longest unique substrings between two DNA strings

        Args:
            str_1 (str): first strand of dna
            str_2 (str): second strand of dna

        Returns:
            list[str]: sorted list containing the longest substrings
    """
    len_1, len_2 = len(str_1), len(str_2)

    max_len = 0
    hashset = set()

    # Create matrix
    matrix = [[0 for _ in range(len_2 + 1)] for _ in range(len_1 + 1)]

    for i in range(len_1 + 1):
        for j in range(len_2 + 1):

            # if one of strings is of length 0
            if i == 0 or j == 0:
                matrix[i][j] = 0

            # chars are equal at indices
            elif str_1[i - 1] == str_2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1

                if max_len < matrix[i][j]:
                    max_len = matrix[i][j]
                    hashset = set()
                    hashset.add(str_1[i - max_len:i])

                elif max_len == matrix[i][j]:
                    hashset.add(str_1[i - max_len:i])

            # chars are not equal at indices
            else:
                matrix[i][j] = 0

    res = list(hashset)

    return sorted(res)


def main() -> None:
    """
    Main function for program

    Args:
        None

    Returns:
        None
    """

    # read the data
    data = sys.stdin.read().splitlines()
    num_pairs = int(data[0])
    pairs = data[1:]

    # for each pair call longest subsequence
    for i in range(num_pairs):
        str_1, str_2 = pairs[i * 2], pairs[i * 2 + 1]
        substrs = longest_subsequence(str_1, str_2)

        # write out results
        if not substrs:
            print('No Common Sequence Found')

        else:
            print(*substrs, sep='\n', end='\n\n' if i != num_pairs - 1 else '\n')


if __name__ == '__main__':
    main()
