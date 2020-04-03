def editDist(a, b, i, j, l):
    if i == len(a):
        return len(b)-j
    if j == len(b):
        return len(a)-i
    if a[i] == b[j]:
        x = editDist(a, b, i+1, j+1, l)
        l[i][j] = x
        return x

    left = 1+editDist(a, b, i, j+1, l)
    mid = 1+editDist(a, b, i+1, j, l)
    right = 1+editDist(a, b, i+1, j+1, l)
    return min(left, min(mid, right))


if __name__ == "__main__":
    A = input()
    B = input()
    L = [[-1 for i in range(len(B))] for i in range(len(A))]
    print(editDist(A, B, 0, 0, L))
