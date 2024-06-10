# List methods - Append, Insert, Remove, Copy (shallow and deeo copy), Count, Extend, Index, Sort, Reverse, Clear, Pop in python

# Create a list
my_list = [1, 2, 3, 4, 5]

# Append - Adds an item to the end of the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Insert - Inserts an item at a specified index
my_list.insert(2, 7)
print(my_list)  # Output: [1, 2, 7, 3, 4, 5, 6]

# Remove - Removes the first occurrence of the specified item
my_list.remove(3)
print(my_list)  # Output: [1, 2, 7, 4, 5, 6]

# Copy (shallow copy)
shallow_copy = my_list.copy()
print(shallow_copy)  # Output: [1, 2, 7, 4, 5, 6]

# Copy (deep copy)
import copy
deep_copy = copy.deepcopy(my_list)
print(deep_copy)  # Output: [1, 2, 7, 4, 5, 6]

# Count - Returns the number of occurrences of an item
count = my_list.count(2)
print(count)  # Output: 1

# Extend - Adds all items from an iterable to the list
my_list.extend([8, 9, 10])
print(my_list)  # Output: [1, 2, 7, 4, 5, 6, 8, 9, 10]

# Index - Returns the index of the first occurrence of an item
index = my_list.index(4)
print(index)  # Output: 3

# Sort - Sorts the list in-place
my_list.sort()
print(my_list)  # Output: [1, 2, 4, 5, 6, 7, 8, 9, 10]

# Reverse - Reverses the order of the list in-place
my_list.reverse()
print(my_list)  # Output: [10, 9, 8, 7, 6, 5, 4, 2, 1]

# Clear - Removes all items from the list
my_list.clear()
print(my_list)  # Output: []

# Pop - Removes and returns the item at the specified index (default is the last item)
my_list = [1, 2, 3, 4, 5]
popped_item = my_list.pop()
print(popped_item)  # Output: 5
print(my_list)  # Output: [1, 2, 3, 4]


# list comprehensions
# List comprehension to create a new list with squared values
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# List comprehension with conditional
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# List comprehension with nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension with string manipulation
names = ['Alice', 'Bob', 'Charlie']
uppercase_names = [name.upper() for name in names]
print(uppercase_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']

# List comprehension with conditional and string manipulation
long_names = [name.lower() for name in names if len(name) > 4]
print(long_names)  # Output: ['alice', 'charlie']

# List comprehension with function
def square(x):
    return x**2

squared_numbers = [square(x) for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# Indexing, Slicing
# Create a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Indexing
print(my_list[0])  # Output: 1 (first element)
print(my_list[3])  # Output: 4 (fourth element)
print(my_list[-1])  # Output: 10 (last element)

# Slicing
print(my_list[2:6])  # Output: [3, 4, 5, 6] (elements from index 2 to 5)
print(my_list[:4])  # Output: [1, 2, 3, 4] (elements from the start to index 3)
print(my_list[6:])  # Output: [7, 8, 9, 10] (elements from index 6 to the end)
print(my_list[::2])  # Output: [1, 3, 5, 7, 9] (every other element)
print(my_list[::-1])  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (reversed list)

# Assigning values using indexing
my_list[0] = 100
print(my_list)  # Output: [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Assigning values using slicing
my_list[2:5] = [20, 30, 40]
print(my_list)  # Output: [100, 2, 20, 30, 40, 6, 7, 8, 9, 10]


#  Special Methods - reduce, map, filter, zip
from functools import reduce

# reduce()
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

# map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# zip()
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]



# Basic searching and sorting in a list
# Linear Search
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

my_list = [5, 2, 9, 1, 7]
print(linear_search(my_list, 9))  # Output: 2
print(linear_search(my_list, 6))  # Output: -1

# Binary Search (requires a sorted list)
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_list = [1, 2, 5, 7, 9]
print(binary_search(sorted_list, 7))  # Output: 3
print(binary_search(sorted_list, 6))  # Output: -1

# Bubble Sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(unsorted_list))  # Output: [11, 12, 22, 25, 34, 64, 90]

# Selection Sort
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(unsorted_list))  # Output: [11, 12, 22, 25, 34, 64, 90]



