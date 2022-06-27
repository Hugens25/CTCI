from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    data: Any
    next: Node = None

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"Node({self.data})"

@dataclass
class Stack:
    top: Node = None
    count: int = 0

    def pop(self):
        if self.top:
            item = self.top
            self.top = self.top.next
            self.count -= 1
            return item
        return None
    
    def push(self, item):
        node = item if isinstance(item, Node) else Node(item)
        node.next = self.top
        self.top = node
        self.count += 1
    
    def peek(self):
        if self.top:
            return self.top.data
        return None
    
    def isEmpty(self):
        return self.top is None
    
    def size(self):
        return self.count
    
    def lineage(self):
        node = self.top
        nodes = []
        while node:
            nodes.append(str(node))
            node = node.next
        return ' -> '.join(nodes)
    
    def __str__(self) -> str:
        return f"(Top={self.top.data}, Count={self.count}, Next={self.top.next})"

    def __repr__(self) -> str:
        nodes = []
        node = self.top
        while node:
            nodes.append(str(node.data))
            node = node.next
        return '-> '.join(nodes)
