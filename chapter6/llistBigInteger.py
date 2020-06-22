from linkedList import linkedList

class BigInteger(object):
    """docstring for BigInteger"""
    def __init__(self, initValue="0"):
        super (BigInteger, self).__init__()
        self.initValue = initValue
        self._head = linkedList(int(initValue[-1]),None)
        curNode = self._head
        for i in range(len(initValue)-1,0,-1):
            curNode._next = linkedList(int(initValue[i]),None)
            curNode = curNode._next

    def __len__(self):
        return len(initValue)-1

    # Comparison operator
    def __eq__(self,other):
        return self.__checkEquality(other)

    def __ne__(self,other):
        return not self.__checkEquality(other)

    def __lt__(self,other):
        return __checklessThan(self,other)

    def __gt__(self,other):
        return not __checklessThan(self,other)

    def __le__(self,other):
        return self.__checklessThan(self,other)

    def __ge__(self,other):
        return not self.__checklessThan(self,other)

    #Arithmatic Operators
    def __add__(self,other):
        curNodeA = self._head
        curNodeB = other._head
        maxLen = max(len(self),len(other))
        addLlist = BigInteger("0"*maxLen)
        carry = 0
        addVal = 0
        while(curNodeA is not None and curNodeB is not None):
            addVal = curNodeA._data+curNodeB._data+carry
            addLlist._data = addVal%10
            carry = int(addVal/10)
            addLlist = addLlist._next
            curNodeA = curNodeA._next
            curNodeB = curNodeB._next
        while(curNodeA is not None):
            addLlist._data = curNodeA._data
        while(curNodeB is not None):
            addLlist._data = curNodeB._data

        return addLlist

    def __sub__(self,other):
        if(self._head>other._head):
            curNodeA = self._head
            curNodeB = other._head
        else:
            curNodeA = other._head
            curNodeB = self._head
        maxLen = max(len(self),len(other))
        subLlist = BigInteger("0"*maxLen)
        carry = 0
        subVal = 0
        while(curNodeA is not None and curNodeB is not None):
            subVal = curNodeA._data-curNodeB._data-carry
            if(subVal<0):
                carry = 1
                subVal = 10-subVal
            else:
                carry = 0
            subLlist._data = subVal
            subLlist = subLlist._next
            curNodeA = curNodeA._next
            curNodeB = curNodeB._next
        while(curNodeA is not None):
            subLlist._data = curNodeA._data

        return subLlist
#TODO: Continue Question 6.7 and Test

    def __checkEquality(self,other):
        curNodeA = self._head
        curNodeB = other._head
        if(len(curNodeA) == len(curNodeB)):
            while(curNodeA is not None):
                if(curNodeA._data != curNodeB._data):
                    return False
                curNodeA = curNodeA._next
                curNodeB = curNodeB._next
        else:
            return False
        reutrn  True

    def __checklessThan(self,other):
        curNodeA = self._head
        curNodeB = other._head
        lessThan = True
        if(len(curNodeA)<len(curNodeB)):
            return True
        elif(len(curNodeB)<len(curNodeA)):
            return False
        elif(len(curNodeA) == len(curNodeB)):
            while(curNodeA is not None and curNodeB is not None):
                if(curNodeA._data < curNodeB._data):
                    digitsVal = True
                elif(curNodeA._data > curNodeB._data):
                    digitsVal = False
                curNodeA = curNodeA._next
                curNodeB = curNodeB._next

        return digitsVal

    def toString(self):
        return self.initValue


