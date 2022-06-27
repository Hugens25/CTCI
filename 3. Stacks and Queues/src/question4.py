from dataclasses import dataclass
from datastructures.stack import Stack

@dataclass
class MyQueue:
    add_stack: Stack
    remove_stack: Stack

    def add(self, item):
        self.add_stack.push(item)
        self.remove_stack.push(item)
    
    def remove(self):
        pass