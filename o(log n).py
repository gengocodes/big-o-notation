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
