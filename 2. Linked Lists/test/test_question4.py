from src import question4
from datastructures.linkedlist import LinkedList

def test_partition():
    ll = LinkedList(3)
    ll.append(4)
    ll.append(2)
    ll.append(1)
    ll.append(5)
    ll = question4.partition(ll, 2)
    assert str(ll) == '1 --> 3 --> 4 --> 2 --> 5'

def test_partition():
    ll = LinkedList(3)
    ll.append(5)
    ll.append(8)
    ll.append(5)
    ll.append(10)
    ll.append(2)
    ll.append(1)
    ll = question4.partition(ll, 5)
    assert str(ll) == '3 --> 2 --> 1 --> 5 --> 8 --> 5 --> 10'