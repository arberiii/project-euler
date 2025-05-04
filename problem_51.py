from collections import defaultdict, Counter
from itertools import combinations
from typing import List, Set, Dict


def all_primes_up_to(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    return [i for i in range(2, n + 1) if sieve[i]]

def mask_digit_combinations(number: int) -> List[str]:
    num_str = str(number)
    results = set()
    counts = Counter(num_str)
    
    for digit, count in counts.items():
        if count >= 3:
            indices = [i for i, d in enumerate(num_str) if d == digit]
            for combo in combinations(indices, 3):
                chars = list(num_str)
                for idx in combo:
                    chars[idx] = '*'
                results.add(''.join(chars))
    
    return list(results)

def find_min_prime_with_eight_family() -> int:
    UPPER_LIMIT = 1_000_000
    TARGET_FAMILY_SIZE = 8
    
    primes = set(all_primes_up_to(UPPER_LIMIT))
    
    mask_to_primes: Dict[str, List[int]] = defaultdict(list)
    for prime in primes:
        for mask in mask_digit_combinations(prime):
            mask_to_primes[mask].append(prime)
    
    masks_with_eight_primes = {
        mask for mask, primes in mask_to_primes.items() 
        if len(primes) == TARGET_FAMILY_SIZE
    }
    
    return min(
        min(primes) 
        for mask in masks_with_eight_primes 
        for primes in [mask_to_primes[mask]]
    )

def main() -> None:
    result = find_min_prime_with_eight_family()
    print(f"The smallest prime in an 8-prime family is: {result}")

if __name__ == "__main__":
    main()
