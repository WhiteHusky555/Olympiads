n, a = map(int, input().split())
t = list(map(int, input().split()))

finish_time = [0] * n

for i in range(n):
    if i == 0:
        finish_time[i] = t[i] + a
    else:

        if t[i] < finish_time[i - 1]:
            finish_time[i] = finish_time[i - 1] + a
        else:
            finish_time[i] = t[i] + a

for i in range(n):
    print(finish_time[i])