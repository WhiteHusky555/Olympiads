import random
arr = []
for i in range(100):
    arr.append(random.randint(-10, 10))
print(*arr)