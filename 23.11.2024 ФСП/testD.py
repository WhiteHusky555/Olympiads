def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_two_primes(n):
    for i in range(2, n + 1):
        if is_prime(i) and is_prime(n - i):
            return i, n - i

def encode(n):
    primes = find_two_primes(n)
    print(primes[0], primes[1])


def decode(a, b):
    print(a + b)

inter = str(input())
if inter == "encode":
    n = int(input())
    for _ in range(n):
        n = int(input())
        encode(n)
else:
    n = int(input())
    for _ in range(n):
        a, b = list(map(int, input().split()))
        decode(a, b)
