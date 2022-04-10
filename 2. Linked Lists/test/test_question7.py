from datastructures.linkedlist import LinkedList, Node
from src.question7 import intersection

def test_intersection_by_reference_success():
    l1 = LinkedList('list1')
    l2 = LinkedList('list2')
    item2 = Node('item2')
    node1 = Node('intersecting', next=item2)
    item1 = Node('item1', next=node1)
    l1.append(item1)
    l2.append(item2)
    actual = intersection(l1, l2)
    assert actual == item2

def test_intersection_by_value_is_none():
    l1 = LinkedList(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l2 = LinkedList(9)
    l2.append(8)
    l2.append(7)
    l2.append(6)
    l2.append(5)
    actual = intersection(l1, l2)
    assert actual is None