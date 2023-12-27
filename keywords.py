
#  classes and object 
"""
Define a class called Person with attributes name and age.
Create an object of this class and demonstrate how to set and retrieve the values of the attributes."""

"""
class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def setname(self,new_name):
        self.name= new_name
    def setage(self,new_age):
        self.age= new_age 


person1 = Person("vinit jain", 20)

print("initial name " ,person1.getname())
print("initial age " ,person1.getage())

person1.setname("jain vinit")
person1.setage(21)

print("updated name " ,person1.getname())
print("updated age " ,person1.getage())    """
"""

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age


# Create an object of the Person class
person1 = Person("vinit jain", 20)

# Retrieve and print the initial values
print("Initial Name:", person1.get_name())
print("Initial Age:", person1.get_age())

# Set new values for name and age
person1.set_name("John Doe")
person1.set_age(25)

# Retrieve and print the updated values
print("\nUpdated Name:", person1.get_name())
print("Updated Age:", person1.get_age())
"""
"""
class Shape :
    def __init__ (self ,color):
        self.color =color
        
    def area(self):
        return 0
    
    

class Circle(Shape):
    def __init__(self , color , radius):
        super(). __init__(color)
        self.radius = radius
    def area (self):
        return 3.14* self.radius**2
   

class Rect(Shape):
    def __init__(self , color , len , high):
        super(). __init__(color)
        self.len  = len
        self.high  = high 

    def area (self):
        return self.len * self.high
    
circle = Circle("red",2)
rect = Rect("blue",2,3)


print ("area of circle ", circle.area())
print ("area of rectangle " ,rect.area())
     
"""

#Encapsulation

"""
Create a Car class with private attributes (__model and __speed). 
Implement methods to get and set these attributes with proper encapsulation.

"""
"""
class Car : 
    def __init__(self ,model, speed):
        self.__model = model
        self.__speed = speed
    def getmodel(self):
        return self.__model
    def setmodel(self, new_model):
        self.__model = new_model
    def getspeed(self):
        return self.__speed
    
    def setspeed(self, new_speed):
        if new_speed >= 0:
            self.__speed = new_speed
        else:
            print("Speed must be a non-negative value.")

car1 = Car("Toyota", 60)

# Retrieve and print the initial values
print("Initial Model:", car1.getmodel())
print("Initial Speed:", car1.getspeed())



# Set new values for model and speed

car1.setmodel("Nissan")
car1.setspeed(100)

print("New Model:", car1.getmodel())
print("New Speed:", car1.getspeed())

car1 = Car("Mahindra", 50)
print(car1._Car__model)
print(car1._Car__speed)

"""
#Inheritance

"""
Create a base class Shape with a method area. 
Derive two classes Circle and Rectangle from Shape to 
calculate the area of a circle and a rectangle, respectively.
"""
"""
class Shape :
    def area (self):
        pass
class Circle (Shape):

    def __init__(self ,radius):
        self.radius = radius
    def area(self):
        return 3.14* self.radius**2

class Rect (Shape):

    def __init__(self ,len , high):
        self.len = len
        self.high = high
    def area(self):
        return self.len * self.high
    
circle= Circle(2)
rect= Rect(9,4)

print("area of circle ", circle.area())
print("area of circle ", rect.area())
        
"""

#Polymorphism: 
"""
Define a class Animal with a method speak. Create subclasses Dog, Cat, and Cow, 
each overriding the speak method to produce a different sound.
Demonstrate polymorphism by calling the speak method on objects of these classes.
"""

"""
class Animal:
    def speak(self):
        pass
class Dog :   
    def speak (self):
        return "woof"

class Cat :   
    def speak (self):
        return "meaw"

class Cow :   
    def speak (self):
        return "moooooooo......"

def Animalclass(ani_instance):
    print("{} su bole" ,ani_instance.speak())

dog1=Dog()
m=Cat()
c=Cow()


Animalclass(dog1)
Animalclass(m)
Animalclass(c)
"""




#Composition:
"""
Create a class Author with attributes name and books (a list of book titles). 
Then, create a class Book with attributes title, published_year, and author (an instance of the Author class)."""
"""
class Author:
    def __init__(self, name, books=None):
        self.name = name
        self.books = books if books is not None else []

    def add_book(self, title):
        self.books.append(title)

class Book:
    def __init__(self, title, published_year, author):
        self.title = title
        self.published_year = published_year
        self.author = author

# Example usage:
# Create an author
author1 = Author("John Doe")

# Add books to the author
author1.add_book("Book1")
author1.add_book("Book2")

# Create a book with the author
book1 = Book("Book1", 2022, author1)

# Accessing attributes
print(f"Book Title: {book1.title}")
print(f"Published Year: {book1.published_year}")
print(f"Author: {book1.author.name}")
print(f"Author's Books: {book1.author.books}")"""



#Method Overloading:
"""
Implement a class Calculator with methods for addition, subtraction, and multiplication.
 Use method overloading to create a new method that can handle variable numbers of arguments for addition."""

#Multiple Inheritance:
"""
Create classes Person, Employee, and Manager.
Use multiple inheritance to derive the Manager class from both Person and Employee. 
Include appropriate attributes and methods for each class."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Person: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: ${self.salary}")


class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Call the constructors of both base classes
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)

        # Additional attribute for Manager
        self.department = department

    def display_info(self):
        # Override display_info method to include Manager-specific information
        Person.display_info(self)
        Employee.display_info(self)
        print(f"Manager Department: {self.department}")


# Example usage:
manager1 = Manager("John Doe", 35, "E123", 75000, "Sales")

# Call the display_info method on the Manager object
manager1.display_info()


#Operator Overloading:
"""
Overload the + operator for a custom class. 
For example, create a class representing a complex number and define the __add__ method to add two complex numbers."""

#Abstract Base Class:
"""
Define an abstract base class Shape with an abstract method area.
 Create concrete classes Circle and Rectangle that inherit from Shape and implement the area method. """

#Singleton Pattern:
"""
Implement a singleton class that allows only one instance to be created. 
For example, create a Logger class that logs messages, ensuring there's only one logger instance."""

    
# Geeks of geeks
"""
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
 
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)"""