def max_balanced_sequences(n, m, k, arr):
    b = []
    for a, c in arr:
        b.extend([a] * c)

    b.sort()
    count = 0
    last = -float('inf')

    for num in b:
        if num - last > k:
            count += 1
            last = num

    return min(count, m)

# Ввод данных
n, m, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# Вывод результата
print(max_balanced_sequences(n, m, k, arr))
