#Abstract classes

from abc import ABC,abstractmethod

class Operation(ABC):
      @abstractmethod
      def add():
           print("hello")
      @abstractmethod
      def sub():
          pass
      def mul(self,c,d):
          print(c*d)
          
class Operation1(Operation):

     def __init__(self,a,b):
          self.a=a 
          self.b=b          
     def add(self):
          print(self.a+self.b)
     def sub(self):
          print(self.a-self.b)    
Op1=Operation() 
Op1.add()
Op1.sub() 
Op1.mul(4,3)

