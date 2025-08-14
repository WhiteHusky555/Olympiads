def count_digits(x):
    if x>10 and x%10!=0:
        return len(str(x))+count_digits((x%10)*10)
    elif x>=10 and x%10==0:
        return len(str(x))+count_digits(x-10)
    elif x==1:
        return 1
    elif x==0:
        return -1

    elif x<10 and x!=1 and x!=0:
        return 2

x=int(input())
print(count_digits(x))