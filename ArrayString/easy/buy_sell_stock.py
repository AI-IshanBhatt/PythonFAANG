def maxProfit(self, prices) -> int:
    current_min = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < current_min:
            current_min = price
        else:
            current_profit = price - current_min
            max_profit = max(max_profit, current_profit)

    return max_profit


def maxProfitOpt(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit