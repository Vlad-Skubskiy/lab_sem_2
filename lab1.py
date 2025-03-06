arr = []
n = int(input("Enter amount of elements in array: "))
for el in range(n):
    el = int(input())
    arr.append(el)
def min_(arr):
    min = arr[1]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
def is_monotone1(arr):
    anomal_arr = []
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            anomal_arr.append(i-1)
    if anomal_arr:
        return print(min_(anomal_arr), max(anomal_arr))
    else:
        return True

# def is_monotone2(arr):

#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             return False
#     return True

if is_monotone1(arr):
    print("True")
else:
    print("False")
