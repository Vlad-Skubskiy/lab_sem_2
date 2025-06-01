# def fib(n:int) -> int:
#     if n == 0:
#         return 0
    
#     a = 0
#     b = 1
#     for i in range(2, n+1):
#         tmp = a + b
#         a = b
#         b = tmp
        
#     return b

def coin_sort(coins:list[int], amount: int) ->int:
    inf = int(1e4) + 1

    dp = [inf] * (amount + 1)
    dp[0] = 0

    for n in range(1, amount + 1):
        for coin in coins:
            if n >= coin:
                dp[n] = min(dp[n], dp[n-coin] + 1)
    print(dp)

    return dp[amount] if dp[amount] != inf else -1