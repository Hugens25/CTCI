from src import question8
from datastructures.linkedlist import LinkedList, Node

def test_loop_detection_by_reference_success():
    node5 = Node(5)
    node4 = Node(4, next=node5)
    node3 = Node(3, next=node4)
    node2 = Node(2, next=node3)
    ll = LinkedList(1)
    ll.append(node2)
    ll.append(node3)
    ll.append(node4)
    ll.append(node5)
    ll.append(node3)
    assert question8.loop_detection(ll) == node3

def test_loop_detection_by_value_is_none():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(3)
    assert question8.loop_detection(ll) is None