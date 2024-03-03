ten_power_10 = 10 ** 10

multiplier = 28433
power = 2
exponent = 7830457
while exponent > 0:
    if exponent % 2 == 1:
        multiplier = multiplier * power % ten_power_10
        exponent -= 1
    power = power * power % ten_power_10
    exponent //= 2

print(multiplier + 1)
