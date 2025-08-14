def days_on_month(days: int):
    global n, m
    if m > days:
        return False
    return (n+days-m) == 14


n, m = map(int, input().strip().split())
if n >= 8:
    print(n-7)
    exit(0)
else:
    month_len = 0
    if days_on_month(28):
        month_len = 28
    elif days_on_month(29):
        month_len = 29
    elif days_on_month(30):
        month_len = 30
    else:
        month_len = 31
    print(n-7+month_len)
