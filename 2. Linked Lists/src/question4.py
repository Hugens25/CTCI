from typing import Any
from datastructures.linkedlist import LinkedList

def partition(ll: LinkedList, partition: Any):
    """
    Write code to partition a linked list around a value x,
    such that all nodes less than x come before all nodes
    greater than or equal to x. If x is contained within the list,
    the values of x only need to be after the elements less than x (see below).
    The partition element x can appear anywhere in the "right partition";
    it does not need to appear between the left and right partitions.
    """
    node = ll.head
    nodes_to_relocate = []
    while node:
        next_node = node.next
        if node.data >= partition:
            nodes_to_relocate.append(node)
            ll.remove(node)
        node = next_node
    for node in nodes_to_relocate:
        ll.append(node.data)
    return ll