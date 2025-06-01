def generate_combinations(n, k):
    A = list(range(1, k + 1))
    result = []
    while True:
        result.append(A.copy())

        if A[-1] == n:
            p = k - 1
            while p >= 0 and A[p] == n - k + p + 1:
                p -= 1
        else:
            p = k - 1

        if p < 0:
            break

        A[p] += 1
        for i in range(p + 1, k):
            A[i] = A[p] + i - p
    return result

n = 6
k = 4
combinations = generate_combinations(n, k)
for c in combinations:
    print(c)