#  Properties
# Creating tuples
empty_tuple = ()
single_element_tuple = (1,)  # Note the trailing comma
normal_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(normal_tuple[0])  # Output: 1
print(normal_tuple[-1])  # Output: 5

# Immutability
try:
    normal_tuple[0] = 10  # This will raise a TypeError
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated_tuple = ('Hello',) * 3
print(repeated_tuple)  # Output: ('Hello', 'Hello', 'Hello')

# Length
print(len(normal_tuple))  # Output: 5

# Membership
print(3 in normal_tuple)  # Output: True
print(10 not in normal_tuple)  # Output: True

# Iteration
for element in normal_tuple:
    print(element)
# Output:
# 1
# 2
# 3
# 4
# 5

# Unpacking
a, b, c, d, e = normal_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Tuple methods
print(normal_tuple.count(3))  # Output: 1
print(normal_tuple.index(4))  # Output: 3



# List vs Tuple
# Creating a list and a tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# Modifying elements
print("Original list:", my_list)
my_list[0] = 10  # Lists are mutable
print("Modified list:", my_list)

print("\nOriginal tuple:", my_tuple)
try:
    my_tuple[0] = 10  # Tuples are immutable, this will raise an error
except TypeError as e:
    print(e)

# Concatenation
list_concat = my_list + [6, 7, 8]
tuple_concat = my_tuple + (6, 7, 8)
print("\nConcatenated list:", list_concat)
print("Concatenated tuple:", tuple_concat)

# Repetition
repeated_list = my_list * 3
repeated_tuple = my_tuple * 3
print("\nRepeated list:", repeated_list)
print("Repeated tuple:", repeated_tuple)

# Length
print("\nLength of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

# Membership
print("\n3 in list:", 3 in my_list)
print("3 in tuple:", 3 in my_tuple)

# Iteration
print("\nList elements:")
for element in my_list:
    print(element)

print("\nTuple elements:")
for element in my_tuple:
    print(element)


# Indexing and Slicing, Count and Index
# Lists
my_list = [1, 2, 3, 4, 5, 3, 2, 1]

# Indexing
print("Indexing in lists:")
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 4
print(my_list[-1])  # Output: 1 (negative index starts from the end)

# Slicing
print("\nSlicing in lists:")
print(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3])  # Output: [1, 2, 3] (elements from the start to index 2)
print(my_list[5:])  # Output: [3, 2, 1] (elements from index 5 to the end)
print(my_list[::-1])  # Output: [1, 2, 3, 5, 4, 3, 2, 1] (reversed list)

# Count
print("\nCount in lists:")
print(my_list.count(3))  # Output: 2 (count of occurrences of 3)

# Index
print("\nIndex in lists:")
print(my_list.index(4))  # Output: 3 (index of the first occurrence of 4)

# Tuples
my_tuple = (1, 2, 3, 4, 5, 3, 2, 1)

# Indexing
print("\nIndexing in tuples:")
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 4
print(my_tuple[-1])  # Output: 1 (negative index starts from the end)

# Slicing
print("\nSlicing in tuples:")
print(my_tuple[1:4])  # Output: (2, 3, 4) (elements from index 1 to 3)
print(my_tuple[:3])  # Output: (1, 2, 3) (elements from the start to index 2)
print(my_tuple[5:])  # Output: (3, 2, 1) (elements from index 5 to the end)
print(my_tuple[::-1])  # Output: (1, 2, 3, 5, 4, 3, 2, 1) (reversed tuple)

# Count
print("\nCount in tuples:")
print(my_tuple.count(3))  # Output: 2 (count of occurrences of 3)

# Index
print("\nIndex in tuples:")
print(my_tuple.index(4))  # Output: 3 (index of the first occurrence of 4)


# Inbuilt functions for List and Tuple - sum, max, min, avg, len, sort
# Lists
my_list = [5, 2, 8, 1, 9, 3]

# sum()
print("Sum of elements in the list:", sum(my_list))  # Output: 28

