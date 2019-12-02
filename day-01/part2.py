#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1/2 - Fuel Calculator
https://adventofcode.com/2019/day/1#part2
"""


def fuel(mass):
    """ Calculates recursively the amount of fuel needed for the given mass. """

    total = 0

    while True:
        mass = mass // 3 - 2
        if mass > 0:
            total += mass
        else:
            break

    return total


def readable(file):
    total = 0
    # read is open's default mode
    with open(file) as f:
        for l in f:
            mass = int(l.strip())
            module_fuel = fuel(mass)
            total = total + module_fuel
    return total


def compact(f):
    return sum([fuel(int(l.strip())) for l in open(f)])


if __name__ == "__main__":
    f = "./day-01/input.txt"
    fuel = compact(f)
    print(fuel)
