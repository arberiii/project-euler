from fractions import Fraction

d = 12_000


def count_fractions_on_range(fr_1: Fraction, fr_2: Fraction):
    count = 0
    for denominator in range(1, d + 1):
        for numerator in range(1, denominator):
            fr = Fraction(numerator, denominator)
            if fr.numerator != numerator or fr.denominator != denominator:
                continue

            if fr > fr_2:
                break

            if fr_1 < fr < fr_2:
                count += 1

    return count


print(count_fractions_on_range(Fraction(1, 3), Fraction(1, 2)))
