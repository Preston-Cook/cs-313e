"""
    File: employee.py
    Description: Given a list of tuples representing intervals,
                The program returns a list of collapsed intervals
    Student Name: Preston Cook
    Student UT EID: plc886
    Partner Name: Crystal Hicks
    Partner UT EID: crh4624
    Course Name: CS 313E
    Unique Number: 50775
    Date Created: 30 January 2023
    Date Last Modified: 30 January 2023
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the 
            interval
"""

import sys
from typing import List, Tuple


def merge_tuples(tuples_list: List[Tuple]) -> List[Tuple]:
    """Merge the tuples"""

    # sort by leftmost value in tuple
    tups = sorted(tuples_list, key=lambda x: x[0])

    # initialize stack with first tuple
    stack = [tups[0]]

    for i in range(1, len(tups)):
        if stack[-1][0] <= tups[i][0] <= stack[-1][-1]:

            # pop value from stack
            l, r = stack.pop()

            # push new tuple to stack
            stack.append((l, max(r, tups[i][1])))
        else:

            # add existing tuple to stack
            stack.append(tups[i])

    return stack


def sort_by_interval_size(tuples_list: List[Tuple]) -> List[Tuple]:
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    return sorted(tuples_list, key=lambda x: abs(x[0] - x[1]))


def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)


if __name__ == "__main__":
    main()
