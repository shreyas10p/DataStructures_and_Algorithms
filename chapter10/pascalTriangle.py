#Without Recursion
def pascalTriangle(n):
    for i in range(n):
        for j in range(n-i-1,0,-1):
            print("_",end="")
        for x in range(i+1):
            print(int(getNumber(i)/(getNumber(x)*getNumber(i-x))),end=" ")
        for j in range(n-i-1,0,-1):
            print("_",end="")
        print()

def getNumber(num):
    f = 1
    l = 1
    while(l<=num):
        f = f*l
        l += 1
    return f

#TODO with recursion

if __name__ == '__main__':
    pascalTriangle(6)
