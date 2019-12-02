#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Day 2: 1202 Program Alarm
https://adventofcode.com/2019/day/2
"""


def nic(ic):
    """ Intcode (ic) interpreter."""
    for i in range(0, len(ic), 4):
        opcode = ic[i]

        if opcode == 99:
            return ic
        elif opcode == 1 or opcode == 2:
            fx = ic[i + 1]  # first input index
            sx = ic[i + 2]  # second input index
            rx = ic[i + 3]  # result index

            ic[rx] = ic[fx] + ic[sx] if opcode == 1 else ic[fx] * ic[sx]

    return ic


if __name__ == "__main__":
    assert nic([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert nic([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert nic([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert nic([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    f = "./day-02/input.txt"
    intcode = open(f).readline().strip().split(",")
    intcode = list(map(int, intcode))

    # Restore code
    intcode[1] = 12
    intcode[2] = 2
    out = nic(intcode)
    print(out[0])
