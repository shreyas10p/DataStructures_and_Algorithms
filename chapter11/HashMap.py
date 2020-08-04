import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from Chapter2.array import Array

class _MapEntry(object):
    """docstring for _MapEntry"""
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap(object):
    """docstring for HashMap"""
    UNUSED = None
    EMPTY = _MapEntry(None,None)
    def __init__(self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - (len(self._table)//3)

    def __len__(self):
        return len(self._table)

    def __contains__(self,key):
        slot = self._findSlot(key,False)
        return slot is not None

    def add(self,key,value):
        if key in self:
            slot = self._findSlot(key,False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key,True)
            self._table[slot] = _MapEntry(key,value)
            self._count += 1
            if(self._count == self._maxCount):
                self._rehash()
            return True

    def _rehash(self):
        originalTable = self._table
        newSize = len(self._table)*2 + 1
        self._table  = Array(newSize)
        self._count = 0
        self._maxCount = newSize - (newSize//3)
        for entry in originalTable:
            if entry is not self.UNUSED and entry is not self.EMPTY:

                slot = self._findSlot(entry.key,True)
                self._table[slot] = entry
                self._count +=1


    def _findSlot(self,key,forInsert):
        slot = self._hash1(key)
        step = self._hash2(key)
        M = len(self._table)
        print("key",key,slot)
        while(self._table[slot] is not self.UNUSED):
            if(forInsert and (self._table[slot] is self.UNUSED or self._table[slot] is self.EMPTY)):
                return slot
            elif( not forInsert and (self._table[slot] is not self.EMPTY and self._table[slot].key==key)):
                return slot
            else:
                slot = (slot+step) %M
        if(forInsert):
            return slot


    def _hash1(self,key):
        return abs(hash(key)) % len(self._table)

    def _hash2(self,key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)

    def __repr__(self):
        return str(self._table)

# TODO : Iterator



# if __name__ == '__main__':
#     map = HashMap()
#     map.add('a',1)
#     map.add('b',2)
#     map.add('c',3)
#     map.add('d',4)
#     map.add('e',5)
#     map.add('f',6)
#     map.add('g',7)
#     map.add('h',8)
#     map.add('i',9)
#     map.add('j',1)
#     map.add('k',2)
#     print("array")
#     for num in map._table:
#         if num is not None:
#             print(num.val)
#         else:
#             print(num)
