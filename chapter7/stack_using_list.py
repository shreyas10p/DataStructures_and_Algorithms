class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = list()

    def length(self):
        return len(self.stack)

    def isEmpty(self):
        if(self.length()==0):
            return False

        return True

    def pop(self):
        assert self.length() >0,"Stack Should be non-empty"
        item = self.stack.pop()
        return item

    def peek():
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self.stack[-1]

    def push(self,item):
        self.stack.append(item)

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

# Disadvantages
# push() and pop() operation requires reallocation of array memory and therefore it consumes O(n) time for push and pop operations.



