def linear_time(arr):
    total = 0
    for value in arr:
        total += value
    return total

arr = list(range(1, 6))
print("O(n) example:", linear_time(arr))
