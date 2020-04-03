def editDist(a, b, i, j):
    if i == len(a):
        return len(b)-j
    if j == len(b):
        return len(a)-i
    if a[i] == b[j]:
        return editDist(a, b, i+1, j+1)

    left = 1+editDist(a, b, i, j+1)
    mid = 1+editDist(a, b, i+1, j)
    right = 1+editDist(a, b, i+1, j+1)
    return min(left, min(mid, right))


if __name__ == "__main__":
    A = input()
    B = input()
    print(editDist(A, B, 0, 0))
