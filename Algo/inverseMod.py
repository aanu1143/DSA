def modInverse(p, q, x=998244353):
    ans = power(q, x-2, x)*p
    return ans%x
def power(x, y, m) :
    if (y == 0) : 
        return 1
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 

    if(y % 2 == 0) : 
        return p 
    else : 
        return ((x * p) % m)