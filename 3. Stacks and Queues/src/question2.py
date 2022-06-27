from dataclasses import dataclass
from datastructures.stack import Stack

@dataclass
class MinStack(Stack):
    """
    3.2 How would you design a stack which, in addition to push and pop,
    has a function min which returns the minimum element? Push, pop and min
    should all operate in 0(1) time.
    """
    min_val: int = None

    def min(self):
        return self.min_val

    def push(self, item):
        if self.min_val is None:
            self.min_val = item

        if item < self.min_val:
            self.min_val = item
        super().push(item)

    