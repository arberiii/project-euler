def count_rectangles(a, b: int) -> int:
    total = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            total += (a - i + 1) * (b - j + 1)
    return total


all_results = {}
closest = None
closest_diff = None
for i in range(1, 2000):
    for j in range(1, 2000):
        res = count_rectangles(i, j)
        if res > 2_001_000:
            break

        diff = abs(2_000_000 - res)
        if closest is None or diff < closest_diff:
            closest = (i, j)
            closest_diff = diff

print(closest[0] * closest[1])


