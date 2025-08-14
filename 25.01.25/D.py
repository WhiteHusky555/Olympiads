def is_balanced(num):
    return len(str(num)) == sum(int(digit) for digit in str(num))


n = int(input().strip())
balanced_numbers = []
current_number = 1
while len(balanced_numbers) < n:
    if is_balanced(current_number):
        balanced_numbers.append(current_number)
    current_number += 1
print(*balanced_numbers)
