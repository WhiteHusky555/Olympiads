import math
from collections import defaultdict
from functools import reduce

MOD = 998244353

def get_coprime_factors(x):
    res = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            j = x // i
            if math.gcd(i, j) == 1:
                res.append((i, j))
                if i != j:
                    res.append((j, i))
    return res

def solve(n, a):
    dp = defaultdict(dict)

    # инициализация первого элемента
    for p, q in get_coprime_factors(a[0]):
        dp[0][(p, q)] = p * q

    for i in range(1, n - 1):
        next_dp = defaultdict(dict)
        for (prev_p, prev_q), val in dp[i - 1].items():
            for p, q in get_coprime_factors(a[i]):
                if prev_q == p:
                    # продолжаем цепочку
                    new_seq = (prev_p, q)
                    next_val = (val * q) % MOD
                    if new_seq in next_dp[i]:
                        next_dp[i][new_seq] = (next_dp[i][new_seq] + next_val) % MOD
                    else:
                        next_dp[i][new_seq] = next_val
        dp[i] = next_dp[i]

    # теперь собрать все последовательности и выбрать те, у которых gcd == 1
    total = 0
    for (start, end), val in dp[n - 2].items():
        seq = [start]
        prev = start
        for i in range(n - 1):
            for p, q in get_coprime_factors(a[i]):
                if prev == p:
                    seq.append(q)
                    prev = q
                    break
        if math.gcd(*seq) == 1:
            product = 1
            for x in seq:
                product = (product * x) % MOD
            total = (total + product) % MOD

    return total

# Пример использования:
n = int(input().strip())

a = list(map(int, input().split()))
print(solve(n, a))  # Выведет: 712