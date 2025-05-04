def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result
                

def main() -> None:
    total = 0
    for i in range(2, 1_000_001):
        total += euler_totient(i)
    print(f"Total sum of Euler's totient function from 2 to 1,000,000: {total}")

if __name__ == "__main__":
    main()
  
