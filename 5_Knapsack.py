#!/usr/bin/env python3


def KnapsackUnique():
    """Only one item for each type"""
    N = int(input("How many item? "))
    S = [0 for _ in range(N)]
    V = [0 for _ in range(N)]
    for i in range(N):
        S[i] = int(input("Size[{}] = ".format(i + 1)))
        V[i] = int(input("Value[{}] = ".format(i + 1)))
    M = int(input("Size of your bag: "))

    C = [0 for _ in range(M + 1)]
    B = ['-' for _ in range(M + 1)]
    C[0] = 0
    for idx in range(N):
        size, value = S[idx], V[idx]
        for i in range(size, M + 1)[::-1]:
            if (i == size or C[i - size] > 0) and C[i] < C[i - size] + value:
                C[i] = C[i - size] + value
                B[i] = chr(65 + idx)
        for i in range(size, M + 1):
            if C[i] < C[i - 1]:
                C[i] = C[i - 1]
                B[i] = B[i - 1]
        print("Step {}: Item {}, size = {}, value = {}".format(idx + 1, chr(65 + idx), size, value))
        print("      ", end='')
        for i in range(1, M + 1):
            print("{:>4}".format(i), end='')
        print("\nCost: ", end='')
        for c in C[1:]:
            print("{:>4}".format(c), end='')
        print("\nBest: ", end='')
        for b in B[1:]:
            print("{:>4}".format(b), end='')
        print()
        print('-' * 10)

    R = M
    L = []
    while R > 0 and B[R] != '-':
        L.append(B[R])
        R -= S[ord(L[-1]) - 65]
    print("Best choice: {{{}}}".format(", ".join(L[::-1])))


def KnapsackUnlimited():
    """Infinity item for each type"""
    N = int(input("How many item? "))
    S = [0 for _ in range(N)]
    V = [0 for _ in range(N)]
    for i in range(N):
        S[i] = int(input("Size[{}] = ".format(i + 1)))
        V[i] = int(input("Value[{}] = ".format(i + 1)))
    M = int(input("Size of your bag: "))

    C = [0 for _ in range(M + 1)]
    B = ['-' for _ in range(M + 1)]
    C[0] = 0
    for idx in range(N):
        size, value = S[idx], V[idx]
        for i in range(size, M + 1):
            if (i == size or C[i - size] > 0) and C[i] < C[i - size] + value:
                C[i] = C[i - size] + value
                B[i] = chr(65 + idx)
            if C[i] < C[i - 1]:
                C[i] = C[i - 1]
                B[i] = B[i - 1]
        print("Step {}: Item {}, size = {}, value = {}".format(idx + 1, chr(65 + idx), size, value))
        print("      ", end='')
        for i in range(1, M + 1):
            print("{:>4}".format(i), end='')
        print("\nCost: ", end='')
        for c in C[1:]:
            print("{:>4}".format(c), end='')
        print("\nBest: ", end='')
        for b in B[1:]:
            print("{:>4}".format(b), end='')
        print()
        print('-' * 10)

    R = M
    L = []
    while R > 0 and B[R] != '-':
        L.append(B[R])
        R -= S[ord(L[-1]) - 65]
    print("Best choice: {{{}}}".format(", ".join(L[::-1])))


if __name__ == "__main__":
    # KnapsackUnique()
    KnapsackUnlimited()
