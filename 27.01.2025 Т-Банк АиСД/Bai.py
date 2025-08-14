def find_days(T, test_cases):
    results = []
    for case in test_cases:
        n, heights, growths, t = case
        days = []
        for i in range(n):
            target = t[i]
            current_height = heights[i]
            growth_per_day = growths[i]
            day = 0

            while True:
                taller_count = sum(
                    1 for j in range(n) if heights[j] + growths[j] * day > current_height + growth_per_day * day)
                if taller_count == target:
                    days.append(day)
                    break
                if day > 10000:  # Arbitrary large number to prevent infinite loop
                    days.append(-1)
                    break
                day += 1

        results.append(max(days) if all(d != -1 for d in days) else -1)

    return results


# Пример использования
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    heights = list(map(int, input().split()))
    growths = list(map(int, input().split()))
    t = list(map(int, input().split()))
    test_cases.append((n, heights, growths, t))

results = find_days(T, test_cases)
for result in results:
    print(result)
 