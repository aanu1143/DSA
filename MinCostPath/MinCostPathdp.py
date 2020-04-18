import sys


def mincostpath(a, i, j, dp):
    n = len(a)
    m = len(a[0])
    if i == (n-1) and j == (m-1):
        return a[i][j]
    if i >= n or j >= m:
        return sys.maxsize
    if dp[i][j] != -1:
        return dp[i][j]
    right = a[i][j] + mincostpath(a, i, j+1, dp)
    left = a[i][j]+mincostpath(a, i+1, j, dp)
    dp[i][j] = min(left, right)
    return dp[i][j]


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    dp = [[-1 for i in range(m)] for i in range(n)]
    print(mincostpath(arr, 0, 0, dp))
