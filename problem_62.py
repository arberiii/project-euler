from collections import defaultdict
import json


def get_cube_counter(number) -> defaultdict:
    cube = number ** 3
    counter = defaultdict(int)
    for digit in str(cube):
        counter[digit] += 1

    return counter


def get_dict_key(counter) -> str:
    return json.dumps(counter, sort_keys=True)


all_counters = defaultdict(list)
for number in range(10000):
    counter = get_cube_counter(number)
    all_counters[get_dict_key(counter)].append(number)

all_perfect = []
for counter, numbers in all_counters.items():
    if len(numbers) == 5:
        all_perfect.append(numbers)

m = None
for numbers in all_perfect:
    all_cubes = [number ** 3 for number in numbers]
    if m is None or min(all_cubes) < m:
        m = min(all_cubes)

print(m)
