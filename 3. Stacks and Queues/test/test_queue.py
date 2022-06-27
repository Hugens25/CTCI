from datastructures.queue import Queue

def test_queue():
    queue = Queue()
    items = [1, 2, 3, 4, 5]
    for item in items:
        queue.add(item)
    assert queue.peek() == 1
    assert queue.isEmpty() == False
    assert queue.size() == 5
    assert queue.remove().data == 1
    assert queue.remove().data == 2
    assert queue.remove().data == 3
    assert queue.remove().data == 4
    assert queue.remove().data == 5
    assert queue.isEmpty() == True
    assert queue.peek() is None
    assert queue.size() == 0