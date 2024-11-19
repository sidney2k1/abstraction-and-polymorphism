from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,x):
        print("Passed Value",x)
    @abstractmethod
    def task(self):
        print("This is an abstract class ")
class testclass(absclass):
    def task(self):
        print("We are inside test class")
testobj=testclass()
testobj.task()
testobj.print(100)