def fib(n, a):
    #Base Case
    if n <= 1:
        return n
    if len(a) > n:
        return a[n]
        
    a.append(fib(n-1, a)+fib(n-2, a))
    return a[-1]


if __name__ == "__main__":
    n = int(input())
    a = [0, 1]
    print(fib(n, a))