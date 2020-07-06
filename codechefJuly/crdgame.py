def checkWinner(chef,morty):
    chefSum = checkDigitSum(chef)
    mortySum = checkDigitSum(morty)
    if(chefSum>mortySum):
        return 1,0
    elif(chefSum<mortySum):
        return 0,1
    else:
        return 1,1

def checkDigitSum(x):
    digitSum = x%10
    x = int(x/10)
    while(x > 9):
        digitSum += x%10
        x = int(x/10)
    digitSum += x
    return digitSum

if __name__ == '__main__':
    CHEF_WIN = 0
    MORTY_WIN = 1
    DRAW = 2
    testCase = input()
    for i in range(int(testCase)):
        countChef = 0
        countMorty = 0
        rounds = int(input())
        for j in range(rounds):
            a,b = map(int,input().split())
            x,y = checkWinner(a,b)
            countChef += x
            countMorty += y
        if(countChef >countMorty):
            print(CHEF_WIN,end=" ")
            print(countChef)
        elif(countChef<countMorty):
            print(MORTY_WIN,end=" ")
            print(countMorty)
        else:
            print(DRAW,end=" ")
            print(countMorty)

