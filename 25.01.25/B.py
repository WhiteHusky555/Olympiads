from itertools import permutations

digits = input().strip().split()

unique_numbers = set(int(''.join(p)) for p in permutations(digits))

sorted_numbers = sorted(unique_numbers)
for number in sorted_numbers:
    print(number)
