#  File: InterestingDrink.py

#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of black tea in each store, and a list of integers named money that contains the amount of money
#               Tim will spend in a given day, returns a list of integers representing how many different shops
#               Tim can buy a cup of black tea.

#  Student Name: Preston Cook

#  Student UT EID: plc886

#  Course Name: CS 313E

#  Unique Number: 50775

import sys

# Input: prices a list of integers containing the price of black tea in each store
#        money  a list of integers containing the amount of money Tim will spend in a given day
# Returns: a list of integers representing how many different shops Tim can buy a cup of black tea.


def find_purchase_options(prices: list[int], money: list[int]) -> list[int]:
    sorted_prices = sorted(prices)
    res = []

    for m in money:
        count = 0
        l, r = 0, len(sorted_prices) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if sorted_prices[mid] <= m:
                count = mid + 1
                l = mid + 1
            else:
                r = mid - 1
        res.append(count)

    return res


#######################################################################################################
# No need to change the main()
# The input format the the main is two lines, each line contains some integers split by a single space.
# For example:
# 3 10 8 6 11
# 1 10 3 11
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()
