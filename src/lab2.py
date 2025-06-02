def bin_search(N, W, H):

    left = max(W, H)
    right = max(W, H) * N
    while left < right:

        m = (left + right) // 2
        count_w = m // W
        count_h = m // H
        if count_h * count_w >= N:
            right = m
        else:
            left = m + 1
    return left

desk1 = bin_search(10, 3, 2)
print(desk1)