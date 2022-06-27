from datastructures.stack import Stack

def sort_stack(stack: Stack):
    """
    Write a program to sort a stack such that the smallest items are on the top.
    You can use an additional temporary stack, but you may not copy the elements
    into any other data structure (such as an array). The stack supports the
    following operations: push, pop, peek, and isEmpty.
    """
    new_stack = Stack()
    temp_stack = Stack()
    while not stack.isEmpty():
        item = stack.pop()
        if new_stack.isEmpty() or item.data <= new_stack.peek():
            new_stack.push(item)
            continue
        else:
            while not new_stack.isEmpty() and item.data > new_stack.peek():
                temp_stack.push(new_stack.pop())
            new_stack.push(item)
            while not temp_stack.isEmpty():
                new_stack.push(temp_stack.pop())
    return new_stack
