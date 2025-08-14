#15
#print('a b c F')
#F=11110100
f='1'*8
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            F=((((not a) or (not b)) and (b or c)) or (not a))
            #print(f'{a} {b} {c} {int(F)}')
            #print(f'{int(F)}', end='')
print(int('11110100', 2))
