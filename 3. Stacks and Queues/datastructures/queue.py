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
class Queue:
    first: Node = None
    last: Node = None
    count: int = 0
    
    def add(self, item):
        node = item if isinstance(item, Node) else Node(item)
        if self.last:
            self.last.next = node
        self.last = node
        if not self.first:
            self.first = self.last
        self.count += 1
    
    def remove(self):
        if self.first:
            item = self.first
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self.count -= 1
            return item
        return None
    
    def peek(self):
        if self.first:
            return self.first.data
        return None
    
    def isEmpty(self):
        return self.first is None
    
    def size(self):
        return self.count
    
    def lineage(self):
        node = self.first
        nodes = []
        while node:
            nodes.append(str(node))
            node = node.next
        return ' -> '.join(nodes)
    
    def __str__(self) -> str:
        return f"(First={self.first.data}, Last={self.last.data}, Count={self.count}, Next={self.first.next})"

    def __repr__(self) -> str:
        nodes = []
        node = self.first
        while node:
            nodes.append(str(node.data))
            node = node.next
        return '-> '.join(nodes)
