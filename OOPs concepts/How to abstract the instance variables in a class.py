from abc import ABC
class student:
    def __init__(self, name, rollno):  # By using self and abject referencen we can abstract the instance variables
         
        self.name = name
        self.rollno = rollno
       
    def display(self):
        print("hello my name is:", self.name)
        print("my roll number is:", self.rollno)
s = student('sunny', 101)
s.display()

print(s.name)   





