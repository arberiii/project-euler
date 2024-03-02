from fractions import Fraction

fr_3_7 = Fraction(3, 7)

current_numerator = 3
closest = Fraction(2, 5)
for denominator in range(8, 1_000_001):
    new_fr = Fraction(current_numerator + 1, denominator)
    if new_fr > fr_3_7:
        continue

    while Fraction(current_numerator + 1, denominator) < fr_3_7:
        current_numerator += 1

    if Fraction(current_numerator, denominator) > closest:
        closest = Fraction(current_numerator, denominator)

print(closest)
