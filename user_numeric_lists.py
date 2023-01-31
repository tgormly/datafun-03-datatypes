"""
Tim Gormly
1/28/23

In this file, we will test built-in list methods on lists with numerical data
"""



divider = "============================================================"

# import modules
import statistics
import random
import math

# specify random seed to keep results consistent
random.seed(1)

print(divider)
print("Lists 1. List Statistics")
print(divider)

# create a list of more than 20 numbers
print("A for loop is used to create 'list1', a list of integers with random numbers\n")

list1 = [random.randint(1,20) for x in range(30)]
# print(list1)

print("'listx' is created with values 1-10 using a range object\n")
listx = [x for x in range(1,11)]
# print(listx)

print("'listy' is created by hand to simulate 10 digits with somewhat linear progression\n")
listy = [3, 3, 6, 9, 12, 14, 14, 19, 25, 26]
# print(listy)

print("\n~~1.Calculate the mean, median, and mode of list1(hint: import statistics module)~~\n")

list1_mean = statistics.mean(list1)
list1_median = statistics.median(list1)
list1_mode = statistics.mode(list1)

print(f"Mean = {list1_mean:.2f}")
print(f"Median = {list1_median:.2f}")
print(f"Mode = {list1_mode:.2f}")

print("\n~~2. Caclulate the standard deviation and variance of list1~~\n")

list1_standard_deviation = statistics.stdev(list1)
list1_variance = statistics.variance(list1)

print(f"Standard Deviation = {list1_standard_deviation:.2f}")
print(f"Variance = {list1_variance:.2f}")

################################################################################################

print(divider)
print("Lists 2. Lists - Correlation and Prediction")
print(divider)

print("\n~~1. Calculate the correlation between listx and listy~~\n")

xy_correlation = statistics.correlation(listx, listy)

print(f"statistics.correlation(listx, listy) = {xy_correlation:.2f} (rounded to two decimals)")

print("\n~~2. Calculate the slope and the intercept of the best fit line~~\n")

print("slope, intercept = statistics.linear_regression(listx, listy) is used to accomplish this")
slope, intercept = statistics.linear_regression(listx, listy)

print("\n~~3. Set a future time = 15~~\n")

print("future_x = 15 is used to accomplish this")
future_x = 15

print("\n~~4. Predict the y value at a future time y = mx + b where m is the slop and b is the y intercept~~\n")

y_future_value = (slope * future_x) + intercept

print(f"The value of y at x = 15 is: {y_future_value:.2f} (rounded to two decimals)") 
print(f"or without rounding, it is: {y_future_value}")

print(divider)
print("Lists 3. Using Python Built-in Functions")
print(divider)

# min()
print(f"\nThe minimum value in list1 is: {min(list1)}")

# max()
print(f"\nThe maximum value in list1 is: {max(list1)}")

# len()
print(f"\nThe length of list1 is: {len(list1)}")

# sum()
print(f"\nThe sum of all values in list1 is: {sum(list1)}")

# average (hint use two values already calculated
print(f"\nThe average of all values in list1 is: {(sum(list1) / len(list1))}")

# set()
print(f"\nUsing set() to remove duplicates, list1 becomes:\n{set(list1)}")

# sorted()
print(f"\nsorted(list1):\n{sorted(list1)}")

# sorted(), using reverse=True
print(f"\nsorted(list1, reverse=True):\n{sorted(list1, reverse=True)}")


print(divider)
print("Lists 4.  List Methods")
print(divider)

print("Now we will use list methods on a list numbers equal to the number of goals scored by a hockey player in a given game")
lst = [1,4,3,2,4,3,3,2,0,0,0,1,2,4,3]

print(f"Here is the list we just made:\n{lst}")

# append() a single value to the list
print("\nFirst we will append to add value because the player played a new game\nThe player had an amazing night and scored 6 goals!\n")

lst.append(6)

print(f"Here is the list after running lst.append(6):\n{lst}")

print('\nNotice how the new value is added to the end of the list')

# extend() the list with a new list you pass in
print('\nNow we will use lst.extend to add another list to the end of lst\n')

lst2 = [0, 1 ,2]
print(f'The new list we are adding is: {lst}\n')

lst.extend(lst2)
print(f'When we run lst.extend(lst2), the original list becomes:\n\n{lst}')

# insert() at an index, insert a value
print('Next we will use insert() to add a new value at a specific index\n')
print("We'll add 3 to index 0\n")

lst.insert(0, 3)

print(f'After running lst.insert(0, 3), the list becomes:\n\n{lst}')

# remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
print(f'\nNow we will remove the number 5 from the list')

lst.remove(3)

print(f'After running lst.remove(5), the list becomes:\n\n{lst}\n\nNotice that only the first instance of the value 3 has been removed - all other instances of 3 remain')

# count(2) count how many times 2 appears in your list (if it doesn't, change  2 to a value in your list)
print('\nNow, let\'s see how many times our player scored 2 goals using the lst.count(2)')

