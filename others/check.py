def checkRange(filename):
    rangeMap = {'20-30':0,'30-40':0,'40-50':0,'50-60':0,'60-70':0,'70-80':0,'80-90':0,'90-100':0}
    with open(filename) as file:
        for marks in file:
            if(20<int(marks)<=30):
                rangeMap['20-30']+=1
            elif(30<int(marks)<=40):
                rangeMap['30-40']+=1
            elif(40<int(marks)<=50):
                rangeMap['40-50']+=1
            elif(50<int(marks)<=60):
                rangeMap['50-60']+=1
            elif(60<int(marks)<=70):
                rangeMap['60-70']+=1
            elif(70<int(marks)<=80):
                rangeMap['70-80']+=1
            elif(80<int(marks)<=90):
                rangeMap['80-90']+=1
            elif(90<int(marks)<=100):
                rangeMap['90-100']+=1
    print(rangeMap)


if __name__ == '__main__':
    checkRange('marks.txt')
