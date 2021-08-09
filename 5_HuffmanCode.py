#!/usr/bin/env python3
import sys

if sys.version_info < (3, 9):
    sys.exit("Python %s.%s or later is required.\n", format(3, 9))


class Node:
    def __init__(self, c=None, p=0, l=None, r=None):
        self.char = c
        self.prob = p
        self.left = l
        self.right = r


class Heap:
    def __init__(self):
        self.A = []

    def __str__(self):
        return '[' + ", ".join([str(x.prob) for x in self.A]) + ']'

    def push(self, e):
        self.A.append(e)

    def pop(self):
        if len(self.A) == 0:
            return None
        idx = 0
        for i in range(1, len(self.A)):
            if self.A[i].prob < self.A[idx].prob:
                idx = i
        top = self.A[idx]
        del self.A[idx]
        return top


def Visit(node: Node, code=""):
    if node.char:
        return {node.char: code}
    return Visit(node.left, code + '0') | Visit(node.right, code + '1')


def HuffmanCode():
    N = int(input("How many char? "))
    print("Enter {} line: <char> <frequency in percent>".format(N))
    C = ['?' for _ in range(N)]
    P = [0 for _ in range(N)]
    for i in range(N):
        L = input("Data {}: ".format(i + 1)).strip().split(' ')
        C[i], P[i] = L[0], int(L[1])

    H = Heap()
    for i in range(N):
        H.push(Node(C[i], P[i]))
    for _ in range(N - 1):
        X = H.pop()
        Y = H.pop()
        H.push(Node(None, X.prob + Y.prob, X, Y))
    H = Visit(H.pop())

    print("\nChar    Code")
    Avg = 0
    for i in range(N):
        print("{:4}  {:>6}".format(C[i], H[C[i]]))
        Avg += P[i] * len(H[C[i]])
    print("Avg:  {:>6}\n".format(Avg / 100))

    # Encode
    S = "deadbeef"
    print("{} is encoded to {}".format(S, ''.join(H[c] for c in S)))

    # Decode
    S = "11111010111101110111011100"
    print(S, "is decoded to ", end='')
    R = {v: k for k, v in H.items()}
    T = ""
    for c in S:
        T += c
        if T in R:
            print(R[T], end='')
            T = ""
    print()


if __name__ == "__main__":
    HuffmanCode()
