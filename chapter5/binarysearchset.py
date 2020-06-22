class Set:
    def __init__(self):
        self._theList = list()

    def __len__(self):
        return len(self._theList)

    def __contains__(self,element):
        idx = self._findPosition(element)
        return idx < len(self) and self._theList[idx] == element

    def add(self,element):
        if element not in self._theList:
            idx = self._findPosition(element)
            self.insert(element,idx)

    def insert(self,element,idx):
        self._theList.insert(idx,element)

        # if(len(self._theList) == idx):
        #     print("idx",idx)
        #     print("in",element)
        #     self._theList.append(element)
        # else:
        #     print("list",self._theList)
        #     print("len",len(self._theList))
        #     print("if",idx)
        #     for i in range(len(self._theList)-1,idx,-1):
        #         print("i",i)
        #         self._theList[i+1] = self._theList[i] list out of range error
        #     self._theList[idx] = element


    def isSubsetOf(self,setB):
        for i in range(len(setB)):
            if setB._theList[i] != self._theList[i]:
                return False
        return True

    def union(self,setB):
        a=0
        b=0
        newSet = Set()
        while a<len(self._theList) and b<len(setB):
            if(setB._theList[b]>self._theList[a]):
                newSet._theList.append(self._theList[a])
                a+=1
            elif(setB._theList[b]<self._theList[a]):
                newSet._theList.append(setB._theList[b])
                b+=1
            else:
                newSet._theList.append(setB._theList[b])
                a+=1
                b+=1

        while(len(self._theList)>a):
            newSet._theList.append(self._theList[a])
            a+=1

        while(len(setB._theList)>b):
            newSet._theList.append(setB._theList[b])
            b+=1

        return newSet


    def remove(self,element):
        assert element in self._theList,"element must be in the list"
        idx = self._findPosition(element)
        self._theList.pop(idx)


    def _findPosition(self,element):
        low = 0
        high = len(self._theList)-1
        while(low<=high):
            mid = (low+high)/2
            if(self._theList[mid] == element):
                return mid
            if(self._theList[mid]<element):
                low = mid+1
            elif(self._theList[mid]>element):
                high = mid -1
        return low

if __name__ == '__main__':
    numberset = Set()
    numberset.add(6)
    numberset.add(8)
    numberset.add(10)
    numberset.add(1)
    numberset.add(18)
    numberset.add(20)
    numberset.add(15)
    numberset.add(20)
    numberset._theList.append(90)
    numbersetB = Set()
    numbersetB.add(9)
    numbersetB.add(24)
    numbersetB.add(36)
    numbersetB.add(25)
    numbersetB.add(44)
    numbersetB.add(2)
    numbersetB.add(16)
    numbersetB.add(4)
    print(numberset._theList)
    print(numbersetB._theList)
    union_set = numberset.union(numbersetB)
    print(union_set._theList)
