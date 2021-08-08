#!/usr/bin/env python3

oo = 10 ** 10


def MatrixChainMultiplication():
    N = int(input("How many matrix?: "))
    P = [0 for _ in range(N + 1)]
    for i in range(N + 1):
        P[i] = int(input("P[{}] = ".format(i)))

    M = [[oo for _ in range(N + 1)] for _ in range(N + 1)]
    S = [[oo for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        M[i][i] = 0
    for l in range(1, N + 1):
        for i in range(1, N - l + 2):
            j = i + l - 1
            p = P[i - 1] * P[j]
            for k in range(i, j):
                t = M[k][i] + M[j][k + 1] + P[k] * p
                if t < M[j][i]:
                    M[j][i] = t
                    S[j][i] = k

    print("Matrix M:")
    for m in M[1:][::-1]:
        for x in m[1:]:
            x = str(x) if x < oo else ""
            print("{:>10}".format(x), end='')
        print()

    print("Matrix S:")
    for s in S[1:][::-1]:
        for x in s[1:]:
            x = str(x) if x < oo else ""
            print("{:>10}".format(x), end='')
        print()

    print("Best strategy: " + FindTheBest(S, 1, N))


def FindTheBest(S, i, j):
    if i == j:
        return chr(64 + i)
    return '(' + FindTheBest(S, i, S[j][i]) + FindTheBest(S, S[j][i] + 1, j) + ')'


if __name__ == "__main__":
    MatrixChainMultiplication()
