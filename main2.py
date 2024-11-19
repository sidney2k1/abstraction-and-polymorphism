from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(self):
        print("I can swim")
class lion(animal):
    def move(self):
        print("i can roar")
w=human()
w.move()
x=snake()
x.move()
y=dog()
y.move()
z=lion()
z.move()