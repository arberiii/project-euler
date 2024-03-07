fifty_million = 50_000_000


def get_all_primes(lower: int) -> list[int]:
    primes = []
    for i in range(2, lower + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


all_primes = get_all_primes(7072)

count = 0
seen = set()

for square in all_primes:
    for cube in all_primes:
        if square ** 2 + cube ** 3 > fifty_million:
            break
        for fourth in all_primes:
            v = square ** 2 + cube ** 3 + fourth ** 4
            if v < fifty_million:
                seen.add(v)
            else:
                break

print(len(seen))
