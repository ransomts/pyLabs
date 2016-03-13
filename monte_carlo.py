#!/usr/bin/env python


def correct_monte_carlo(n):
    from math import sqrt
    from random import random
    count_inside = 0
    for count in range(0, n):
        x = random()
        y = random()
        d = sqrt(x**2 + y**2)
        if d < 1: count_inside += 1
    count += 1
    return 4.0 * count_inside / count

print correct_monte_carlo(1000)
