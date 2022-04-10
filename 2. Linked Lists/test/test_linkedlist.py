from datastructures.linkedlist import LinkedList

def test_linkedlist():
    items = [2, 3, 4, 5]
    l = LinkedList(1)
    for item in items:
        l.append(item)
    
    assert l.get(1).prev is None
    assert l.get(1).next.data == 2
    assert l.get(5).next == None
    assert l.head == l.get(1)
    assert l.tail == l.get(5)
    assert l.size == 5
    l.prepend(0)
    assert l.head.data == 0
    assert l.head.next.data == 1
    assert l.size == 6
    l.remove(l.get(5))
    assert l.size == 5
    assert l.tail.data == 4