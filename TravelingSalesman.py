#!/usr/bin/env python3

from functools import reduce

PATH = ""


def TravelingSalesman():
    global PATH
    print(PATH)
    N = int(input("How many vertex? "))
    print("Input each edge with weight in form <u> <v> <w>. Input empty line to break.")
    M = 0
    A = []
    while True:
        M += 1
        L = input("Edge {}:".format(M)).strip().upper()
        if len(L) == 0:
            break
        L = L.split(' ')
        u, v, w = L[0], L[1], int(L[2])
        A.append([w, u, v])

    print("Read {} edge(s)!".format(M - 1))
    A.sort()
    Chosen = set(A[0][1])
    Chosen.add(A[0][2])
    MST = [A[0][1:]]
    while len(Chosen) < N:
        Min = 10 ** 10
        U, V = None, None
        for w, u, v in A:
            if ((u in Chosen) ^ (v in Chosen)) and (w < Min):
                Min = w
                U, V = u, v
        MST += [[U, V]]
        Chosen.add(U)
        Chosen.add(V)

    START = "A"

    print("Minimun spaning tree: {}.".format(", ".join([u + " -> " + v for u, v in MST])))
    MST = BuildMST(MST)
    for v in MST.keys():
        MST[v].sort()
    TreeWalk = DFS(MST, START)
    print("Tree walk: {}".format(" -> ".join(list(TreeWalk))))
    Hamiltonian = list(reduce(lambda x, y: x + y if y not in x else x, TreeWalk, "")) + [START]
    print("Hamiltonian cycle: {}".format(" -> ".join(list(Hamiltonian))))
    Cost = []
    for i in range(1, len(Hamiltonian)):
        U, V = Hamiltonian[i - 1], Hamiltonian[i]
        for w, u, v in A:
            if (u == U and v == V) or (u == V and v == U):
                Cost += [w]
                break
    print("Cost: {} = {}".format(" + ".join(str(x) for x in Cost), sum(Cost)))


def BuildMST(A):
    AdjList = {}
    for u, v in A:
        if u in AdjList:
            AdjList[u].append(v)
        else:
            AdjList[u] = [v]
        if v in AdjList:
            AdjList[v].append(u)
        else:
            AdjList[v] = [u]
    return AdjList


def DFS(Adj, u, p=None):
    global PATH
    PATH += u
    for v in Adj[u]:
        if v == p:
            continue
        DFS(Adj, v, u)
        PATH += u
    return PATH


if __name__ == "__main__":
    TravelingSalesman()
