#!/usr/bin/env python3


def JobAssignment():
    N = int(input("How many job? "))
    A = []
    for _ in range(N):
        L = input("Person {} cost for each job: ".format(_ + 1)).strip().split(' ')
        A.append([int(x) for x in L])
    print(A)

    BEST = 10 ** 10
    SOLUTION = []

    def Try(p=0, S=[], Cost=0):
        nonlocal BEST
        nonlocal SOLUTION
        if p == N:
            if Cost < BEST:
                print("New BEST: {}".format(Cost))
                BEST = Cost
                SOLUTION = S
            print('-' * 60)
            return
        if Cost > BEST:
            print("Current cost exceeded BEST! BREAK")
            print('-' * 60)
            return

        for j in range(N):
            if j in S:
                continue
            print("Assign job {} for person {}. Current cost: {}, choice =".format(j + 1, p + 1, Cost + A[p][j]), [x + 1 for x in S] + [j + 1])
            Try(p + 1, S + [j], Cost + A[p][j])

    Try()
    print("Solution:", [x + 1 for x in SOLUTION])
    print("Minimum cost:", BEST)


if __name__ == "__main__":
    JobAssignment()
