#!/usr/bin/env python3


def LongestCommonSubsequence():
    X = ''.join(input("X: ").strip().split(' '))
    Y = ''.join(input("Y: ").strip().split(' '))

    N, M = len(X), len(Y)
    A = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    D = [['-' for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if X[i] == Y[j]:
                A[i + 1][j + 1] = A[i][j] + 1
                D[i + 1][j + 1] = '*'
            elif A[i][j + 1] >= A[i + 1][j]:
                A[i + 1][j + 1] = A[i][j + 1]
                D[i + 1][j + 1] = '^'
            else:
                A[i + 1][j + 1] = A[i + 1][j]
                D[i + 1][j + 1] = '<'

    print("Calculation:")
    print("X/Y", end='')
    for c in Y:
        print("{:>5}".format(c), end='')
    print()
    print()
    for i in range(1, N + 1):
        print(X[i - 1], "  ", end='')
        for j in range(M):
            print("{:>5}".format(str(A[i][j]) + D[i][j]), end='')
        print()
        print()

    LCS = ""
    x, y = N, M
    while x > 0 and y > 0:
        if D[x][y] == '*':
            LCS = X[x - 1] + LCS
            x -= 1
            y -= 1
        elif D[x][y] == '^':
            x -= 1
        else:
            y -= 1
    print("LCS:", LCS)


if __name__ == "__main__":
    LongestCommonSubsequence()
