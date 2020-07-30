


# 2 3 3 2 3 3 3 2 3 3 3 2 3 3 2 3 3 3 2 3 3 3 2 3 3 3 2 3 3 2
#    2      3       3     2       3       3        3     2     3     3   2 3  3 3 2
#            2                        3                           2           3


def result(x,y,geneObj):
    print(x,end=' ')
    for num in range(next(geneObj)):
        print(y,end=' ')
    result(x,y,geneObj)


def infinitepattern(x,y):
    while True:
        yield x
        for i in range(x):
            yield y
        yield x
        for i in range(y):
            yield y


NumberA = 2
NumberB = 3
generatorObj = infinitepattern(NumberA,NumberB)
result(NumberA,NumberB,generatorObj)
