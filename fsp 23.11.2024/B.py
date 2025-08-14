def fibonacci_list(n):
    sequence = [1, 1]
    while len(sequence) < n+1:
        sequence.append(sequence[-1] + sequence[-2])
    # print(sequence)
    return sequence

def fib_triangles(fib_list):
    unique_triangles = list()
    for i in range(len(fib_list)):
        for j in range(i, len(fib_list)):
            for k in range(j, len(fib_list)):
                if fib_list[i] + fib_list[j] > fib_list[k] and sorted([fib_list[i], fib_list[j], fib_list[k]]) not in unique_triangles:
                    unique_triangles.append(sorted([fib_list[i], fib_list[j], fib_list[k]]))
    # print(unique_triangles)
    return len(unique_triangles)

n = int(input())
fib_list = fibonacci_list(n)
print(fib_triangles(fib_list))
