from abc import ABC# which is the abstract module abc
class Animal(ABC):
 
    def move(self): # A method without a body  which is going to acts as a decorator  
        pass
 
class Human(Animal):
 
    def move(self):   # here we redefined move method
        print("I can walk and run")
 
class Snake(Animal):
 def move(self):
        print("I can crawl")
 

         

R = Human()
R.move()
 
K = Snake()
K.move()
