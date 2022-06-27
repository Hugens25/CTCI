from src import question2


def test_stack_min():
    stack = question2.MinStack()
    stack.push('2')
    stack.push('1')
    stack.push('3')
    assert stack.min() == '1'