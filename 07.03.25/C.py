#14
def fib(x: int):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

def decode(x: str):
    sum=0
    for i in range(len(x)):
        ii=len(x)-i
        sum+=int(x[i])*fib(ii)
    return sum

print(decode('101000101010100010100010101010'))