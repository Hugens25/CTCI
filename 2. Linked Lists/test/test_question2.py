from src import question2
from datastructures.linkedlist import LinkedList

def test_kth_to_last():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    actual = question2.kth_to_last(ll, 2)
    assert actual.data == 4