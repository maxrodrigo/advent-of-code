#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Day 2: 1202 Program Alarm
https://adventofcode.com/2019/day/2
"""

from itertools import product


def nic(intcode, n=None, v=None):
    """ Intcode (ic) interpreter."""
    # Grab a copy of intcode since list are mutable.
    ic = intcode[:]

    ic[1] = n or ic[1]
    ic[2] = v or ic[2]

    for i in range(0, len(ic), 4):
        opcode = ic[i]

        if opcode == 99:
            return ic
        elif opcode == 1 or opcode == 2:
            fa = ic[i + 1]  # first param address
            sa = ic[i + 2]  # second param address
            ra = ic[i + 3]  # result address

            ic[ra] = ic[fa] + ic[sa] if opcode == 1 else ic[fa] * ic[sa]
    return ic


if __name__ == "__main__":
    assert nic([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert nic([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert nic([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert nic([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    f = "./day-02/input.txt"
    intcode = open(f).readline().strip().split(",")
    intcode = list(map(int, intcode))

    # part 1
    out = nic(intcode, 12, 2)
    print(f"Part 1: {out[0]}")

    # part 2
    # Generate all possible input tuples
    for n, v in product(range(0, 100), range(0, 100)):
        out = nic(intcode, n, v)
        if out[0] == 19690720:
            res = 100 * n + v
            print(f"Part 2: {res}")
            break
