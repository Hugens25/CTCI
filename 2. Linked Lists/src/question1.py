from datastructures.linkedlist import LinkedList

def remove_dups(ll: LinkedList):
    """
    2.1 Write code to remove duplicates from an unsorted linked list

    Q: How would you solve this problem if a temporary buffer is not allowed?
    A: Sort, then check if neighboring nodes have same data.
    """
    node = ll.head
    existing_data = []
    while node:
        if node.data in existing_data:
            ll.remove(node)
        else:
            existing_data.append(node.data)
        node = node.next
