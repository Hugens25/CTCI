from datastructures.linkedlist import LinkedList, Node

def kth_to_last(ll: LinkedList, k: int, node: Node = None, 
                total: int = 0, idx_to_find: int = 0):
    """
    Implement an algorithm to find the kth to 
    last element of a singly linked list.
    """
    idx = 0
    node = ll.head
    vals = {}
    total_nodes = 0
    kth_idx = 0
    while node:
        vals[idx] = node
        idx += 1
        node = node.next
        total_nodes += 1
    kth_idx = total_nodes - k

    return vals[kth_idx]

