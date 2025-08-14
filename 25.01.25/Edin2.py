x=int(input())
count=0
for i in range(1, x+1):
    if i==1 or i%10==0 or i==x:
        count+=len(str(i))
    if i==x:
        break
print(count)