# max()
print("Maximum element in the list:", max(my_list))  # Output: 9

# min()
print("Minimum element in the list:", min(my_list))  # Output: 1

# len()
print("Length of the list:", len(my_list))  # Output: 6

# sorted()
print("Sorted list:", sorted(my_list))  # Output: [1, 2, 3, 5, 8, 9]

# Tuples
my_tuple = (5, 2, 8, 1, 9, 3)

# sum()
print("\nSum of elements in the tuple:", sum(my_tuple))  # Output: 28

# max()
print("Maximum element in the tuple:", max(my_tuple))  # Output: 9

# min()
print("Minimum element in the tuple:", min(my_tuple))  # Output: 1

# len()
print("Length of the tuple:", len(my_tuple))  # Output: 6

# sorted()
print("Sorted tuple:", sorted(my_tuple))  # Output: [1, 2, 3, 5, 8, 9]

# Average (not a built-in function)
def calculate_average(sequence):
    return sum(sequence) / len(sequence)

print("\nAverage of list elements:", calculate_average(my_list))  # Output: 4.666666666666667
print("Average of tuple elements:", calculate_average(my_tuple))  # Output: 4.666666666666667



#Intro for Dictionary
# Creating a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values
print(person['name'])  # Output: 'Alice'
print(person.get('age'))  # Output: 25

# Adding or modifying key-value pairs
person['email'] = 'alice@example.com'  # Adding a new key-value pair
person['age'] = 26  # Modifying an existing key-value pair
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Removing key-value pairs
del person['city']
print(person)  # Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# Checking for keys
print('name' in person)  # Output: True
print('occupation' in person)  # Output: False

# Getting keys and values
print(person.keys())  # Output: dict_keys(['name', 'age', 'email'])
print(person.values())  # Output: dict_values(['Alice', 26, 'alice@example.com'])

# Iterating over a dictionary
for key in person:
    print(key, person[key])
# Output:
# name Alice
# age 26
# email alice@example.com

# Length of a dictionary
print(len(person))  # Output: 3

# Clearing a dictionary
person.clear()
print(person)  # Output: {}


# Accessing and modifying values using keys
# Creating a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values using keys
print(person['name'])  # Output: 'Alice'
print(person.get('age'))  # Output: 25

# Accessing a non-existent key (throws KeyError)
try:
    print(person['email'])
except KeyError:
    print("Key 'email' does not exist")

# Accessing a non-existent key (using get() method)
print(person.get('email'))  # Output: None
print(person.get('email', 'No email found'))  # Output: 'No email found'

# Modifying values using keys
person['age'] = 26  # Updating an existing key-value pair
person['city'] = 'San Francisco'  # Modifying an existing key-value pair
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'San Francisco'}

# Adding a new key-value pair
person['email'] = 'alice@example.com'
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'San Francisco', 'email': 'alice@example.com'}

# Removing a key-value pair
del person['city']
print(person)  # Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}



# Dict methods - keys(), values(), items(), etc
# Creating a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

# keys() method
print("Keys:", person.keys())
# Output: Keys: dict_keys(['name', 'age', 'city', 'email'])

# values() method
print("Values:", person.values())
# Output: Values: dict_values(['Alice', 25, 'New York', 'alice@example.com'])

# items() method
print("Items:", person.items())
# Output: Items: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York'), ('email', 'alice@example.com')])

# get() method
print("Age:", person.get('age'))  # Output: Age: 25
print("Phone:", person.get('phone', 'No phone number found'))  # Output: Phone: No phone number found

# pop() method
popped_value = person.pop('city')
print("Popped value:", popped_value)  # Output: Popped value: New York
print("Dictionary after pop():", person)
# Output: Dictionary after pop(): {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}

# popitem() method
popped_item = person.popitem()
print("Popped item:", popped_item)  # Output: Popped item: ('email', 'alice@example.com')
print("Dictionary after popitem():", person)
# Output: Dictionary after popitem(): {'name': 'Alice', 'age': 25}

