#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def product_between_zeros(*args):
    zero_count = 0
    result = 1

    for arg in args:
        if arg == 0:
            zero_count += 1
            if zero_count == 2:
                return result
        elif zero_count == 1:
            result *= arg

    return None


if __name__ == "__main__":
    values = list(int(i) for i in input("Введите числа: ").split())

    result = product_between_zeros(*values)
    if result is None:
        print("Нельзя вычислить произведение аргументов между первым и вторым нулями.")
    else:
        print(f"Произведение аргументов между первым и вторым нулями: {result}")
