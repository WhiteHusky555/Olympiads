n, a, b = (map(int, input().split()))
stack = list(input().strip())
money = 0
balance = 0
stack_psp = []
for i in range(0, len(stack)-2):
    if stack[i] == "(":
        if stack[i+1] == ')':
            pass
        elif ")" in stack[i+1:]:
            stack[i+1], stack[stack.index(')')] = stack[stack.index(')')], stack[i+1]