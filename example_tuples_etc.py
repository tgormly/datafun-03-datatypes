"""
Tuples, sets, and dictionaries are all iterable objects. 
That means that they can be used in a for loop.
And with filter() and map() functions (better!)
And with comprehension syntax (the best!)

Here are some examples for tuples, sets, and dictionaries.

"""

# import any modules first


"""

TUPLES .......................................................

In Python, a tuple is a immutable sequence type. 
This means that once you create a tuple, 
you cannot change the values it contains: 
you can't add, remove, or change the values of any of the elements 
    in the tuple.
Tuples are created using parentheses.

You can access the elements of a tuple using indexing, like a list.
The first index is 0 and the last index is -1.

Since a tuple (like a list) is ordered, you can use slicing to get a
range of elements from the tuple. [start:end:step]

Tuples support concatenation, repetition, and membership testing.

Tuples enable a function to return multiple values, for example:
(slope, intercept) = statistics.linear_regression(xlist, ylist)
(host, port) = get_host_and_port()

Tuples are often used as keys in dictionaries.


"""


# Create some tuples
tupleA = (1, 2, 3, 4, 5)
tupleB = (4, 5, 6, 7, 8)

# tuple concatenation
tupleCat = tupleA + tupleB

# tuple repetition
tupleAThrice = tupleA * 3

# TODO: Start using this f-string "syntactic sugar" for quick ouptut
# just add space = space inside the curly braces
# it will print the name of the variable and the value
print(f"{tupleA = }") # this is very cool!  I assumed you needed to do f"tupleA = {tupleA}"
print(f"{tupleB = }")
print(f"{tupleCat = }")
print(f"{tupleAThrice = }")

# tuple membership testing

tupleD = (1, 2, 3)
hasOne = 1 in tupleD  # True
hasFour = 4 in tupleD  # False


# tuple indexing (0 is first, -1 is last, or 1 less than the length)

my_tuple = (1, 2, 3)
first = my_tuple[0]

print(f"{my_tuple[0] = }") # this synactic sugar works with index references too

second = my_tuple[1]
third = my_tuple[2]
last = my_tuple[-1]


# Use tuples to return multiple values from a function


def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


q, r = divide_and_remainder(10, 3)
print(f"Quotient: {q}, Remainder: {r}")
"""

SETS .......................................................    


A set is an unordered collection of unique elements.
A set is created using curly braces.
Sets can use the same methods as lists and tuples.
Sets support the following operations:

Membership testing (using the in and not in operators)
Element addition (using the add method)
Element removal (using the remove and discard methods)
Set union (using the union method or the | operator)
Set intersection (using the intersection method or the & operator)
Set difference (using the difference method or the - operator)
Set symmetric difference (using the symmetric_difference method or ^ operator)


"""


setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print(f"{setA = }") 
print(f"{setB = }")
# set union
setC = setA | setB
print(f"{setC = }")

# set intersection
setD = setA & setB
print(f"{setD = }")

# set difference
setE = setA - setB
print(f"{setE = }") # contains values from set A, minus all values in set B

# sets are often used to remove duplicates from a list
# after gettin the set, convert it back to a list with list() or []
listWords = ["apple", "banana", "apple", "pear", "banana", "orange"]
setWords = set(listWords)
listWordsNoDuplicates = list(setWords)

print(f"{listWordsNoDuplicates = }")

listWordsNoDuplicates = [setWords]  # same as above - except this appears to create a list with one item at index 0, a set of pear orange apple banana, where the code on line 136 creates just a list without duplicates

print(f"{listWordsNoDuplicates = }")
print(f"{listWordsNoDuplicates[0] = }")
# print(f"{listWordsNoDuplicates[0][1] = }") # this does not work as sets are unordered and their items are not indexed

"""


DICTIONARIES .......................................................    

A dictionary is an unordered collection of key-value pairs.
A dictionary is created using curly braces.
A dictionary is accessed using keys, not indexes.
A dictionary is mutable, so you can add, remove, and change values.
A dictionary is iterable, so you can use it in a for loop.
A dictionary is not ordered, so you can't slice to access a range of values.

Dictionaries support the following operations:

Indexing: access the value associated with a key in the dictionary. 
For example: dogA['name'].

Membership testing: use 'in' and 'not in' operators 
to test whether a key is in the dictionary. 
For example: 'name' in dogA.

Adding and updating items: use indexing to add a new key-value pair,
or to update the value associated with an existing key. 
For example: dogA['age'] = 2.

Removing items: Use the del statement to remove a key-value pair. 
For example: del dogA['weight_kg'].

Iteration: You can use a for loop to iterate over the 
keys, values, or key-value pairs in a dictionary. 
For example: for key in dogA: print(key)

Dictionaries are a lot like 
JSON objects - a common data format used in web development.

"""


dogA_dict = {"name": "Rex", "age": 2, "weight_kg": 13.4}
dogB_dict = {"name": "Fido", "age": 3, "weight_kg": 15.2}

assessment_dict = {"low": 0, "medium": 1, "high": 2}

data_dict = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "income": [50000, 60000, 70000, 80000],
}


# Define your PyBuddies in a dictionary
# With few chnages, you could read in many PyBuddies from a JSON file.


# In data anlytics, dictionaries are used to store and manipulate
# tabular data, e.g. from database records or Excel rows.


# Dictionaries can be used to store and aggregate statistical data,
# such as counts or sums. For example, a dictionary of word-count pairs.

with open("text_simple.txt") as file_object:
    word_list = file_object.read().split()

word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1

print(word_counts_dict)


# IMPORTANT: Dictionary comprehesions - the preferred approach

# Create a dictionary of word counts from a list of words
# A dictionary is alawys key:value pairs
# Say "I want word:count for each word in word_list"
# Remember to wrap the result in curly braces
word_counts_dict = {word: word_list.count(word) for word in word_list}

# Spend most of your practice on comprehensions - they are
# key to transforming data in Python.
