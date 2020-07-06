from random import randint
def reversellist(llist):
    if(llist._next is not None):
        reversellist(llist._next)
        print("rev",llist._data)

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname(path.dirname(path.abspath(__file__)))+'/chapter6' )
        from linkedList import linkedList
    else:
        from ..chapter6.linkedList import linkedList

    head = cursor = linkedList(randint(0,10),None)
    for i in range(10):
        cursor._next = linkedList(randint(0,10),None)
        cursor = cursor._next

    reversellist(head)
