'''
1. the purpose of a moudle is to be able to use 
functions, packages and other features that have been 
made already, short cuts the amont of work you would need to do 

2. The difference between a class and an object is that an object is an insatnce 
of a class, you cannot modify the contents of it with an object ref. 

3. Inheritence allows for users prevent repetition. If child classes 
need the same methods and variables then its best for the parent class 
to already have these so the child class can inheriet them and also have 
chaarceristics aside from thos. 
'''

'''Coding questions
1. Write a python class that represents a person. Class should gave a consutrcutor
that takes i persons name and age. Should also have a method that prints 
out persons name and age

2. Uses inheritence from a parent class. The parent class should have a method 
that prints out I am the parent and child class should have a method that 
prints out i am the child. Instantoate both classes and call their respective methods

'''

#Inheritence
class Parent():
    def print_Parent(self):
        print("I am the parent")
        
class Child(Parent): 
    def print_Child(self):
        print("I am the child")
    
p = Parent()
c1 = Child()

p.print_Parent()
c1.print_Child()


'''Inheritance 
Create parent class called Animal that has method called speak. CReate
a chold class called dog that inherits from ANimal class and overrides
speak method to print out "woof". Instantiate Dog class and call speak method. 
'''
class Animal():
    def speak(self):
        print("speak")
class Dog(Animal):
    def speak(self): 
        print("Woof")
        
dog = Dog()
dog.speak()


'''Composition and Inheritance 
Create a class that represents a car and another class that reprecents an 
engine. The car class should have an instance of the engine class as one
pf its attributes. Instantiate car object and call a method that prints out 
engine's horsepower.
'''
class engine():
    def __init__(self, horsepower):
        self.horsepower = horsepower
        
class Car():
    def __init__(self, engine):
        self.engine = engine
    def get_hp(self):
        print(f"The engine horsepower is {self.engine.horsepower}.")
    
engine = engine(400)
car = Car(engine)
car.get_hp()


'''Regular expression
used regular expression to validate an email address. prompts user to enter 
email address and prints whther email address valid or not 
'''
import re
userInput = input("Enter your email: ")
email = r"\S+@\w+.\w+"
    
if re.match(email, userInput):
    print("True")
else: 
    print("False")
    

'''Reads txt file 
Reads txt file and prints out th enumber of words in the file 
'''
filename = input("Enter file name: ")
with open(filename, "r") as file:
    content = file.read()
    count = len(content.spilt())
print(f"There are {count} words")


'''Connects mysql database and retrieves data from a table. P
prints out the data retrieved 
'''   
import sqlite3

#connecting to memory
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

#reteicing with read
sq = '''SELECT *
          FROM dataset'''
data = cursor.execute(sq).fetchall()
print(data)

#commit and close
conn.commit()
conn.close()



