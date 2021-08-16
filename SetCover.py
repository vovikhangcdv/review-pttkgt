#!/usr/bin/env python3

import sys
from functools import reduce

if sys.version_info < (3, 9):
    sys.exit("Python {}.{} or later is required.\n".format(3, 9))


def SetCover():
    N = int(input("How many set? "))
    A = [None for _ in range(N)]
    for i in range(N):
        L = input("Set {}: ".format(i + 1)).strip().split(' ')
        A[i] = set([int(x) for x in L])

    U = set(reduce(lambda R, S: R | S, A, set()))
    print("U = ", U)

    R = set()
    Chosen = set()
    while len(R) < len(U):
        Max = 0
        choice = 0
        for i in range(1, N + 1):
            if i in Chosen:
                continue
            NextR = R | A[i - 1]
            if len(NextR) > Max:
                Max = len(NextR)
                choice = i
        Chosen.add(choice)
        R = R | A[choice - 1]
        print("Choice set {}, R = {}".format(choice, R))

    print("Cover set: {}".format(Chosen))


if __name__ == "__main__":
    SetCover()
