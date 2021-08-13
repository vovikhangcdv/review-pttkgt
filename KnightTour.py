#!/usr/bin/env python3

HX = [-1, -2, -2, -1, 1, 2, 2, 1]
HY = [2, 1, -1, -2, -2, -1, 1, 2]


def KnightTour(UseBound=True):
    N = int(input("Size of board: "))
    x0, y0 = [int(x) for x in input("Starting position: ").strip().split(' ')]
    x0, y0 = x0 - 1, y0 - 1

    A = [[0 for _ in range(N)] for _ in range(N)]
    FOUNDED = False
    STEP = 0

    def Try(x, y, k=1):
        nonlocal FOUNDED
        nonlocal STEP
        if FOUNDED:
            return
        A[x][y] = k
        STEP += 1
        print("Step {}: [{}, {}] = {}".format(STEP, x + 1, y + 1, k))
        Show()
        print('-' * 60)
        if k == N * N:
            print("\nSolution:")
            Show()
            FOUNDED = True
            return

        L = []
        for i in range(8):
            nx, ny = x + HX[i], y + HY[i]
            if nx in range(N) and ny in range(N) and A[nx][ny] == 0:
                L.append([Candidate(nx, ny), nx, ny])

        if UseBound:
            L.sort()
        for c, nx, ny in L:
            Try(nx, ny, k + 1)
        if not FOUNDED:
            A[x][y] = 0

    def Candidate(x, y):
        res = 0
        for i in range(8):
            nx, ny = x + HX[i], y + HY[i]
            if nx in range(N) and ny in range(N) and A[nx][ny] == 0:
                res += 1
        return res

    def Show():
        for L in A:
            for x in L:
                print("{:>3}".format(x), end='')
            print()

    Try(x0, y0)

    if not FOUNDED:
        print("\nNO SOLUTION!!!")


if __name__ == "__main__":
    KnightTour(False)
