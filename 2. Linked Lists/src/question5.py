from datastructures.linkedlist import LinkedList

def sum_lists(l1: LinkedList, l2: LinkedList):
    """
    You have two numbers represented by a linked list, 
    where each node contains a single digit.
    The digits are stored in reverse order, such that the 1 's digit 
    is at the head of the list. Write a function that adds the two 
    numbers and returns the sum as a linked list.

    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem.
    ^^ Not Implemented. But could this be done by starting the arithmatic from tail?
    """
    carry_value = 0
    if not l1:
        return l2
    if not l2:
        return l1
    
    smaller_list = l1 if len(l1) <= len(l2) else l2
    bigger_list = l2 if smaller_list == l1 else l1
    
    small_list_node = smaller_list.head
    big_list_node = bigger_list.head
    sum = small_list_node.data + big_list_node.data
    value = sum % 10
    carry_value = 1 if sum > 9 else 0
    sum_list = LinkedList(value)
    small_list_node = small_list_node.next
    big_list_node = big_list_node.next
    while small_list_node:
        sum = small_list_node.data + big_list_node.data + carry_value
        value = sum % 10
        carry_value = 1 if sum > 9 else 0
        sum_list.append(value)
        small_list_node = small_list_node.next
        big_list_node = big_list_node.next
    while big_list_node:
        sum = big_list_node.data + carry_value
        value = sum % 10
        carry_value = 1 if sum > 9 else 0
        sum_list.append(value)
        big_list_node = big_list_node.next

    return sum_list