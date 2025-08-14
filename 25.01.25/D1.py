from itertools import permutations

def generate_cur_len(x):
    balanced_numbers = []
    unique_numbers = set(p for p in permutations([i for i in range(0, x)]))
    print(unique_numbers)
    for number in unique_numbers:
        if len(str(number)) == sum(int(digit) for digit in str(number)):
            balanced_numbers.append(number)
    return list(balanced_numbers)

n = int(input().strip())
balanced_numbers = []
current_len = 1

while len(balanced_numbers) < n:
    balanced_numbers.extend(generate_cur_len(current_len))
    current_len += 1

# Удаляем дубликаты и сортируем
balanced_numbers = sorted(set(balanced_numbers))

for i in range(n):
    print(balanced_numbers[i])
