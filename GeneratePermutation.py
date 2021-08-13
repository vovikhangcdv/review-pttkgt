import itertools


def GeneratePermutation():
    A = input("Input elements list: ").strip().split(" ")
    permutations_list = [''.join(x) for x in list(itertools.permutations(A))]
    print("Permutations list: ")
    print(permutations_list)


if __name__ == "__main__":
    GeneratePermutation()