print(f'\nThe player scored 2 goals in one game {lst.count(2)} time(s)')

# sort()
print('\nLet\'s now use the sort() method to place the values of the list in ascending order')

lst.sort()

print(f'\nThis method sorts the list in place, so the actual values in the list have been re-arranged')
print(f'\nNow the list reads as:\n\n{lst}')

# sort(), with reverse=True to get them in descending order
print(f'\nLet\'s reverse the order of the list by adding a reverse=True parameter to the sort method')

lst.sort(reverse=True)

print(f'\nThis method still updates the list in place, truly re-arranging the values.\nSee what happens when we print the list:\n')
print(lst)

# copy()
print(f'\nWe can use "lst.copy()" to create a new copy of our list')
lst3 = lst.copy()

print(f'See what happens after we assign lst.copy() to the variable lst3 and print it:\n')
print(lst3)

# pop() the first item off the top of the list/stack
print("\nThe pop() method can be used to remove an item from the list.")
print("\nWhen we run lst.pop(0), the value at index 0 will be removed:\n")

lst.pop(0)

print(lst)

# pop() the last time off the bottom of the list/stack
print("\nIf we don't provide an argument for the pop() method, the very last item will be removed instead")
lst.pop()

print(f"\nHere is the list after running lst.pop():\n\n{lst}")

print(divider)
print("Lists 5. List Transformations - Using filter() and map()")
print(divider)

import math

# Use the built in filter() function to keep x such that x is less than 4 (or some other cutoff), or keep the even ones, whatever.
print("\nNow we will use the filter() function to filter our list")
# define the method used in the filter:
def hat_trick(variable):
    if(variable >= 3):
        return True
    else:
        return False

hat_trick_list = filter(hat_trick, lst)

print(f"If we run hat_trick_list = filter(hat_trick, lst), the result will be hat_trick_list being an iterable object\n\nIf we try to print it, we only print its location ID")
print(f"\nprint(hat_trick_list) outputs: {hat_trick_list}")

print("\n\nInstead, we can iterate over it and print each item using a for loop:\n")

for i in hat_trick_list:
    print(i, end=", ")

print("\nWe can achieve the same result using a lambda function, also known as an anonymous function, in place of a pre-defined function.")

print("\nThe following code produces the same iterable object:\n\nhat_trick_list = [filter(lambda x: x >= 3, lst)]")

hat_trick_list = filter(lambda x: x >= 3, lst)

for i in hat_trick_list:
    print(i, end=", ")

print("\nWe will use lambda expressions for the remainder of this exercise")

# Use the built in map() function to map each x to cuberoot of x (hint: use math module)

print("\nNow we will use the map function for a few things")

print("\nFirst, we will find the cuberoot of each value")

cube_root_list = map(lambda x: math.pow(x, (1/3)), lst)

print("\nNotice that, like filter, this creates an iterable object - if we attempt to print it, we will only print its memory address")
print(f"\nprint(cube_root_list) outputs: {print(cube_root_list)}")
print("Using a for loop, we can print each value like so:\n")

for i in cube_root_list:
    print(f"{i:.2f}", end=', ')

# Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. Hint: Volume = side * side * side
print(f"\nNow let's try to cube each value in our original list")

cubed_list = map(lambda x: x ** 3, lst)

print("\nHere is the output of iterating over our new map object with cubed values:\n")

for i in cubed_list:
    print(f"{i}", end=", ")


print(divider)
print("Lists 6. List Transformations - Using List Comprehensions")
print(divider)

print("\nNow let's practice using list comprehensions")

# Comprehension means to "grasp together" 
# Or to use one list to "completely describe" a new list

# Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff. 

print("\nLet's use a list comprehension to check to build a new list with hat-trick games.\n\nThis will create a new list, *not* a new iterable object")

hat_trick_list = [x for x in lst if x >= 3]

print(f"\nThe code 'hat_trick_list = [x for x in lst if x >= 3]' creates a new list assigned to hat_trick_list")
print(f"\nPrinting hat_trick_list yields the following result:\n\n{hat_trick_list}")

# Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 

print("\nWe can use a list comprehension to triple these values as follows:")

tripled_list = [x * 3 for x in lst]

print(f"The code 'tripled_list = [x * 3 for x in lst]' creates a new list assigned to tripled_list")

print(f"Printing tripled_list yields the following result:\n\n{tripled_list}")

# Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.

print("\nNow let's treat these values as the radius of a circle,\n and generate a new list where the values are equal to the area of a circle with these radii")

circle_area_list = [round(math.pi * (x * x), 2) for x in lst]

print("The code 'circle_area_list = [round(math.pi * (x * x), 2) for x in lst]' creates a new list, circle_area_list using list comprehension.\n\n")

print(f"Printing this list yields the following output:\n\n{circle_area_list}")