def xor_set(S):
    result = 0
    for num in S:
        result ^= num
    return result


def g(x, S):
    max_xor = 0
    for num in S:
        max_xor = max(max_xor, x ^ num)
    return max_xor


def f(l, r, a, S):
    max_value = 0
    for i in range(l - 1, r):
        max_value = max(max_value, g(a[i], S))
    return max_value


def process_queries(n, q, a, queries):
    S = set()
    results = []

    for query in queries:
        if query[0] == 1:
            k, v = query[1] - 1, query[2]
            a[k] = v
        elif query[0] == 2:
            x = query[1]
            S.add(x)
        elif query[0] == 3:
            l, r = query[1], query[2]
            results.append(f(l, r, a, S) & ((1 << 64) - 1))

    return results



n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

output = process_queries(n, q, a, queries)
for result in output:
    print(result)
