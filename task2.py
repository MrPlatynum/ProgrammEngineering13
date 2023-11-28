#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def harmonic_mean(*args):
    if not args:
        return None

    reciprocal_sum = 0
    for arg in args:
        reciprocal_sum += 1 / arg

    return len(args) / reciprocal_sum


if __name__ == "__main__":
    values = list(int(i) for i in input("Введите числа: ").split())

    result = harmonic_mean(*values)
    if result is None:
        print("Список аргументов пуст, среднее гармоническое не может быть вычислено.")
    else:
        print(f"Среднее гармоническое: {result}")
