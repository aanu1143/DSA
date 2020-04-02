def lcs(a, b, i, j, l):
    if i >= len(a) or j >= len(b):
        return 0

    if l[i][j] != -1:
        return l[i][j]

    if a[i] == b[j]:
        return(1+lcs(a, b, i+1, j+1, l))

    left = lcs(a, b, i, j+1, l)
    right = lcs(a, b, i+1, j, l)
    l[i][j] = max(left, right)
    return l[i][j]


if __name__ == "__main__":
    A = input()
    B = input()
    L = [[-1 for i in range(len(A))] for i in range(len(B))]
    print(lcs(A, B, 0, 0, L))
