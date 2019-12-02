#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1/1 - Fuel Calculator
https://adventofcode.com/2019/day/1
"""


def readable(file):
    total = 0
    # read is open's default mode
    with open(file) as f:
        for l in f:
            mass = int(l.strip())
            fuel = mass // 3 - 2
            total = total + fuel
    return total


def compact(f):
    return sum([int(l.strip()) // 3 - 2 for l in open(f)])


if __name__ == "__main__":
    f = "./day-01/input.txt"
    r = readable(f)
    c = compact(f)
    print(f"r: {r} | c: {c}")
