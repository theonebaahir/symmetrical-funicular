from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self,x):
        print("Passed value:", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
class testclass(absclass):
    def task(self):
        print("We are inside testclass task")


testobj = testclass()
testobj.task()
testobj.print(100)