def quadratic_time(n):
    steps = 0
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps

n = 5
print("O(n^2) example (total operations):", quadratic_time(n))
