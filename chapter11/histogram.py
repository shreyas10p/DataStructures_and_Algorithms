from HashMap import HashMap

class Histogram(object):
    """docstring for Histogram"""
    def __init__(self, catSeq):
        self._hashMap = HashMap()
        for cat in catSeq:
            self._hashMap.add(cat,0)

    def getCount(self,cat):
        assert cat in self._hashMap,"Category Not Found"
        slot  = self._hashMap._findSlot(cat,False)
        return self._hashMap[slot].val

    def incCount(self,cat):
        assert cat in self._hashMap,"Category Not Found"
        slot = self._hashMap._findSlot(cat,False)
        self._hashMap[slot].val +=1

# TODO: Total Count and iterrator()
