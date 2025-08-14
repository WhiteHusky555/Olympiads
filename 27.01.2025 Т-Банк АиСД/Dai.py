def calculate_min_distance(n, x, q, queries):
    x.sort()  # Сортируем массив координат
    results = []

    for a, b in queries:
        min_distance = float('inf')

        # Проверяем все уникальные значения y в x
        for i in range(n):
            y = x[i]
            total_distance = 0

            # Вычисляем сумму расстояний для данного y
            for j in range(n):
                if y >= x[j]:
                    total_distance += (y - x[j]) * a
                else:
                    total_distance += (x[j] - y) * b

            min_distance = min(min_distance, total_distance)

        results.append(min_distance)

    return results


# Чтение входных данных
n = int(input().strip())
x = list(map(int, input().strip().split()))
q = int(input().strip())
queries = [tuple(map(int, input().strip().split())) for _ in range(q)]

# Получение результатов
results = calculate_min_distance(n, x, q, queries)

# Вывод результатов
for result in results:
    print(result)

#2 вариант

def distance(x, y, a, b):
  if y >= x:
    return (y - x) * a
  else:
    return (x - y) * b

def calculate_min_distance(x_values, a, b):
  min_sum = float('inf')
  for y in range(max(x_values) + 1):
    current_sum = sum(distance(x, y, a, b) for x in x_values)
    min_sum = min(min_sum, current_sum)
  return min_sum


n = int(input())
x_values = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    min_distance = calculate_min_distance(x_values, a, b)
    print(min_distance)

