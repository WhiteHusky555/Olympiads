def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    s = data[1].strip()

    left = [-1] * (n + 1)
    right = [-1] * (n + 1)

    head = 0

    for i in range(1, n + 1):
        ch = s[i - 1]
        if ch == 'L':
            left_i = left[i - 1]
            right_i = i - 1
            left[i] = left_i
            right[i] = right_i

            if left_i != -1:
                right[left_i] = i
            left[i - 1] = i

            if left[i - 1] == -1 or i - 1 == head:
                head = i
        else:  # ch == 'R'
            left_i = i - 1
            right_i = right[i - 1]
            left[i] = left_i
            right[i] = right_i

            if right_i != -1:
                left[right_i] = i
            right[i - 1] = i

    result = []
    current = head
    while current != -1:
        result.append(str(current))
        current = right[current]

    print(" ".join(result))


if __name__ == "__main__":
    main()