# Define a class
class Animal:
    # Class attribute
    species = "mammal"

    # Initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def speak(self):
        print(f"{self.name} makes a sound.")

    # Another method
    def describe(self):
        print(f"{self.name} is {self.age} years old and belongs to the {self.species} species.")

# Create objects (instances of the class)
dog = Animal("Buddy", 5)
cat = Animal("Whiskers", 3)

# Access attributes
print(dog.name)  # Output: Buddy
print(cat.age)   # Output: 3

# Call methods
dog.speak()      # Output: Buddy makes a sound.
cat.describe()   # Output: Whiskers is 3 years old and belongs to the mammal species.

# Modify attribute value
dog.age = 6
dog.describe()   # Output: Buddy is 6 years old and belongs to the mammal species.



# Define a class
class Car:
    # Class attribute
    wheels = 4

    # Constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Method
    def accelerate(self, increase):
        self.speed += increase

    # Method
    def brake(self, decrease):
        self.speed -= decrease

    # Method
    def get_info(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"Current speed: {self.speed} mph")

# Create objects (instances of the class)
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)

# Access attributes
print(car1.make)  # Output: Toyota
print(car2.model) # Output: Civic

# Access class attribute
print(Car.wheels) # Output: 4

# Call methods
car1.accelerate(30)
car1.get_info()   # Output: 2020 Toyota Camry
                  #         Current speed: 30 mph

car2.accelerate(40)
car2.brake(10)
car2.get_info()   # Output: 2018 Honda Civic
                  #         Current speed: 30 mph



class BankAccount:
    def __init__(self, name, balance=0):
        self.__name = name  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} to {self.__name}'s account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from {self.__name}'s account.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.__name}'s account balance: {self.__balance}"

# Data encapsulation and data hiding
account = BankAccount("John Doe", 1000)
# account.__balance = 2000  # This will raise an AttributeError

# Abstraction
account.deposit(500)
account.withdraw(200)
print(account)  # Output: John Doe's account balance: 1300

# Accessing the private attribute directly
print(account._BankAccount__balance)  # Output: 1300 (not recommended)



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Instance method
    def area(self):
        return self.length * self.width

    # Instance method
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Instance method
    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    # Class method
    @classmethod
    def from_square(cls, side):
        return cls(side, side)

    # Static method
    @staticmethod
    def is_square(length, width):
        return length == width

# Create a Rectangle object
rect = Rectangle(5, 3)

# Call instance methods
print(rect.area())        # Output: 15
print(rect.perimeter())   # Output: 16

# Call instance method to modify object
rect.resize(7, 4)
print(rect.area())        # Output: 28

# Call class method
square = Rectangle.from_square(4)
print(square.area())      # Output: 16

# Call static method
print(Rectangle.is_square(5, 5))   # Output: True
print(Rectangle.is_square(4, 6))   # Output: False





class Student:
    # Class attribute (shared among all instances)
    school_name = "ABC University"

    def __init__(self, name, age, major):
        # Instance attributes
        self.name = name
        self.age = age
        self.major = major
        self.courses = []  # Empty list to store courses

    def enroll(self, course):
        self.courses.append(course)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
        print(f"Enrolled Courses: {', '.join(self.courses)}")
        print(f"School: {self.school_name}")

# Create instances of the Student class
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 21, "Electrical Engineering")

# Access and modify instance attributes
print(student1.name)  # Output: Alice
student1.age = 21
student1.enroll("Python Programming")
student1.enroll("Data Structures")

# Access class attribute
print(student1.school_name)  # Output: ABC University
print(student2.school_name)  # Output: ABC University

# Modify class attribute
Student.school_name = "XYZ University"
print(student1.school_name)  # Output: XYZ University
print(student2.school_name)  # Output: XYZ University

# Call methods
student1.display_info()
# Output:
# Name: Alice
# Age: 21
# Major: Computer Science
# Enrolled Courses: Python Programming, Data Structures
# School: XYZ University


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    def resize(self, new_radius):
        self.radius = new_radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError("Cannot add Circle and non-Circle objects")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Cannot compare Circle and non-Circle objects")

# Create a Circle object
circle1 = Circle(5)

# Call methods with arguments
print(circle1.area())  # Output: 78.5
print(circle1.circumference())  # Output: 31.4

# Call a method with an argument to modify the object
circle1.resize(10)
print(circle1)  # Output: Circle with radius 10.0

# Special method __str__
print(str(circle1))  # Output: Circle with radius 10.0

# Special method __add__
circle2 = Circle(3)
combined_circle = circle1 + circle2
print(combined_circle)  # Output: Circle with radius 13.0

# Special method __lt__
smaller_circle = circle1 < circle2
print(smaller_circle)  # Output: False



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object created: {self.name}, {self.age}")

    def __del__(self):
        print(f"Person object destroyed: {self.name}, {self.age}")

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Output:
# Person object created: Alice, 25
# Person object created: Bob, 30

# Doing some operations
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# The destructor is automatically called when the object goes out of scope
# or when the program terminates