def binary_search(arr, x):
    l = -1
    r = len(arr)
    while (r - l) > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    return r

n = int(input().strip())
trains = []
for _ in range(n):
    trains.append(list(map(int, input().split())))
q = int(input().strip())
meet = [[train[0]] for train in trains]
for _ in range(q):
    t, d = map(int, input().split())
    t -= 1
    while meet[t][-1] < d:
        next_time = meet[t][-1] + trains[t][1]
        meet[t].append(next_time)
    pos = binary_search(meet[t], d)
    print(meet[t][pos])