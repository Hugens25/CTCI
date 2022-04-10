from src import question3
from datastructures.linkedlist import LinkedList

def test_delete_middle_node_success():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert str(ll) == '1 --> 2 --> 3 --> 4 --> 5'
    question3.delete_middle_node(ll.get(3))
    assert str(ll) == '1 --> 2 --> 4 --> 5'

def test_delete_middle_node_w_head_node_fail():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert str(ll) == '1 --> 2 --> 3 --> 4 --> 5'
    question3.delete_middle_node(ll.get(1))
    assert str(ll) == '1 --> 2 --> 3 --> 4 --> 5'

def test_delete_middle_node_w_tail_node_fail():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert str(ll) == '1 --> 2 --> 3 --> 4 --> 5'
    question3.delete_middle_node(ll.get(5))
    assert str(ll) == '1 --> 2 --> 3 --> 4 --> 5'