# -*- coding: utf-8 -*-
x = int('1001', 2)
y = int('1110', 2)

bit_or = bin(x | y)
print(bit_or)

bit_and = bin(x & y)
print(bit_and)

bit_xor = bin(x ^ y)
print(bit_xor)

bit_invert = bin(~x)
print(bit_invert)


def double_multiplier(number, factor):
    return number << factor

print(double_multiplier(4, 2))