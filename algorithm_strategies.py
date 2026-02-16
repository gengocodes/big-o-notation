# Divide and Conquer: Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Recursive: Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Greedy Algorithm: Coin Change (min coins)
def greedy_coin_change(coins, amount):
    coins = sorted(coins, reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result


if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original Array:", arr)
    print("Merge Sort (Divide & Conquer):", merge_sort(arr))

    n = 5
    print(f"Factorial of {n} (Recursive):", factorial(n))

    coins = [25, 10, 5, 1]
    amount = 63
    print(f"Greedy Coin Change for {amount} with coins {coins}:", greedy_coin_change(coins, amount))