# update() method
person.update({'city': 'San Francisco', 'email': 'alice@company.com', 'phone': '123-456-7890'})
print("Dictionary after update():", person)
# Output: Dictionary after update(): {'name': 'Alice', 'age': 25, 'city': 'San Francisco', 'email': 'alice@company.com', 'phone': '123-456-7890'}

# clear() method
person.clear()
print("Dictionary after clear():", person)  # Output: Dictionary after clear(): {}
      



# Adding and removing key-value pairs
# Creating a dictionary
person = {'name': 'Alice', 'age': 25}

# Adding a new key-value pair
person['city'] = 'New York'
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Modifying an existing key-value pair
person['age'] = 26
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Adding multiple key-value pairs
person.update({'email': 'alice@example.com', 'phone': '123-456-7890'})
print(person)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com', 'phone': '123-456-7890'}

# Removing a key-value pair
del person['phone']
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Removing a key-value pair and getting its value
popped_value = person.pop('city')
print(popped_value)  # Output: 'New York'
print(person)  # Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# Removing an arbitrary key-value pair
popped_item = person.popitem()
print(popped_item)  # Output: ('email', 'alice@example.com')
print(person)  # Output: {'name': 'Alice', 'age': 26}

# Clearing the dictionary
person.clear()
print(person)  # Output: {}



# Dict comprehension,Nesting dict
# Creating a dictionary from a list
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Creating a dictionary from another dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {key: value * 2 for key, value in original_dict.items()}
print(new_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}

# Conditional dictionary comprehension
even_squared_dict = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squared_dict)  # Output: {2: 4, 4: 16}

# Nested dictionary
person = {
    'name': 'Alice',
    'age': 25,
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY'
    },
    'contact': {
        'phone': '123-456-7890',
        'email': 'alice@example.com'
    }
}

# Accessing nested values
print(person['name'])  # Output: 'Alice'
print(person['address']['city'])  # Output: 'New York'
print(person['contact']['email'])  # Output: 'alice@example.com'

# Modifying nested values
person['age'] = 26
person['address']['street'] = '456 Oak Ave'
print(person)
# Output: {'name': 'Alice', 'age': 26, 'address': {'street': '456 Oak Ave', 'city': 'New York', 'state': 'NY'}, 'contact': {'phone': '123-456-7890', 'email': 'alice@example.com'}}


# data manipulation, filtering, analysis
# Sample data
students = [
    {'name': 'Alice', 'age': 18, 'grade': 'A', 'subjects': ['Math', 'Physics', 'Chemistry']},
    {'name': 'Bob', 'age': 20, 'grade': 'B', 'subjects': ['English', 'History', 'Geography']},
    {'name': 'Charlie', 'age': 19, 'grade': 'A', 'subjects': ['Math', 'Physics', 'Biology']},
    {'name': 'David', 'age': 21, 'grade': 'C', 'subjects': ['English', 'Art', 'Music']},
    {'name': 'Eve', 'age': 19, 'grade': 'B', 'subjects': ['Math', 'Physics', 'Computer Science']}
]

# Data manipulation
# Adding a new key-value pair
for student in students:
    student['is_adult'] = student['age'] >= 18

# Filtering
# Get students with grade 'A'
top_students = [student for student in students if student['grade'] == 'A']
print("Top Students:")
for student in top_students:
    print(student['name'])

# Get students taking 'Math'
math_students = [student for student in students if 'Math' in student['subjects']]
print("\nMath Students:")
for student in math_students:
    print(student['name'])

# Analysis
# Count students by grade
grade_counts = {}
for student in students:
    grade = student['grade']
    if grade in grade_counts:
        grade_counts[grade] += 1
    else:
        grade_counts[grade] = 1

print("\nGrade Counts:")
for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count} students")

# Get subjects taken by all students
all_subjects = set()
for student in students:
    subjects = set(student['subjects'])
    all_subjects.update(subjects)

print("\nSubjects taken by all students:", ', '.join(all_subjects))


# choosing betweek sets and dict
# Example data
data = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Using a set
unique_data_set = set(data)
print("Unique data using set:", unique_data_set)

# Using a dict
unique_data_dict = {}
for item in data:
    unique_data_dict[item] = True
