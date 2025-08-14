def check_condition(h, a, t, day):
    for i in range(len(h)):
        current_height = h[i] + a[i] * day
        higher_plants = sum(1 for j in range(len(h)) if h[j] + a[j] * day > current_height)
        if higher_plants != t[i]:
            return False
    return True

def find_day(h, a, t):
    right = 1
    while not check_condition(h, a, t, right):
        right*=2
        if right>10e9:
            return -1
    left=0
    while right-left>1:
        mid = int(left + right) // 2
        if check_condition(h, a, t, mid):
            right = mid
        else:
            left = mid
    if not check_condition(h, a, t, right):
        return -1
    if left==0:
        return 0
    return -1 if left > right else right

t = int(input())
for _ in range(t):
    n = int(input())
    h_arr = list(map(int, input().split()))
    a_arr = list(map(int, input().split()))
    t_arr = list(map(int, input().split()))
    print(find_day(h_arr, a_arr, t_arr))


