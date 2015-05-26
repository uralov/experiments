# -*- coding: utf-8 -*-
def get_number_exponentiation_list(number, exponentiation):
    for x in range(exponentiation):
        yield number ** x

# for gen_item in get_number_exponentiation_list(2, 10):
#     print gen_item


def fibonachi(count_iterations):
    a, b = 0, 1
    while a < count_iterations:
        yield a
        a, b = b, a + b

for fib in fibonachi(10):
    print(fib)