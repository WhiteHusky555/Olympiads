PRIME, MOD = 31, 10**9 + 7

def manacher_odd(s):
    n = len(s)
    d = [1] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            d[i] = min(r - i + 1, d[l + r - i])
        while i - d[i] >= 0 and i + d[i] < n and s[i - d[i]] == s[i + d[i]]:
            d[i] += 1
        if i + d[i] - 1 > r:
            l, r = i - d[i] + 1, i + d[i] - 1
    return d

def manacher_even(s):
    n = len(s)
    d = [0] * n
    l, r = -1, -1
    for i in range(n - 1):
        if i < r:
            d[i] = min(r - i, d[l + r - i - 1])
        while i - d[i] >= 0 and i + d[i] + 1 < n and s[i - d[i]] == s[i + d[i] + 1]:
            d[i] += 1
        if i + d[i] > r:
            l, r = i - d[i] + 1, i + d[i]
    return d



s=str(input()).strip()
for i in range(len(s)):
    st = s[:i]+s[i+1:]
    count=sum(manacher_even(st))+sum(manacher_odd(st))
    if count>len(st):
        print("YES")
        break
else:
    print("NO")