
inc: int = 0
lenth: int = int(input())
arr: list = list(map(int, input().strip().split()))
if lenth==1:
    print(0)
else:
    for i in range(1, lenth):
        if arr[i-1] > arr[i]:
            inc += abs(arr[i-1]-arr[i])
print(inc)