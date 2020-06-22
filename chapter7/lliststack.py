class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        super(Stack, self).__init__()
        self._head = None
        self._size = 0

    def length(self):
        return self._size

    def isEmpty(self):
        if(self._head is None and self._size == 0):
            return True
        return False

    def push(self,item):
        newNode = ListNode(item)
        if(self._head is not None):
            newNode.next = self._head
        self._head = newNode
        self._size += 1

    def pop(self):
        assert self._head is not None,"Stack is empty"
        element = self._head.data
        self._head = self._head.next
        self._size -= 1
        return element

    def peek(self):
        assert self._head is not None,"Stack is empty"
        return self._head.data

class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, data):
        super(ListNode, self).__init__()
        self.data = data
        self.next = None

if __name__ == '__main__':
    stack_obj = Stack()
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.push(7)
    stack_obj.push(10)
    stack_obj.push(19)
    stack_obj.push(18)
    reverse_list = []
    for x in range(stack_obj.length()):
        reverse_list.append(stack_obj.pop())

    print(reverse_list)
