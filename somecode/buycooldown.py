def fun(prices):
    hold, sell, cool = float('-inf'), 0, float('-inf')
    for i in prices:
        hold, sell, cool = max(hold, sell-i), max(sell, cool), hold+i
    return max(sell, cool)


if __name__ == '__main__':
    print(fun([1, 2, 4, 0, 3]))
