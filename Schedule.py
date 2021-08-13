#!/usr/bin/env python3


def Schedule():
    N = int(input("Number of processor: "))
    M = int(input("Number of task: "))
    T = [None for _ in range(M)]
    for i in range(M):
        T[i] = [int(input("T[{}] = ".format(i + 1))), i + 1]
    T.sort(reverse=True)
    P = [0 for _ in range(N)]
    S = [[] for _ in range(N)]
    for t, i in T:
        m = min(P)
        for k in range(N):
            if P[k] == m:
                P[k] += t
                S[k].append(i)
                break

    print("\nResult:")
    for i in range(N):
        print("P[{}] = {}, task = {}".format(i + 1, P[i], S[i]))


if __name__ == "__main__":
    Schedule()
