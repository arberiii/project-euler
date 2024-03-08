from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


ORIGIN = Point(0, 0)
UPPER_BOUND = 50


def is_right_triangle(p1: Point, p2: Point, p3: Point) -> bool:
    sides = [
        (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2,
        (p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2,
        (p3.x - p1.x) ** 2 + (p3.y - p1.y) ** 2
    ]
    sides.sort()
    if sides[0] + sides[1] == sides[2]:
        return True
    return False


def is_possible_triangle(p1: Point, p2: Point, p3: Point) -> bool:
    if p1.x == p2.x == p3.x:
        return False
    if p1.y == p2.y == p3.y:
        return False
    if p1 == p2 or p2 == p3 or p1 == p3:
        return False
    return True


def count_right_angle_triangles():
    count = 0
    for x_1 in range(0, UPPER_BOUND + 1):
        for y_1 in range(0, UPPER_BOUND + 1):
            for x_2 in range(0, UPPER_BOUND + 1):
                for y_2 in range(0, UPPER_BOUND + 1):
                    point_1 = Point(x_1, y_1)
                    point_2 = Point(x_2, y_2)
                    if not is_possible_triangle(ORIGIN, point_1, point_2):
                        continue
                    if is_right_triangle(ORIGIN, point_1, point_2):
                        count += 1

    return count // 2


print(count_right_angle_triangles())
