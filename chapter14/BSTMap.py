class BSTMap(object):
    """docstring for BSTMap"""
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BSTMapIterator(self._root)

    def __contains__(self,targetKey):
        return _bstSearch(self._root,targetKey) is not None

    def __repr__(self):
        data = ""
        return data

    def valueOf(self,targetKey):
        value = self._bstSearch(self._root,targetKey)
        assert value is not None,"Key value Error"
        return value._val

    def _bstSearch(self,bstTree,targetKey):
        if(bstTree is None):
            return None
        if(targetKey<bstTree._key):
            return self._bstSearch(bstTree._left,targetKey)
        elif(targetKey>bstTree._key):
            return self._bstSearch(bstTree._right,targetKey)
        elif(targetKey == bstTree._key):
            return bstTree

    def _bstMinimum(self,bstTree):
        if(bstTree._left is None):
            return bstTree._val
        return self._bstMinimum(bstTree._left)

    def _bstMaximum(self,bstTree):
        if(bstTree._right is None):
            return bstTree._val
        return self._bstMaximum(bstTree._right)

    def add(self,key,value):
        node = self._bstSearch(self._root,key)
        if(node is not None):
            node._val = value
            return False
        else:
            self._root = self._bstInsert(self._root,key,value)
            self._size += 1
            return True

    def _bstInsert(self,subTree,key,val):
        if(subTree is None):
            subTree = _BSTMapNode(key,val)
        if(key<subTree._key):
            subTree._left = self._bstInsert(subTree._left,key,val)
        elif(key>subTree._key):
            subTree._right = self._bstInsert(subTree._right,key,val)
        return subTree

    def remove(self,key):
        assert key in self,"Key not found"
        self._root = self._bstDelete(self._root,key)
        self._size -= 1

    def _bstDelete(self,subTree,key):
        if(subTree is None):
            return subTree
        elif(key<subTree._left):
            subTree._left = self._bstDelete(subTree._left,key)
            return subTree
        elif(key>subTree._right):
            subTree._right = self._bstDelete(subTree,_right,key)
            return subTree
        else:
            if(subTree._left is None and subTree._right is None):
                return None
            elif(subTree._left is None or subTree._right is None):
                if(subTree._left is not None):
                    return subTree._left
                else:
                    return subTree._right
            else:
                minEle = self._bstMinimum(subTree._right)
                subTree._key = minEle._key
                subTree._val = minEle._val
                subTree._right = self._bstDelete(subTree._right,minEle._key)
                return subTree


class _BSTMapNode(object):
    """docstring for _BSTMapNode"""
    def __init__(self, key,val):
        self._key = key
        self._val = val
        self._left = None
        self._right = None

if __name__ == '__main__':
    arr = [60, 25, 100, 35, 17, 80]
    bstMap = BSTMap()
    for i in range(len(arr)):
        bstMap.add(arr[i],i)
    print(bstMap.valueOf(25))
