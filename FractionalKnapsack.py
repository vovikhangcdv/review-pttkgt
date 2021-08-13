#!/usr/bin/env python3


def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def FractionalKnapsack():
    M = int(input("How big is your bag? "))
    N = int(input("How many item? "))
    A = []
    for i in range(N):
        L = input("S[{}] V[{}] = ".format(i, i)).strip().split(" ")
        L = [int(x) for x in L]
        A.append([L[1] / L[0]] + L + [i])

    A.sort(reverse=True)
    Total = 0
    X = [0 for _ in range(N)]
    for r, s, v, i in A:
        if s <= M:
            Total += v
            X[i] = 1
            M -= s
        else:
            Total += v * X[i]
            d = gcd(M, s)
            X[i] = "{}/{}".format(int(M / d), int(s / d))
            break

    print("\nMax value =", Total)
    print("Best choice:", X)


if __name__ == "__main__":
    FractionalKnapsack()
