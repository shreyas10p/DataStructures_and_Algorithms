# add , substract, multiply operations pending.

class Polynomial(object):
    """docstring for Polynomial"""
    def __init__(self,degree=None,coeffient=None):
        super(Polynomial, self).__init__()
        if degree is None:
            self._head = None
        else:
            self._head = _PolyNode(degree,coeffient)
        self._tail = self._head

    def __repr__(self):
        initStr = ""
        for val in self:
            initStr += str(val._coef)+"|"+str(val._degree)+" -> "
        return initStr

    def _appendTerm(self,degree,coeffient):
        if(coeffient != 0):
            newNode = _PolyNode(degree,coeffient)
            if(self._tail == None):
                self._head = newNode
            else:
                preNode = None
                curNode = self._head
                while(curNode is not None and curNode._degree > degree):
                    preNode = curNode
                    curNode = curNode._next
                newNode._next = curNode
                if curNode is self._head:
                    self._head = newNode
                else:
                    preNode._next = newNode
            self._tail = newNode


    def degree(self):
        if self._head is not None:
            return self._head._degree
        else:
            return -1

    def __getitem__(self,item):
        assert self.degree() >= 0,"Operation not permitted"
        curNode = self._head
        while(curNode is not None):
            if(curNode._degree == item):
                return curNode._coef
            curNode = curNode._next
        return 0

    def evaluate(self,scalar):
        assert self.degree() >= 0,"Operation not permitted"
        result = 0
        curNode = self._head
        while(curNode is not None):
            result += (scalar**curNode._degree)*curNode._coef
            curNode = curNode._next
        return result


    def __iter__(self):
        return _BagIterator(self._head)

    def __add__(self,addPoly):
        resPoly = Polynomial()
        curNodeA = self._head
        curNodeB = addPoly._head
        while (curNodeA is not None and curNodeB is not None):
            if(curNodeA._degree > curNodeB._degree):
                resPoly._appendTerm(curNodeA._degree,curNodeA._coef)
                curNodeA = curNodeA._next
            elif(curNodeB._degree > curNodeA._degree):
                resPoly._appendTerm(curNodeB._degree,curNodeB._coef)
                curNodeB = curNodeB._next
            elif(curNodeB._degree == curNodeA._degree):
                newNode = _PolyNode(curNodeB._degree,curNodeA._coef+curNodeB._coef)
                resPoly._appendTerm(newNode._degree,newNode._coef)
                curNodeA = curNodeA._next
                curNodeB = curNodeB._next
        while(curNodeA is not None):
            resPoly._appendTerm(curNodeA._degree,curNodeA._coef)
            curNodeA = curNodeA._next
        while(curNodeB is not None):
            resPoly._appendTerm(curNodeB._degree,curNodeB._coef)
            curNodeB = curNodeB._next
        return resPoly

    def __sub__(self,addPoly):
        resPoly = Polynomial()
        curNodeA = self._head
        curNodeB = addPoly._head
        while (curNodeA is not None and curNodeB is not None):
            if(curNodeA._degree > curNodeB._degree):
                resPoly._appendTerm(curNodeA._degree,curNodeA._coef)
                curNodeA = curNodeA._next
            elif(curNodeB._degree > curNodeA._degree):
                resPoly._appendTerm(curNodeB._degree,curNodeB._coef)
                curNodeB = curNodeB._next
            elif(curNodeB._degree == curNodeA._degree):
                newNode = _PolyNode(curNodeB._degree,curNodeA._coef-curNodeB._coef)
                resPoly._appendTerm(newNode._degree,newNode._coef)
                curNodeA = curNodeA._next
                curNodeB = curNodeB._next
        while(curNodeA is not None):
            resPoly._appendTerm(curNodeA._degree,curNodeA._coef)
            curNodeA = curNodeA._next
        while(curNodeB is not None):
            resPoly._appendTerm(curNodeB._degree,curNodeB._coef)
            curNodeB = curNodeB._next
        return resPoly

# FFT implementation for efficient multiplication alogorithm. (Karatsuba and FFT)
    def __mul__(self,mulPoly):
        resPoly = Polynomial()
        curNodeA = self._head
        curNodeB = mulPoly._head


# An iterator for the Bag ADT implemented as a Python list.
class _BagIterator :
    def __init__( self, theList ):
        self._bagItems = theList

    def __iter__( self ):
        return self

    def next( self ):
        if(self._bagItems is not None):
            item = self._bagItems
            self._bagItems = self._bagItems._next
            return item
        else:
            raise StopIteration


class _PolyNode(object):
    """docstring for _PolyNode"""
    def __init__(self,degree,coef):
        super(_PolyNode, self).__init__()
        self._degree = degree
        self._coef = coef
        self._next = None

    def __repr__(self):
        return ""+str(self._degree)

if __name__ == '__main__':
    poly = Polynomial()
    poly._appendTerm(4,3)
    poly._appendTerm(5,6)
    poly._appendTerm(8,2)
    poly._appendTerm(3,7)
    val = poly.evaluate(2)
    polyB = Polynomial()
    polyB._appendTerm(1,2)
    polyB._appendTerm(6,3)
    polyB._appendTerm(3,9)
    polyB._appendTerm(5,6)
    print("add",poly+polyB)
    print(poly)
    print(val)
