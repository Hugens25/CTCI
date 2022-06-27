from datastructures.stack import Stack

def test_stack():
    stack = Stack()
    items = [1, 2, 3, 4, 5]
    for item in items:
        stack.push(item)
    assert stack.peek() == 5
    assert stack.isEmpty() == False
    assert stack.size() == 5
    assert stack.pop().data == 5
    assert stack.pop().data == 4
    assert stack.pop().data == 3
    assert stack.pop().data == 2
    assert stack.pop().data == 1
    assert stack.isEmpty() == True
    assert stack.peek() is None
    assert stack.size() == 0