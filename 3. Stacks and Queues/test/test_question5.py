from datastructures.stack import Stack
from src import question5

def test_sort_stack_already_ordered():
    stack = Stack()
    stack.push(9)
    stack.push(8)
    stack.push(7)
    stack.push(6)
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    actual = question5.sort_stack(stack)
    assert actual.pop().data == 1
    assert actual.pop().data == 2
    assert actual.pop().data == 3
    assert actual.pop().data == 4
    assert actual.pop().data == 5
    assert actual.pop().data == 6
    assert actual.pop().data == 7
    assert actual.pop().data == 8
    assert actual.pop().data == 9

def test_sort_stack_descending_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    actual = question5.sort_stack(stack)
    assert actual.pop().data == 1
    assert actual.pop().data == 2
    assert actual.pop().data == 3
    assert actual.pop().data == 4
    assert actual.pop().data == 5
    assert actual.pop().data == 6
    assert actual.pop().data == 7
    assert actual.pop().data == 8
    assert actual.pop().data == 9

def test_sort_stack_scrambled():
    stack = Stack()
    stack.push(4)
    stack.push(7)
    stack.push(9)
    stack.push(1)
    stack.push(6)
    stack.push(3)
    stack.push(8)
    stack.push(2)
    stack.push(5)
    actual = question5.sort_stack(stack)
    assert actual.pop().data == 1
    assert actual.pop().data == 2
    assert actual.pop().data == 3
    assert actual.pop().data == 4
    assert actual.pop().data == 5
    assert actual.pop().data == 6
    assert actual.pop().data == 7
    assert actual.pop().data == 8
    assert actual.pop().data == 9