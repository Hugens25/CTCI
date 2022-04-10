from src import question5
from datastructures.linkedlist import LinkedList

def test_sum_lists():
    l1 = LinkedList(7)
    l1.append(1)
    l1.append(6)
    l2 = LinkedList(5)
    l2.append(9)
    l2.append(2)
    expected = LinkedList(2)
    expected.append(1)
    expected.append(9)
    actual = question5.sum_lists(l1, l2)
    assert actual == expected

def test_sum_lists_diff_list_lens():
    l1 = LinkedList(9)
    l1.append(0)
    l1.append(0)
    l1.append(0)
    l1.append(0)
    l1.append(0)
    l1.append(1)
    l2 = LinkedList(2)
    expected = LinkedList(1)
    expected.append(1)
    expected.append(0)
    expected.append(0)
    expected.append(0)
    expected.append(0)
    expected.append(1)
    actual = question5.sum_lists(l1, l2)
    assert actual == expected