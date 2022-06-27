from dataclasses import dataclass
from typing import List
from datastructures.stack import Stack, Node

@dataclass
class SetOfStacks(Stack):
    """
    3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack
    exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
    SetO-fStacks should be composed of several stacks and should create a new stack once
    the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should
    behave identically to a single stack (that is, pop() should return the same values as
    it would if there were just a single stack).

    FOLLOW UP
    Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
    """
    stacks: List[Stack] = None
    capacity: int = 5
    def push(self, item):
        if not self.top or self.top.data.size() >= self.capacity:
            stack = Stack()
            stack.push(item)
            stack.top.next = self.top.data.top if self.top else None
            if self.stacks:
                self.stacks.insert(0, stack)
            else:
                self.stacks = [stack]
            super().push(stack)
        else:
            self.top.data.push(item)
    
    def pop(self):
        if self.top and self.top.data.top:
            return self.top.data.pop()
        if not self.top and self.top.next:
            self.top = self.top.next
            return self.top.data.pop()

    def pop_at(self, index):
        return self.stacks[index].pop()