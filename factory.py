from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

    def get_animal(self):
        animal = self.create_animal()
        return animal

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

dog_factory = DogFactory()
dog = dog_factory.get_animal()
print(dog.speak())  

cat_factory = CatFactory()
cat = cat_factory.get_animal()
print(cat.speak()) 
