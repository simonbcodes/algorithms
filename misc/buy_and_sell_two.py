# mildy overcomplicated, but O(n) i think

def buy_and_sell(prices):    
    i = 0
    profit = 0

    while i < len(prices) - 1:
        j = i + 1
        done = False
        while j < len(prices) and prices[j] > prices[j - 1]:
            j += 1
        add = prices[j - 1] - prices[i]
        if add > 0:
            profit += add
        i = j

    return profit

a = [i for i in range(1, 6)]

print(buy_and_sell(a))
