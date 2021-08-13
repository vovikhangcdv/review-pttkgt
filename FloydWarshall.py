#!/usr/bin/env python3

oo = 10 ** 10


def PrintMatrix(A):
    N = len(A) - 1
    print(' ', end='')
    for i in range(N):
        print("{:>4}".format(chr(97 + i)), end='')
    print()

    for i in range(1, N + 1):
        print(chr(96 + i), end='')
        for x in A[i][1:]:
            print("{:>4}".format(x if isinstance(x, int) and x < oo else '*'), end='')
        print()


def ShortestPath(B, start, end):
    m = B[start][end]
    if start == end:
        return [start]
    elif m == 0:
        return [start, end]
    return ShortestPath(B, start, m) + ShortestPath(B, m, end)


def Warshall():
    N = int(input("N = "))
    print("Input adjacency matrix:")
    A = [[0 for _ in range(N + 1)]]
    for _ in range(N):
        line = input().strip().replace("  ", " ").split(" ")
        L = [int(x) for x in line]
        assert all([x == 0 or x == 1 for x in L])
        A.append([0] + L)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if A[i][k] and A[k][j]:
                    A[i][j] = 1
        print("Step {}:".format(k))
        PrintMatrix(A)


def Floyd():
    N = int(input("N = "))
    print("Input adjacency matrix:")
    A = [[0 for _ in range(N + 1)]]
    B = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(N):
        line = input().strip().replace("  ", " ").split(" ")
        L = [int(x) if '0' <= x <= '9' else oo for x in line]
        A.append([0] + L)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if A[i][k] and A[k][j]:
                    t = A[i][k] + A[k][j]
                    if t < A[i][j]:
                        A[i][j] = t
                        B[i][j] = k
        print("Step {}:".format(k))
        print("- A" + str(k) + ":")
        PrintMatrix(A)
        print('- B' + str(k) + ":")
        PrintMatrix(B)
        print('-' * 10)

    print([chr(x + 96) for x in ShortestPath(B, 3, 1)])


if __name__ == "__main__":
    # Warshall()
    Floyd()
