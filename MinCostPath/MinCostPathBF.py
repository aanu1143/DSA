import sys


def mincostpath(a, i, j):
    n = len(a)
    m = len(a[0])
    if i == (n-1) and j == (m-1):
        return a[i][j]
    if i >= n or j >= m:
        return sys.maxsize
    right = a[i][j] + mincostpath(a, i, j+1)
    left = a[i][j]+mincostpath(a, i+1, j)
    return min(left, right)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(mincostpath(arr, 0, 0))
