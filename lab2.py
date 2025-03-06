def find_amount_of_stickers(s, n, w, h):
    return (s//w) * (s//h) >= n

def binary_search(n, w, h):
    left = min(w, h)
    right = max(w, h) * n
    while left<right:
        mid = left + (right - left) // 2
        if find_amount_of_stickers(mid, n, w, h):
            right = mid
        else:
            left = mid + 1

    return left

desk1 = binary_search(2, 1000000000, 999999999)
print(desk1)