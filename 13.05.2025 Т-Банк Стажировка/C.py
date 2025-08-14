def arr_vars(x):
    arr = [x]
    while x>0:
        x //= 2
        arr.append(x)
        #print(arr)
    return arr

n = int(input().strip())
arr = list(map(int, input().split()))
variants = arr_vars(max(arr))
#print(variants)
max_vars = 0
arr = sorted(arr, reverse=True)
#print(arr)
while (arr and variants):
    if arr.pop(0) >= variants.pop(0):
        #print(arr, variants)
        max_vars+=1
print(max_vars)
