def constant_time(arr):
    return arr[0]

arr = [10, 20, 30, 40]
print("O(1) example:", constant_time(arr))


def linear_time(arr):
    total = 0
    for value in arr:
        total += value
    return total

arr = list(range(1, 6))
print("O(n) example:", linear_time(arr))


def logarithmic_time(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return steps

arr = list(range(1, 33))  # 32 elements
target = 30
print("O(log n) example (steps to find target):", logarithmic_time(arr, target))


def quadratic_time(n):
    steps = 0
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps

n = 5
print("O(n^2) example (total operations):", quadratic_time(n))

