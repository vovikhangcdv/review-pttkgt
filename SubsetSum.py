#!/usr/bin/env python3


def SubsetSum():
    A = input("Your set (ex. 1 2 3): ").strip().split(' ')
    A = [int(x) for x in A]
    M = int(input("Target sum: "))
    L = [0] + [None for _ in range(M)]
    for x in A:
        for i in range(x, M + 1)[::-1]:
            if (L[i - x] != None) and (L[i] == None):
                L[i] = x
    if L[M]:
        S = set()
        while M != 0:
            S.add(L[M])
            M -= L[M]
        print("Solution:", S)
    else:
        print("No solution!")


if __name__ == "__main__":
    SubsetSum()
