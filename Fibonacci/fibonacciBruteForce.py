def fib(n):
    #Base Case
    if n <= 1:
        return n
        
    return fib(n-1)+fib(n-2)


if __name__ == "__main__":
    n = int(input())

    print(fib(n))
