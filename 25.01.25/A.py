x = int(input().strip())
str_x = str(x)
max_number = x

for i in range(3):
    for j in range(i + 1, 3):
        swapped_str = list(str_x)
        swapped_str[i], swapped_str[j] = swapped_str[j], swapped_str[i]
        swapped_number = int(''.join(swapped_str))
        if swapped_number > max_number:
            max_number = swapped_number
print(max_number)
