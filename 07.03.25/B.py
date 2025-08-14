#13
from math import sqrt
arr=[]
for i in range(1, 50):
    for j in range(1, 50):
        for k in range(1, 50):
            if (i+j+k) == 100:

                p = 100//2
                if (p*(p-i)*(p-j)*(p-k))>0:
                    #print(i, j, k)
                    S = sqrt(p*(p-i)*(p-j)*(p-k))
                    arr.append([S, i, j, k])
print(sorted(arr, key=lambda x: x[0]))