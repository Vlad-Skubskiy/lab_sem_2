import math

def electr() -> float:
    w = int(input())
    N = list(map(int, input().split()))
    dp = [[0] * (N[i] + 1) for i in range(len(N))]

    for i in range(1, len(N)):
        for h in range(1, N[i] + 1):
            for h_prev in range(1, N[i-1]+1):
                worst_case = math.sqrt((h-h_prev) ** 2 + w ** 2)
                dp[i][h] = max(dp[i][h], dp[i-1][h_prev] + worst_case)
    result = max(dp[len(N)-1])
    return round(result, 2)
print(electr())