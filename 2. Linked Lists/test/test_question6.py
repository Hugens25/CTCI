from datastructures.linkedlist import LinkedList
from src import question6

def test_palindrome():
    ll = LinkedList('r')
    ll.append('a')
    ll.append('c')
    ll.append('e')
    ll.append('c')
    ll.append('a')
    ll.append('r')
    assert question6.palindrome(ll) == True

def test_palindrome_example_2():
    ll = LinkedList('t')
    ll.append('o')
    ll.append('o')
    ll.append('t')
    assert question6.palindrome(ll) == True

def test_palindrome_false():
    ll = LinkedList('r')
    ll.append('a')
    ll.append('c')
    ll.append('e')
    ll.append('c')
    ll.append('a')
    ll.append('r')
    ll.append('s')
    ll.append('e')
    assert question6.palindrome(ll) == False
