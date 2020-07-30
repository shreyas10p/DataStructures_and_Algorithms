class BinTreeNode(object):
    """docstring for BinTreeNode"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PreOrder(subTree):              #<root><left><right>
    if(subTree is None):
        return
    print(subTree.data)
    PreOrder(subTree.left)
    PreOrder(subTree.right)

def Inorder(subTree):             #<left><root><right>
    if(subTree is None):
        return
    Inorder(subTree.left)
    print(subTree.data)
    Inorder(subTree.right)

def PostOrder(subTree):           #<left><right><root>
    if(subTree is None):
        return
    Inorder(subTree.left)
    Inorder(subTree.right)
    print(subTree.data)


if __name__ == '__main__':
    binNode1 = BinTreeNode('A')

    binNode1.left = BinTreeNode('B')
    binNode1.right = BinTreeNode('Z')
    binNode1.left.left = BinTreeNode('C')
    binNode1.right.left = BinTreeNode('Y')
    PreOrder(binNode1)
    print("inorder")
    Inorder(binNode1)
    print("postOrder")
    PostOrder(binNode1)
