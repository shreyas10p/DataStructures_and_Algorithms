from .Chapter2.array import Array

def fib(n):
    if(n>0):
        if(n==1 or n==2):
            return 1
        else:
            return fib(n-1)+fib(n-2)

#Fibonacci with memoization
def fibMemoization(n):
    cacheList = Array(100)
    if(n>0):
        if(n==1 or n==2):
            return 1
        else:
            if(cacheList[n] is not None):
                return cacheList[n]
            cacheList[n] = fib(n-1)+fib(n-2)
    return cacheList[n]

if __name__ == '__main__':
    n = fib(10)
    nMem = fibMemoization(10)
    print(n)
    print(nMem)
