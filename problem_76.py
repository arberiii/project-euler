cached = {}


def get_possible_summation(final_sum: int, top: int) -> int:
    if (final_sum, top) in cached:
        return cached[(final_sum, top)]
    total = 0
    for i in range(1, top + 1):
        if i == final_sum:
            total += 1
        elif i > final_sum:
            continue
        else:
            total += get_summation(final_sum - i, i)
    cached[(final_sum, top)] = total
    return total


print(get_possible_summation(5, 4))
