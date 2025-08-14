from functools import lru_cache
@lru_cache()
def fact(n: int):
    if n==1:
        return 1
    return n*fact(n-1)





numb_fact: int = int(input())
zeros: int = 0
