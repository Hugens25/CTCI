from src import question1
from datastructures.linkedlist import LinkedList

def test_remove_dups():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert str(ll) == '1 --> 2 --> 2 --> 3 --> 4 --> 5'
    question1.remove_dups(ll)
    assert str(ll) == '1 --> 2 --> 3 --> 4 --> 5'