from collections import deque


def solve(N, segments):
    graph = [[] for _ in range(N + 1)]
    for l, r in segments:
        graph[l - 1].append(r)

    dist = [-1] * (N + 1)
    dist[0] = 0
    queue = deque([0])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                if v == N:
                    # нашли путь до N, можно прервать
                    break

    if dist[N] == -1:
        print("No")
    else:
        print("Yes")
        print(dist[N])


# Чтение входных данных
N, Q = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(Q)]

solve(N, segments)
