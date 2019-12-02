#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Day 1: The Tyranny of the Rocket Equation
https://adventofcode.com/2019/day/1
"""


def fuel_total(m):
    """ Calculates recursively the amount of fuel needed for the given mass. """
    total = 0

    while True:
        m = fuel(m)
        if m > 0:
            total += m
        else:
            break

    return total


def fuel(m):
    """ Calculates the amount of fuel needed for the given mass. """
    return m // 3 - 2


if __name__ == "__main__":
    f = "./day-01/input.txt"
    masses = [int(m.strip()) for m in open(f)]

    # part 1
    assert fuel(12) == 2
    assert fuel(14) == 2
    assert fuel(1969) == 654
    assert fuel(100756) == 33583

    req = sum([fuel(m) for m in masses])
    print(req)

    # part 2
    assert fuel_total(14) == 2
    assert fuel_total(1969) == 966
    assert fuel_total(100756) == 50346

    req = sum([fuel_total(m) for m in masses])
    print(req)
