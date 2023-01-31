
# (base) C:\Users\timgo>cd c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes\

# (base) c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes>cd c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes\

# (base) c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes>python user_numeric_lists.py
# ============================================================
# Lists 1. List Statistics
# ============================================================
# A for loop is used to create 'list1', a list of integers with random numbers

# 'listx' is created with values 1-10 using a range object

# 'listy' is created by hand to simulate 10 digits with somewhat linear progression


# ~~1.Calculate the mean, median, and mode of list1(hint: import statistics module)~~

# Mean = 9.47
# Median = 9.00
# Mode = 1.00

# ~~2. Caclulate the standard deviation and variance of list1~~

# Standard Deviation = 6.46
# Variance = 41.77
# ============================================================
# Lists 2. Lists - Correlation and Prediction
# ============================================================

# ~~1. Calculate the correlation between listx and listy~~

# statistics.correlation(listx, listy) = 0.98 (rounded to two decimals)

# ~~2. Calculate the slope and the intercept of the best fit line~~

# slope, intercept = statistics.linear_regression(listx, listy) is used to accomplish this

# ~~3. Set a future time = 15~~

# future_x = 15 is used to accomplish this

# ~~4. Predict the y value at a future time y = mx + b where m is the slop and b is the y intercept~~

# The value of y at x = 15 is: 38.61 (rounded to two decimals)
# or without rounding, it is: 38.60606060606061
# ============================================================
# Lists 3. Using Python Built-in Functions
# ============================================================

# The minimum value in list1 is: 1

# The maximum value in list1 is: 20

# The length of list1 is: 30

# The sum of all values in list1 is: 284

# The average of all values in list1 is: 9.466666666666667

# Using set() to remove duplicates, list1 becomes:
# {1, 3, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16, 18, 19, 20}

# sorted(list1):
# [1, 1, 1, 1, 1, 1, 3, 4, 4, 4, 5, 7, 7, 8, 9, 9, 11, 13, 13, 13, 14, 15, 15, 16, 16, 16, 18, 19, 19, 20]

# sorted(list1, reverse=True):
# [20, 19, 19, 18, 16, 16, 16, 15, 15, 14, 13, 13, 13, 11, 9, 9, 8, 7, 7, 5, 4, 4, 4, 3, 1, 1, 1, 1, 1, 1]
# ============================================================
# Lists 4.  List Methods
# ============================================================
# Now we will use list methods on a list numbers equal to the number of goals scored by a hockey player in a given game
# Here is the list we just made:
# [1, 4, 3, 2, 4, 3, 3, 2, 0, 0, 0, 1, 2, 4, 3]

# First we will append to add value because the player played a new game
# The player had an amazing night and scored 6 goals!

# Here is the list after running lst.append(6):
# [1, 4, 3, 2, 4, 3, 3, 2, 0, 0, 0, 1, 2, 4, 3, 6]

# Notice how the new value is added to the end of the list

# Now we will use lst.extend to add another list to the end of lst

# The new list we are adding is: [1, 4, 3, 2, 4, 3, 3, 2, 0, 0, 0, 1, 2, 4, 3, 6]

# When we run lst.extend(lst2), the original list becomes:

# [1, 4, 3, 2, 4, 3, 3, 2, 0, 0, 0, 1, 2, 4, 3, 6, 0, 1, 2]
# Next we will use insert() to add a new value at a specific index

# We'll add 3 to index 0

# After running lst.insert(0, 3), the list becomes:

# [3, 1, 4, 3, 2, 4, 3, 3, 2, 0, 0, 0, 1, 2, 4, 3, 6, 0, 1, 2]

# Now we will remove the number 5 from the list
# After running lst.remove(5), the list becomes:

# [1, 4, 3, 2, 4, 3, 3, 2, 0, 0, 0, 1, 2, 4, 3, 6, 0, 1, 2]

# Notice that only the first instance of the value 3 has been removed - all other instances of 3 remain

# Now, let's see how many times our player scored 2 goals using the lst.count(2)

# The player scored 2 goals in one game 4 time(s)

# Let's now use the sort() method to place the values of the list in ascending order

# This method sorts the list in place, so the actual values in the list have been re-arranged

# Now the list reads as:

# [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 6]

# Let's reverse the order of the list by adding a reverse=True parameter to the sort method

# This method still updates the list in place, truly re-arranging the values.
# See what happens when we print the list:

# [6, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0]

# We can use "lst.copy()" to create a new copy of our list
# See what happens after we assign lst.copy() to the variable lst3 and print it:

# [6, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0]

# The pop() method can be used to remove an item from the list.

# When we run lst.pop(0), the value at index 0 will be removed:

# [4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0]

# If we don't provide an argument for the pop() method, the very last item will be removed instead

# Here is the list after running lst.pop():

# [4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0]
# ============================================================
# Lists 5. List Transformations - Using filter() and map()
# ============================================================

# Now we will use the filter() function to filter our list
# If we run hat_trick_list = filter(hat_trick, lst), the result will be hat_trick_list being an iterable object

# If we try to print it, we only print its location ID

# print(hat_trick_list) outputs: <filter object at 0x00000161F8F036A0>


# Instead, we can iterate over it and print each item using a for loop:

# 4, 4, 4, 3, 3, 3, 3,
# We can achieve the same result using a lambda function, also known as an anonymous function, in place of a pre-defined function.

# The following code produces the same iterable object:

# hat_trick_list = [filter(lambda x: x >= 3, lst)]
# 4, 4, 4, 3, 3, 3, 3,
# We will use lambda expressions for the remainder of this exercise

# Now we will use the map function for a few things

# First, we will find the cuberoot of each value

# Notice that, like filter, this creates an iterable object - if we attempt to print it, we will only print its memory address
# <map object at 0x00000161F8F03A00>

# print(cube_root_list) outputs: None
# Using a for loop, we can print each value like so:

# 1.59, 1.59, 1.59, 1.44, 1.44, 1.44, 1.44, 1.26, 1.26, 1.26, 1.26, 1.00, 1.00, 1.00, 0.00, 0.00, 0.00,
# Now let's try to cube each value in our original list

# Here is the output of iterating over our new map object with cubed values:

# 64, 64, 64, 27, 27, 27, 27, 8, 8, 8, 8, 1, 1, 1, 0, 0, 0, ============================================================
# Lists 6. List Transformations - Using List Comprehensions
# ============================================================

# Now let's practice using list comprehensions

# Let's use a list comprehension to check to build a new list with hat-trick games.

# This will create a new list, *not* a new iterable object

# The code 'hat_trick_list = [x for x in lst if x >= 3]' creates a new list assigned to hat_trick_list

# Printing hat_trick_list yields the following result:

# [4, 4, 4, 3, 3, 3, 3]

# We can use a list comprehension to triple these values as follows:
# The code 'tripled_list = [x * 3 for x in lst]' creates a new list assigned to tripled_list
# Printing tripled_list yields the following result:

# [12, 12, 12, 9, 9, 9, 9, 6, 6, 6, 6, 3, 3, 3, 0, 0, 0]

# Now let's treat these values as the radius of a circle,
#  and generate a new list where the values are equal to the area of a circle with these radii
# The code 'circle_area_list = [round(math.pi * (x * x), 2) for x in lst]' creates a new list, circle_area_list using list comprehension.


# Printing this list yields the following output:

# [50.27, 50.27, 50.27, 28.27, 28.27, 28.27, 28.27, 12.57, 12.57, 12.57, 12.57, 3.14, 3.14, 3.14, 0.0, 0.0, 0.0]

# (base) c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes>