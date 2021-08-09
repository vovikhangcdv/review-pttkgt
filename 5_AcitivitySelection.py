#!/usr/bin/env python3


def AcitivitySelection():
    N = int(input("How many task? "))
    A = []
    for i in range(1, N + 1):
        line = input("S[{}] F[{}] = ".format(i, i)).strip().split(' ')
        A.append([int(x) for x in line][::-1] + [i])

    A.sort()
    last = 0
    Choice = []

    for f, s, idx in A:
        if s >= last:
            Choice.append(idx)
            last = f

    for i in range(len(A)):
        A[i][0], A[i][2] = A[i][2], A[i][0]
    A.sort()
    print("\nTIMELINE\nTask:  ", end='')
    M = max([x[2] for x in A])
    for i in range(1, M + 1):
        print("{:>4}".format(i), end='')
    print()
    for idx, s, f in A:
        print("  {:2d}   ".format(idx), end='')
        c = ' ###' if idx in Choice else ' ---'
        print("    " * (s - 1) + c * (f - s + 1))

    print("\nMy choice:", Choice)


if __name__ == "__main__":
    AcitivitySelection()
