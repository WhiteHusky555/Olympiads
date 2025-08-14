def can_satisfy_condition(d, n, h, a, t):
    # Calculate the count of plants taller than the second plant on day d
    h2 = h[1] + a[1] * d
    count_above = 0
    for i in range(n):
        if h[i] + a[i] * d > h2:
            count_above += 1
    # Check if this count matches the required count from t
    return all(count_above == t[i] for i in range(n))


def find_minimum_day(n, h, a, t):
    left, right = 0, 10 ** 9
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if can_satisfy_condition(mid, n, h, a, t):
            answer = mid
            right = mid - 1  # Try to find a smaller valid day
        else:
            left = mid + 1  # Increase the day count

    return answer


T = int(input())
results = []
for _ in range(T):
    n = int(input())
    h = list(map(int, input().split()))
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))

    result = find_minimum_day(n, h, a, t)
    results.append(result)

for res in results:
    print(res)