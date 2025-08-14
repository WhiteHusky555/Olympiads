x=int(input())
ls = set()
ls.add(1)
ls.add(x)
for i in range(0, x+1, 10):
    ls.add(i)
ls.remove(0)
st=''
for x in ls:
    st+=str(x)
print(len(st))