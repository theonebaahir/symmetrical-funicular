from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
          pass
class human(animal):
    def movce(self):
        print("I can walk")
class snake(animal):
    def movce(self):
        print("I can walk")
class dog(animal):
    def movce(self):
        print("I can walk")
class lion(animal):
    def movce(self):
        print("I can walk")

r = human()
r.movce()

k = snake()
k.movce

a = dog()
a.movce

b = lion()
b.movce


    
     
    