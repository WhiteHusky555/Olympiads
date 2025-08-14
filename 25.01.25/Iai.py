import math

def can_reach(n, mines, start, target):
    x_s, y_s = start
    x_t, y_t = target


    distance_to_target = math.sqrt((x_t - x_s) ** 2 + (y_t - y_s) ** 2)

    for (x_i, y_i) in mines:

        distance_to_mine_start = math.sqrt((x_i - x_s) ** 2 + (y_i - y_s) ** 2)

        distance_to_mine_target = math.sqrt((x_i - x_t) ** 2 + (y_i - y_t) ** 2)

        if distance_to_mine_start <= distance_to_target or distance_to_mine_target <= distance_to_target:
            return "NO"

    return "YES"


n = int(input().strip())
mines = [tuple(map(int, input().strip().split())) for _ in range(n)]
x_s, y_s, x_t, y_t = map(int, input().strip().split())


result = can_reach(n, mines, (x_s, y_s), (x_t, y_t))

print(result)
