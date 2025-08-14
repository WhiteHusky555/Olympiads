def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5
    d = 2

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d
    return prime

def encode(x):
    if is_prime(x):
        print(x, x)
    else:
        for i in range(1, int(x**(1/2))+1):
            if is_prime(i) and is_prime(x-i):
                print(i, x-i)
                break

def decode(a, b):
    if a>b:
        print(a-b)
    else:
        print(a+b)

inter=str(input())
if inter=="encode":
    n=int(input())
    for i in range(n):
        x=int(input())
        encode(x)
else:
    n=int(input())
    for i in range(n):
        a, b = list(map(int, input().split()))
        decode(a, b)