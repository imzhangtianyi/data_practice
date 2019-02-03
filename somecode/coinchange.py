from collections import deque
def bfs(coins, amount):
    dq = deque()
    visited = [True] + [False]*amount
    for coin in coins:
        dq.append((coin, 1))

    while dq:
        value, depth = dq.popleft()
        for coin in coins:
            val = value + coin
            if val == amount: return depth+1
            if val < amount and not visited[val]:
                visited[val] = True
                dq.append((val, depth+1))
    return -1

def dfs(coins, amount):
    arr = [0] + [amount+1] * amount
    for val in range(1, amount+1):
        for coin in coins:
            if val >= coin:
                arr[val] = min(arr[val], arr[val-coin]+1)
    return arr[amount]

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 24
    print('the number of coin is: {}'.format(bfs(coins, amount)))