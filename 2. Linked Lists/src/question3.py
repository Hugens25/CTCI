from datastructures.linkedlist import Node

def delete_middle_node(node: Node):
    """
    Implement an algorithm to delete a node in the 
    middle (i.e., any node but the first and last node,
    not necessarily the exact middle) of a singly linked list,
    given only access to that node.
    """
    if node.prev and node.next:
        node.prev.next = node.next
        node.next.prev = node.prev