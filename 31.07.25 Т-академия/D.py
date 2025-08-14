import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2 + n]))

    NEG_INF = -10 ** 15
    dp1 = [[NEG_INF] * (k + 2) for _ in range(n + 1)]
    dp2 = [[NEG_INF] * (k + 2) for _ in range(n + 1)]

    dp2[1][0] = 0

    for j in range(k + 1):
        for i in range(1, n + 1):
            if dp2[i][j] > NEG_INF:
                if i <= n:
                    val = dp2[i][j] + a[i - 1]
                    if val > dp1[i][j]:
                        dp1[i][j] = val
                if i + 1 <= n:
                    val = dp2[i][j] + a[i]
                    if val > dp1[i + 1][j]:
                        dp1[i + 1][j] = val
            if dp1[i][j] > NEG_INF:
                if i + 1 <= n:
                    val = dp1[i][j] + a[i]
                    if val > dp1[i + 1][j]:
                        dp1[i + 1][j] = val
                if i + 2 <= n:
                    val = dp1[i][j] + a[i + 1]
                    if val > dp1[i + 2][j]:
                        dp1[i + 2][j] = val

        pm = [NEG_INF] * (n + 1)
        for t in range(1, n + 1):
            current = max(dp1[t][j], dp2[t][j])
            if t == 1:
                pm[t] = current
            else:
                pm[t] = max(pm[t - 1], current)

        if j < k:
            for t in range(2, n + 1):
                if pm[t - 1] > dp2[t][j + 1]:
                    dp2[t][j + 1] = pm[t - 1]

    ans = NEG_INF
    for j in range(k + 1):
        if dp1[n][j] > ans:
            ans = dp1[n][j]
    print(ans)


if __name__ == "__main__":
    main()