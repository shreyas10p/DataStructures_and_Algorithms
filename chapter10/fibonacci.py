def fib(n):
    if(n>0):
        if(n==1 or n==2):
            return 1
        else:
            return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    n = fib(10)
    print(n)
