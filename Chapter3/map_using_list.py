class Map(object):
    """docstring for Map"""
    def __init__(self, arg):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self,key):
        return _findPosition(key)

    def add(self,key,value):
        idx = self._findPosition(key)
        if idx is not None:
            self._theElements[idx].value = value
            return False
        else:
            self._theElements.append(_Mapentry(key,value))
            return True

    def _findPosition(self,key):
        for i in range(len(self._theElements)):
            if self._theElements[i].key == key:
                return i

        return None

    def valueOf(self,key):
        idx = self._findPosition(key)
        assert idx is not None , "Key does not exists"
        return self._theElements[idx].value


class _Mapentry(object):
    """docstring for _Mapentry"""
    def __init__(self, key,value):
        super(_Mapentry, self).__init__()
        self.key = key
        self.value = value


