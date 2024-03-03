from dataclasses import dataclass
from decimal import Decimal
import math


@dataclass
class Number:
    base: int
    exponent: int


with open('0099_base_exp.txt') as f:
    numbers_un_formatted = [line.rstrip() for line in f]

numbers = [Number(base=int(x.split(',')[0]), exponent=int(x.split(',')[1])) for x in numbers_un_formatted]

max_number = numbers[0]
for number in numbers:
    if number.exponent * math.log(number.base) > max_number.exponent * math.log(max_number.base):
        max_number = number

line_number = 1
for i in range(len(numbers)):
    if numbers[i] == max_number:
        line_number = i + 1
        break

print(line_number)
