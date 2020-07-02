def printRev(n):
    if n>0:
        print(n)
        printRev(n-1)

def printInc(n):
    if n>0:
        printInc(n-1)
        print(n)

def fact(n):
    assert n>0,"Number must be greater than 0"
    if(n<2):
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
    ans = fact(10)
    print(ans)
    # printRev(10)
    printInc(10)
