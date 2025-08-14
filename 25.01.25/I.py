m=int(input())
mines=[]
for i in range(m):
    mines.append(list(map(int, input().split())))
ls=list(map(int, input().split()))
start=ls[0::2]
finish=ls[2::]
time_need=abs(start[0]-finish[0])+abs(start[1]-finish[1])
time_have=float('inf')
for i in range(m):
    if abs(mines[i][0]-finish[0])+abs(mines[i][1]-finish[1])+1<time_have or abs(mines[i][0]-start[0])+abs(mines[i][1]-start[1])+1<time_have:
        time_have=min(abs(mines[i][0]-finish[0])+abs(mines[i][1]-finish[1]), abs(mines[i][0]-start[0])+abs(mines[i][1]-start[1]))
if time_need>time_have:
    print('NO')
else:
    print('YES')
