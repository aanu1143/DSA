def lcs(a, b, i, j):
    if i >= len(a) or j >= len(b):
        return 0
        
    if a[i] == b[j]:
        return(1+lcs(a, b, i+1, j+1))

    left = lcs(a, b, i, j+1)
    right = lcs(a, b, i+1, j)
    return max(left, right)


if __name__ == "__main__":
    A = input()
    B = input()
    print(lcs(A, B, 0, 0))

