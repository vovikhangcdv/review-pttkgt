#!/usr/bin/env python3


def BinPacking(BestFit=False, Decreasing=False):
    """Change two parameters above to get specific algorithm you want"""
    SIZE = int(input("Max size of a bin: "))
    N = int(input("How many object?"))
    L = [None for _ in range(N)]
    for i in range(N):
        L[i] = [int(input("L[{}] = ".format(i + 1))), -i - 1]

    if Decreasing:
        L.sort(reverse=True)

    O = []
    B = []
    if BestFit:
        for s, i in L:
            idx = len(B)
            Max = 0
            for k in range(len(B)):
                if B[k] + s <= SIZE and B[k] > Max:
                    Max = B[k]
                    idx = k
            if idx == len(B):
                B.append(s)
                O.append([-i])
            else:
                B[idx] += s
                O[idx].append(-i)
    else:
        for s, i in L:
            for k in range(len(B)):
                if B[k] + s <= SIZE:
                    B[k] += s
                    O[k].append(-i)
                    break
            else:
                B.append(s)
                O.append([-i])

    print("\nResult:")
    for i in range(len(B)):
        print("Bin {}: used {}/{}, object = {}".format(i + 1, B[i], SIZE, O[i]))


if __name__ == "__main__":
    BinPacking(False, False)
