from src.question6 import AnimalShelter, Animal, Animals

def test_animal_shelter():
    shelter = AnimalShelter()
    animals = [
        Animal(type=Animals.DOG, name='DOG 1'),
        Animal(type=Animals.CAT, name='CAT 1'),
        Animal(type=Animals.CAT, name='CAT 2'),
        Animal(type=Animals.DOG, name='DOG 2'),
        Animal(type=Animals.CAT, name='CAT 3'),
        Animal(type=Animals.DOG, name='DOG 3')
    ]
    for animal in animals:
        shelter.enqueue(animal)
    
    animal = shelter.dequeueAny()
    assert animal.data.type == Animals.DOG
    assert animal.data.name == 'DOG 1'
    
    animal = shelter.dequeueDog()
    assert animal.data.type == Animals.DOG
    assert animal.data.name == 'DOG 2'

    animal = shelter.dequeueAny()
    assert animal.data.type == Animals.CAT
    assert animal.data.name == 'CAT 1'
    
    animal = shelter.dequeueCat()
    assert animal.data.type == Animals.CAT
    assert animal.data.name == 'CAT 2'

    assert shelter.size() == 2

    assert shelter.first.data.type == Animals.CAT
    assert shelter.first.data.name == 'CAT 3'
    
    assert shelter.first.next.data.type == Animals.DOG
    assert shelter.first.next.data.name == 'DOG 3'

    assert shelter.first.next.next == None