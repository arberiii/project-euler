from dataclasses import dataclass


@dataclass
class PolygonNumber:
    sides: int
    first_two_digits: int
    last_two_digits: int
    incoming_edges: set[str]
    outgoing_edges: set[str]

    def to_string(self) -> str:
        return f"p{self.sides}_{self.first_two_digits}{self.last_two_digits}"


def generate_all_numbers() -> list[PolygonNumber]:
    all_numbers = []
    n = 1
    while True:
        p_3 = n * (n + 1) // 2
        p_4 = n ** 2
        p_5 = n * (3 * n - 1) // 2
        p_6 = n * (2 * n - 1)
        p_7 = n * (5 * n - 3) // 2
        p_8 = n * (3 * n - 2)
        has_any = False
        if p_3 >= 1000 and p_3 < 10000:
            has_any = True
            all_numbers.append(PolygonNumber(3, p_3 // 100, p_3 % 100, set(), set()))

        if p_4 >= 1000 and p_4 < 10000:
            has_any = True
            all_numbers.append(PolygonNumber(4, p_4 // 100, p_4 % 100, set(), set()))

        if p_5 >= 1000 and p_5 < 10000:
            has_any = True
            all_numbers.append(PolygonNumber(5, p_5 // 100, p_5 % 100, set(), set()))

        if p_6 >= 1000 and p_6 < 10000:
            has_any = True
            all_numbers.append(PolygonNumber(6, p_6 // 100, p_6 % 100, set(), set()))

        if p_7 >= 1000 and p_7 < 10000:
            has_any = True
            all_numbers.append(PolygonNumber(7, p_7 // 100, p_7 % 100, set(), set()))

        if 1000 <= p_8 < 10000:
            has_any = True
            all_numbers.append(PolygonNumber(8, p_8 // 100, p_8 % 100, set(), set()))

        if not has_any and n > 50:
            break
        n += 1

    return all_numbers


def build_graph(numbers: list[PolygonNumber]) -> list[PolygonNumber]:
    for number_1 in numbers:
        for number_2 in numbers:
            if number_1.sides == number_2.sides:
                continue
            if number_1.last_two_digits == number_2.first_two_digits:
                number_1.outgoing_edges.add(number_2.to_string())
                number_2.incoming_edges.add(number_1.to_string())
    return numbers


def _build_cycle(
        numbers: list[PolygonNumber],
        current_cycle: list[PolygonNumber],
        cycles: list[list[PolygonNumber]],
) -> None:
    if len(current_cycle) == 6:
        if current_cycle[0].first_two_digits == current_cycle[-1].last_two_digits:
            cycles.append(current_cycle)
        return

    last_number = current_cycle[-1]
    for next_number in numbers:
        sides_in_cycle = {number_c.sides for number_c in current_cycle}
        if next_number.sides in sides_in_cycle:
            continue
        if last_number.last_two_digits == next_number.first_two_digits:
            _build_cycle(numbers, current_cycle + [next_number], cycles)


numbers_ = generate_all_numbers()
numbers_ = build_graph(numbers_)

all_cycles = []
for number_ in numbers_:
    if number_.sides != 3:
        continue

    _build_cycle(numbers_, [number_], all_cycles)

s = 0
for number_ in all_cycles[0]:
    s += number_.first_two_digits * 100 + number_.last_two_digits

print(s)
