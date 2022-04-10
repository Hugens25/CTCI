from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: Any
    prev: Node = None
    next: Node = None

    def __str__(self) -> str:
        return self.data
    
    def __eq__(self, other: Node) -> bool:
        if not other:
            return False
        return other.data == self.data

@dataclass
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = None
        self.size = 1
    
    def __str__(self):
        node = self.head
        data = []
        while node:
            data.append(str(node.data))
            node = node.next
        return ' --> '.join(data)
    
    def __repr__(self):
        node = self.head
        data = []
        while node:
            data.append(str(node.data))
            node = node.next
        return f'LinkedList({", ".join(data)})'
    
    def __len__(self):
        return self.size
    
    def __eq__(self, other: LinkedList) -> bool:
        if other.size != self.size:
            return False
        other_node = other.head
        self_node = self.head
        while other_node:
            if other_node != self_node:
                return False
            other_node = other_node.next
            self_node = self_node.next
        return True

    def append(self, data: Any):
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data)
        if self.tail is None:
            node.prev = self.head
            self.head.next = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def prepend(self, data: Any):
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data)
        if self.tail is None:
            self.tail = self.head
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
    
    def remove(self, node: Node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1
    
    def get(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        raise ValueError('A node does not exist with the provided data. '
                         f'Data: {data}')
