
n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i + 2, n):
        sub_array = a[i:j + 1]

        for k in range(len(sub_array)):
            for l in range(k + 1, len(sub_array)):
                for m in range(l + 1, len(sub_array)):
                    if sub_array[l] - sub_array[k] == sub_array[m] - sub_array[l]:
                        count += 1
                        break
                else:
                    continue
                break
            else:
                continue
            break
print(count)
