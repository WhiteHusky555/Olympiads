def is_on_edge(x: int, y: int):
    vertices = [
        (16, 15), (-24, 24), (-36, 31), (-44, -27), (12, 14),
        (-101, 45), (-50, 6), (34, -58), (-25, -26), (-10, 32)
    ]
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # следующая вершина (с замыканием)
        dx = x2 - x1
        dy = y2 - y1
        # Проверка коллинеарности и принадлежности отрезку
        cross = (x - x1) * dy - (y - y1) * dx
        if cross != 0:
            continue
        # Параметры точки на отрезке [0, 1]
        if dx == 0 and dy == 0:  # вырожденное ребро
            return (x, y) == (x1, y1)
        t_x = (x - x1) / dx if dx != 0 else 0
        t_y = (y - y1) / dy if dy != 0 else 0
        t = t_x if dx != 0 else t_y
        if 0 <= t <= 1:
            return True
    return False

count = 0
for x in range(-100, 101):
    for y in range(-100, 101):
        if is_on_edge(x, y):
            count += 1
print(count)