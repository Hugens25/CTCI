from datastructures.linkedlist import LinkedList

def palindrome(ll: LinkedList):
    begin = ll.head
    end = ll.tail
    count = 0

    while begin and end and begin.next != end.next and begin.prev != end.prev:
        count += 1
        if count >= ll.size // 2:
            return True
        if begin.data == end.data:
            begin = begin.next
            end = end.prev
            continue
        return False
    return True