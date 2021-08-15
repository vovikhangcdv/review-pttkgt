#!/usr/bin/env python3


def GraphColoring():
    print("Input each edge in form: <u> <v>, empty line to break")
    nEdge = 0
    AdjList = {}
    while True:
        nEdge += 1
        L = input("Edge {}: ".format(nEdge)).strip()
        if len(L) == 0:
            break
        u, v = L.upper().split(" ")
        if u in AdjList:
            AdjList[u].add(v)
        else:
            AdjList[u] = {v}
        if v in AdjList:
            AdjList[v].add(u)
        else:
            AdjList[v] = {u}
    N = len(AdjList)
    print("Read {} edge(s)\n".format(N))

    print("Vertex   Degree")
    for i in range(N):
        print("{:6}   {:>6}".format(chr(65 + i), len(AdjList[chr(65 + i)])))
    print()

    L = [[-len(AdjList[x]), x] for x in AdjList.keys()]
    L.sort()
    MarkedColor = [None for _ in range(N)]
    Color = 0
    while N:
        Color += 1
        T = []
        for d, u in L:
            i = ord(u) - 65
            if MarkedColor[i]:
                continue
            if any([t in AdjList[u] for t in T]):
                continue
            MarkedColor[i] = Color
            T += [u]
            N -= 1
        print("Color {}: {}".format(Color, T))


if __name__ == "__main__":
    GraphColoring()
