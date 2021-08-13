#!/usr/bin/env python3
import sys

if sys.version_info < (3, 9):
    sys.exit("Python {}.{} or later is required.\n".format(3, 9))


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
        return '[' + ", ".join([x.char + ':' + str(x.prob) for x in self.A]) + ']'

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
    if not (node.left or node.right):
        return {node.char: code}
    return Visit(node.left, code + '0') | Visit(node.right, code + '1')


def HuffmanCodeSolve():
    N = int(input("How many char? "))
    print("Enter {} line: <char> <frequency>".format(N))
    C = ['?' for _ in range(N)]
    P = [0 for _ in range(N)]
    for i in range(N):
        L = input("Data {}: ".format(i + 1)).strip().split(' ')
        C[i], P[i] = L[0], int(L[1])
    T = sum(P)
    for i in range(N):
        P[i] = P[i] / T * 100

    H = Heap()
    for i in range(N):
        H.push(Node(C[i], P[i]))
    print("\nInitial tree:", H)
    for _ in range(N - 1):
        X = H.pop()
        Y = H.pop()
        H.push(Node('(' + X.char + ", " + Y.char + ')', X.prob + Y.prob, X, Y))
        print("After step {}:".format(_ + 1), H)
    H = Visit(H.pop())

    print("\nChar    Freq    Code")
    Avg = 0
    for i in range(N):
        print("{:4}   {:>5.1f}    {:>4}".format(C[i], P[i], H[C[i]]))
        Avg += P[i] * len(H[C[i]])
    print("Avg:  {:>6}\n".format(Avg / 100))
    return H


def Encode(H):
    S = input("What defuq your want to encode? ")
    print("{} is encoded to {}".format(S, ''.join(H[c] for c in S)))


def Decode(H):
    R = {v: k for k, v in H.items()}
    S = input("What defuq your want to decode? ")
    print(S, "is decoded to ", end='')
    T = ""
    for c in S:
        T += c
        if T in R:
            print(R[T], end='')
            T = ""
    print()


def HuffmanCode():
    H = HuffmanCodeSolve()
    Choice = int(input("1: Encode, 2: Decode. Your choice? "))
    if Choice == 1:
        Encode(H)
    elif Choice == 2:
        Decode(H)
    else:
        print("Are you kidding me?")


if __name__ == "__main__":
    HuffmanCode
