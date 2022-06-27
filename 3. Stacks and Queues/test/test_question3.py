from src import question3

def test_set_of_plates():
    stack = question3.SetOfStacks(capacity=3)
    for i in range(1, 10):
        stack.push(i)
    assert stack.size() == 3
    assert stack.pop().data == 9
    assert stack.pop().data == 8
    assert stack.pop().data == 7
    assert stack.pop().data == 6
    assert stack.pop().data == 5
    assert stack.pop().data == 4
    assert stack.pop().data == 3
    assert stack.pop().data == 2
    assert stack.pop().data == 1
    assert stack.pop() == None

    stack2 = question3.SetOfStacks(capacity=3)
    for i in range(1, 10):
        stack2.push(i)
    assert stack2.pop_at(0).data == 9
    assert stack2.pop_at(1).data == 6
    assert stack2.pop_at(2).data == 3