#!/usr/bin/env python3

# Created by Joseph Kwon
# Created on Sep 16, 2022
# This program does basic math

import math


def main():
    # this function does basic math
    print(9 + 2)
    # print the "question" as well
    print("7-3={}".format(7 - 3))
    print("4/2={}".format(4 / 2))
    print("9+2={}".format(9 + 2))
    print("4+4/2={}".format(4 + 4 / 2))
    print("5/2={}".format(5 / 2))
    print("3*3={}".format(3 * 3))
    print(math.sqrt(9))
    print("5+2**3={}".format(5 + 2**3))  # exponent

    print("5+2^3={}".format(5 + 2 ^ 3))  # bitwise operand


if __name__ == "__main__":
    main()