print("Unique data using dict:", list(unique_data_dict.keys()))

# When to use a set:
# - You only need to store unique values
# - You don't need to store additional information about each value
# - You need to check membership quickly (e.g. `x in my_set`)
# - You need to perform set operations (e.g. union, intersection, difference)

# When to use a dict:
# - You need to store additional information about each value
# - You need to look up values by key quickly (e.g. `my_dict[x]`)
# - You need to iterate over the key-value pairs in a specific order

# In this example, if we only need to store unique values, a set is a better choice.
# But if we need to store additional information about each value, a dict is a better choice.

# For example, let's say we want to store the count of each value:
unique_data_dict_with_count = {}
for item in data:
    if item in unique_data_dict_with_count:
        unique_data_dict_with_count[item] += 1
    else:
        unique_data_dict_with_count[item] = 1
print("Unique data with count using dict:", unique_data_dict_with_count)


# Creating Sets : set() constructor, curly braces {}
my_set = set([1, 2, 3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Basic Operations : Union, intersection, difference, symmetric difference
# define two sets
a = set([1, 2, 3])
b = set([2, 3, 4])

# Union
result = a.union(b)
print("Union: ", result)

# Intersection
result = a.intersection(b)
print("Intersection: ", result)

# Difference
result = a.difference(b)
print("Difference: ", result)

# Symmetric Difference
result = a.symmetric_difference(b)
print("Symmetric Difference: ", result)


# Set methods - add(), remove(), discard(), clear(), etc
# create a set
my_set = {1, 2, 3, 4, 5}

# add an element
my_set.add(6)
print("After adding 6: ", my_set)

# update a set with another set
another_set = {6, 7, 8}
my_set.update(another_set)
print("After updating with another set: ", my_set)

# remove an element
my_set.remove(7)
print("After removing 7: ", my_set)

# discard an element (does not raise an error if the element is not present)
my_set.discard(9)
print("After discarding 9: ", my_set)

# pop an arbitrary element
popped_element = my_set.pop()
print("Popped element: ", popped_element)
print("After popping: ", my_set)

# clear the set
my_set.clear()
print("After clearing: ", my_set)

# copy a set
original_set = {1, 2, 3}
copied_set = original_set.copy()
print("Copied set: ", copied_set)

# difference_update (remove elements that are present in another set)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)
print("After difference update: ", set1)

# intersection_update (keep only elements that are present in another set)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print("After intersection update: ", set1)

# symmetric_difference_update (keep only elements that are present in either set, but not both)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print("After symmetric difference update: ", set1)

# isdisjoint (check if two sets have no elements in common)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("Is disjoint: ", set1.isdisjoint(set2))

# issubset (check if all elements of one set are present in another set)
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("Is subset: ", set1.issubset(set2))

# issuperset (check if all elements of another set are present in one set)
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print("Is superset: ", set1.issuperset(set2))


# Checking membership with in keyword, Set comprehension
# Checking membership with the `in` keyword
my_set = {1, 2, 3, 4, 5}
print(2 in my_set)  # True
print(6 in my_set)  # False

# Set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5, 6]
unique_numbers = {num for num in numbers}
print(unique_numbers)  # {1, 2, 3, 4, 5, 6}

# Checking membership with the `in` keyword and set comprehension
states = ['Gujarat', 'Maharashtra', 'Rajasthan']
capitals = ['Gandhinagar', 'Mumbai', 'Jaipur']
state_capital_map = {state: capital for state, capital in zip(states, capitals)}
print('Rajasthan' in state_capital_map)  # True
print('Delhi' in state_capital_map)  # False

# Checking if all elements of a list are present in another list
target_list = [6, 4, 8, 9, 10]
test_list = [4, 6, 9]
print(all(element in target_list for element in test_list))  # True

# Checking if all elements of a set are present in another set
target_set = {6, 4, 8, 9, 10}
test_set = {4, 6, 9}
print(test_set.issubset(target_set))  # True


# Adv set operations and examples
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Using the & operator
intersection_set = set1 & set2
print(intersection_set)  # {3, 4, 5}

# Using the intersection() method
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3, 4, 5}
