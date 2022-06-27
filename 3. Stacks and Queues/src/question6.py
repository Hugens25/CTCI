from dataclasses import dataclass
from enum import Enum
from datastructures.queue import Queue

# TODO: Change Enum name from plural to singular
# to follow standard naming conventions
class Animals(Enum):
    DOG = 'DOG'
    CAT = 'CAT'

@dataclass
class Animal:
    type: str
    name: str

    def __str__(self) -> str:
        return f"{self.name.title()} [ {self.type} ]"

    def __repr__(self) -> str:
        return f"Animal(type={self.type}, name={self.name})"


class AnimalShelter(Queue):
    """
    An animal shelter, which holds only dogs and cats,
    operates on a strictly "first in, first out" basis.
    People must adopt either the "oldest" (based on arrival time)
    of all animals at the shelter, or they can select whether they
    would prefer a dog or a cat (and will receive the oldest animal of that type).
    They cannot select which specific animal they would like. Create the data
    structures to maintain this system and implement operations such as
    enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure.
    """
    def enqueue(self, animal: Animal):
        self.add(animal)
    
    def dequeueAny(self):
        return self.remove()
    
    def dequeueSpecific(self, animal_type):
        node = self.first
        if node.data.type == animal_type:
            return self.remove()
        while node:
            if node.next.data.type == animal_type:
                next_animal = node.next
                node.next = node.next.next
                self.count -= 1
                return next_animal
            node = node.next
    
    def dequeueDog(self):
        return self.dequeueSpecific(Animals.DOG)
    
    def dequeueCat(self):
        return self.dequeueSpecific(Animals.CAT)