#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geometric_mean(*args):
    if not args:
        return None

    product = 1
    for arg in args:
        product *= arg

    return product ** (1 / len(args))


if __name__ == "__main__":
    values = list(int(i) for i in input("Введите числа: ").split())

    result = geometric_mean(*values)
    if result is None:
        print("Список аргументов пуст, среднее геометрическое не может быть вычислено.")
    else:
        print(f"Среднее геометрическое: {result}")
