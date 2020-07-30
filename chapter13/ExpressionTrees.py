class ExpressionTrees(object):
    """docstring for ExpressionTrees"""
    def __init__(self, ExpStr):
        self._expStr = expStr
        self._buildTree(expStr)

    def evaluate(self,variables):
        self._evalTree(self._expStr,variables)

    def __str__(self):
        return self._buildStr(self._expStr)



class ExpNode(object):
    """docstring for ExpNode"""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

