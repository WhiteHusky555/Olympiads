n, a, b = map(int, input().split())
s = input().strip()

count_open = s.count('(')
count_close = len(s) - count_open

delta = (count_open - count_close) // 2
cost = abs(delta) * b

s_list = list(s)
if delta > 0:
    replace_count = delta
    for i in reversed(range(len(s_list))):
        if replace_count <= 0:
            break
        if s_list[i] == '(':
            s_list[i] = ')'
            replace_count -= 1
elif delta < 0:
    replace_count = -delta
    for i in range(len(s_list)):
        if replace_count <= 0:
            break
        if s_list[i] == ')':
            s_list[i] = '('
            replace_count -= 1

s_balanced = ''.join(s_list)

balance = 0
closing_errors = 0
for c in s_balanced:
    if c == '(':
        balance += 1
    else:
        balance -= 1
    if balance < 0:
        closing_errors += 1
        balance = 0

balance = 0
opening_errors = 0
for c in reversed(s_balanced):
    if c == ')':
        balance += 1
    else:
        balance -= 1
    if balance < 0:
        opening_errors += 1
        balance = 0


pairs = min(closing_errors, opening_errors)
cost += pairs * min(a, 2 * b) + (closing_errors + opening_errors - 2 * pairs) * b

print(cost)