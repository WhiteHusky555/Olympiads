s = input().strip()
count = {}

for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i:j + 1]
        # print(substring)
        for char in substring:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

for char in sorted(count.keys()):
    print(f"{char}: {count[char]}")

