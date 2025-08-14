x=int(input())
len_st=0
len_st+=1
if x>10 and x%10!=0:
    len_st+=len(str(x))
for i in range(10, x+1, 10):
    len_st+=len(str(i))
print(len_st)