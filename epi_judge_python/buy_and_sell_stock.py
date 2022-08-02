from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    minimum_so_far, max_profit_so_far = prices[0], 0

    for price in prices:
        if(price < minimum_so_far):
            minimum_so_far = price

        today_profit = price - minimum_so_far

        if(today_profit > max_profit_so_far):
            max_profit_so_far = today_profit

    return max_profit_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
