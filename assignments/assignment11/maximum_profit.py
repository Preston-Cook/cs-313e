'''import sys module to read from stdin'''
import sys

# Add Your functions here


# You are allowed to change the main function.

# Do not change the template file name.

def main():
    '''Main function for execution of program'''

    # The first line is the amount of investment in million USD which is an integer number.

    money = 12


# The second line includes an integer number which is the number of houses listed for sale.

    num_houses = 4

    prices = [6, 3, 4, 5]

    # read the number of vertices
    increase = list(map(lambda x: x / 100, [12, 6, 1, 9]))

    values = [increase[i] * prices[i] for i in range(num_houses)]

    res = knap_sack(money, prices, values, num_houses)
    print(f'{res:.2f}')


def knap_sack(capacity: int, weights: list[int], values: list[int], num_items: int):
    '''implemention of the dynamic programming solution of the knap sack problem'''
    dp = [0 for _ in range(capacity + 1)]

    for i in range(1, num_items + 1):
        for c in range(capacity, 0, -1):
            if weights[i - 1] <= c:
                dp[c] = max(dp[c], dp[c - weights[i - 1]] + values[i - 1])

    return dp[capacity]


def calculate_max_profit(prices: list[int], increase: list[int],
                         most_profitable_lst: list[int], money: int) -> str:
    '''Calculates the max profit of houses'''
    res = 0

    for i in most_profitable_lst:
        price = prices[i]

        if money >= price:
            money -= price
            res += increase[i] * price

    return f'{res:.2f}'


if __name__ == '__main__':
    main()
