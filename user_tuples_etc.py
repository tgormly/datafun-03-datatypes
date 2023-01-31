"""
Tim Gormly
1/30/23
In this file, we will explore tuples, sets, and dictionaries.  
"""


divider = "============================================================"
small_divider = "------------------------------------------------------------" 

def total_points_and_goal_percentage(goals, assists):
    '''This function receives goals and assists made by a player and returns a tuple that 
    contains the players' total points (in hockey, each goal AND assist count as 1 point)
    as well as the players' goal % - the percentage of their points that comes from their
    goals scored
    
    example function call:
    total_points_and_goal_percentage(100, 100)

    returns a tuple containing (200, 0.5)
    '''
    # calculate the players' total points and percent of points from goals
    try:
        total_points = goals + assists
        goal_percent = goals / total_points

    except Exception as e:
        print(f"Error: {e}")
        return None
    
    #check for valid results - if the result of this function is illogical, present a message to the user and return None
    if goal_percent > 1 or goal_percent < 0:
        print(f"A player's goals cannot make up more than 100% or less than 0% of their total points\nThe function just calculated a goal_percentage of {goal_percent * 100}%\nPlease review your data and try again.")
        return None

    # if no exception has been thrown, and the results are logical, return the computed values as a tuple
    return total_points, goal_percent


if __name__ == "__main__":

    print(divider)
    print("First, we are going to explore tuples")
    print(divider)

    print("\nFirst, let's create a couple of tuples.  One will contain biographical data for a hockey player, and the second will contain their gameplay statistics")

    headerBio = ("FirstName", "LastName", "Age", "Hometown")
    player1Bio = ("Frank", "Jones", "28", "Manitoba")

    headerStats = ("Goals", "Assists", "Hits", "Penalty Minutes")
    player1Stats = (20, 33, 40, 16)

    print("Let's take a look at what we've created.  We've also made a tuple to represent a header for each of these other tuples.  In a spreadsheet, these headers would be the top row that names the columns and describes the data held in that column")
    
    print(small_divider)
    print(f"\n{headerBio = }\n{player1Bio = }")
    print(small_divider)
    print(f"{headerStats = }\n{player1Stats = }")
    print(small_divider)

    print("\nOK, that looks good, but wouldn't it make more sense to contain both biographical and statistical data all in one row?")
    print("\nWe can do this using concatination:")

    headerPlayer = headerBio + headerStats
    player1 = player1Bio + player1Stats

    print(small_divider)
    print(f"\n{headerPlayer = }\n{player1 = }")
    print(small_divider)

    print("\nThat looks much nicer!")

    print("Similar to concatenation, we could also use multiplication with a single tuple to have it repeat itself several times.")
    print("The tuples we've created already can demonstrate this:")

    print(small_divider)
    print(f"{player1 * 3 = }")
    print(small_divider)

    print("This is a bit odd with this particular tuple, but it illustrates the point.")

    print(small_divider)

    print("\nTuples also allow for membership testing.  Observe the following:")
    
    print(small_divider)
    print(f"{'Frank' in player1 = }")
    print(f"{'James' in player1 = }")
    print(f"\nAs a reminder, here is what is contained in player1:\n\n{player1}")
    print(small_divider)

    print("\nTuples are ordered, and support indexing.  Observe the following:")
    
    print(small_divider)
    print(f"{player1[0] = }")
    print(f"{player1[5] = }")
    print(f"{player1[-1] = }")
    print(f"{player1[4:] = }")
    print(f"{player1[:4] = }")
    print(f"{player1[:4:2] = }")
    print(small_divider)

    print("Tuples can be returned from functions as well.")
    print(f"\nThe following function, total_points_and_goal_percentage() will receive a players' goals and assists and then return a tuple containing the total of their goals and assists (also known as their points) as well as a float that represents the percentage of the players points that come from goals")
    print(f"\nWe will attempt to call this function using a few different parameters:")

    print(small_divider)
    print(f"{total_points_and_goal_percentage(100, 100) = }")
    print(f"{total_points_and_goal_percentage(100, 0) = }")
    print(f"{total_points_and_goal_percentage(0, 100) = }")
    print(f"{total_points_and_goal_percentage(-1, 5) = }")
    print(small_divider)

    print()
    print()
    print(divider)
    print("Next, we will look at a few quick things with sets")
    print(divider)

    print("\nFirst, let's create a few sets.\n\nLet's look at a few cities with major league (NHL) teams, and a few cities with minor league (AHL) teams:")

    major_league_cities = {"St Louis", "Chicago", "Calgary", "Edmonton", "Dallas", "Seattle", "Las Vegas"}
    minor_league_cities = {"Chicago", "Cleveland", "Calgary", "Coachella Valley", "Manitoba"}

    print(small_divider)
    print(f"{major_league_cities = }")
    print(f"{minor_league_cities = }")
    print(small_divider)

    print("\nNotice that there are cities that are unique to each set, as well as some cities that appear in both sets")
    print("\nIf we think about these two sets as two circles in a Venn Diagram, we can explore some interesting things:")

    print(small_divider)
    print("Set Union:")
    print(f"The union of these two sets is: \n{major_league_cities | minor_league_cities = }")
    print(f"\nThe result of this union is a new set that contains all unique values found between the two sets")
    print("\nNote: the result of this union is still a set, so no duplicate values are present in the result set, even though duplicate values are present between the two sets themselves")
    print(small_divider)
    
    print(small_divider)
    print("Set Intersection")
    print(f"The intersection of these two sets is: \n{major_league_cities & minor_league_cities = }")
    print(f"\nThe result of this intersection is a new set that contains all values that are found within BOTH sets.\nItems that are in one set but not the other are discarded")
    print(small_divider)

    print(small_divider)
    print("Set Difference")
    print(f"The difference of the major league city set by subtracting the minor league set: \n{major_league_cities - minor_league_cities = }")
    print(f"The difference of the minor league city set by subtracting the major league set: \n{minor_league_cities - major_league_cities = }")
    print(f"\nThe result of a set difference is a new set that contains values present in the first set, but NO values in the second set.\nItems that are in one set but not the other are discarded")
    print(small_divider)

    print("\nAs we have seen in these examples, a set will never contain duplicate values - they are always discarded so that only unique values remain")
    print("\nThis feature of sets can be very useful in reducing a list that contains many duplicate values down to its unique values")
    print("\nObserve the following example:")

    list_with_duplicates = ["puck", "stick", "ice", "boards", "glass"] * 3

    list_with_duplicates.sort()

    print(small_divider)
    print("Here is a list with many duplicate values:")
    print(f"\n{list_with_duplicates = }")
    print(small_divider)
    print(f"\nObserve what happens to the list with it is passed into the set() method:")
    print(f"\n{set(list_with_duplicates) = }")
    print("\nAll duplicate values have been removed!")
    print(small_divider)

    print()
    print()
    print(divider)
    print("Lastly, let's look at Dictionaries")
    print(divider)

    print("\nDictionaries are collections made of key value pairs.")
    print("\nTo illustrate this, we will read a file and use a dictionary comprehension so that each word in the file is a key, and each value is equal to the total number of times that word, or key, appears in the file:\n")

    # open a file and 
    with open("text_names_in.txt") as file_object:
        word_list = file_object.read().split()
    
        #variable.........|key.|.value...............|.for every word found when iterating over the word list
        word_count_dict = {word: word_list.count(word) for word in word_list}

        print(word_count_dict)