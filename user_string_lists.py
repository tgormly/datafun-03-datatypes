"""
Tim Gomrly
1/29/23
In this file, we will use various list methods and other pre-built python methods to review string lists, text files, etc
"""

# imports first
import random

divider = "============================================================"
small_divider = "------------------------------------------------------------" 
# reusable functions next

def show_title_and_contents(title, contents):
    '''This function will take a title of a collection (hard-coded at function call), and a collection,
    it will then print a formatted summary of the collection to the console'''
    
    print(f"Title: {title}")
    print(f"\nContents:")
    print(contents)
    print(small_divider)

def show_length_of_collection(title, collection):
    '''This function will take a title of a collection (hard-coded at function call), and a collection,
    It will then print a formatted message showing the length of the collection to the console'''
    
    print(f"{title} has a length of {len(collection)}.")

def sentence_generator(fullNames, ranks, positions, penatlies):
    '''This function will take several collections as parameters.  It will then make a random selection
    from each collection to create a message that will be printed to the console
    
    These messages will simulate a referee's announcement of a penalty being assessed by the player
    
    Example output might look like:

    Adam O'Dowd a assistant captain playing goalie has been sent to the penalty box for 2 minutes for interference.
    '''
    print(f"{random.choice(fullNames)[0]} {random.choice(fullNames)[1]} a(n) {random.choice(ranks)} playing {random.choice(positions)} has been sent to the penalty box for 2 minutes for {random.choice(penalties)}.")


# Lists used in file:

firstNames = ["John", "Adam", "Barry", "Clark", "Daniel", "Eric", "Frank", "Frank", "Frank", "Frank"]

lastNames = ["Garfield", "Harris", "Johnson", "Kraft", "Langdon", "Morris", "O'Dowd"]

positions = ["left wing", "right wing", "goalie", "center", "defense"]

ranks = ["skater", "skater","skater","skater","skater","skater","skater","skater", "assistant captain", "captain"] # skater is listed many more times than the other ranks, as there are many more skaters than assistant captains or captains

penalties = ["high sticking", "interference", "cross checking", "hooking", "boarding", "roughing"]

# call functions and execute code
if __name__ == "__main__":

    print(divider)
    print("String Lists 1. Using Python Built-In Functions")
    print(divider)

    print("\nIn this section, we will use len(), set(), and zip()")

    print("\nFirst, let's take a look at the values in our lists:")
    print(small_divider)
    show_title_and_contents("First Names", firstNames)
    show_title_and_contents("Last Names", lastNames)
    show_title_and_contents("Positions", positions)
    show_title_and_contents("Ranks", ranks)
    show_title_and_contents("Penalties", penalties)

    print("\nOh no! For some reason, 'Frank' is listed in our First Name list 4 times!")
    print("\nWe can remove these duplicates by creating a set from this list instead")

    print(f"If we assign the return of set(firstNames) to a new variable and display its contents, we see the following result:")

    firstNamesSet = set(firstNames)

    print(small_divider)
    show_title_and_contents("First Name Set", firstNamesSet)

    print("\nMuch better!  Now Frank is only listed one time.")

    print("\nWe may want to do a similar thing to our list that shows the different ranks a player can be")
    print("\nThis list contains 'skater' many more times than the other elements, as there are many more regular skaters on a hockey team than there are players who are captains or assistant captains")

    print("\nThese collections have different numbers of elements.  Let's take a look:")
    print(small_divider)
    show_length_of_collection("First Names List", firstNames)
    show_length_of_collection("First Names Set", firstNamesSet)
    show_length_of_collection("Last Names", lastNames)
    show_length_of_collection("Positions", positions)
    show_length_of_collection("Ranks", ranks)
    show_length_of_collection("Penalties", penalties)
    print(small_divider)

    print("\nNotice that the Set of first names has a lower number of elements than the list of first names")
    
    print("\nNow let's zip the first name and last name lists into a list of tuples!")

    fullNames = zip(firstNames, lastNames)

    print(small_divider)
    show_title_and_contents("Full Names", fullNames)

    print("Oops! The result of the zip(firstNames, lastNames) is a zip object - if we try to print this, we only print its memory address.\n\nLet's use the list() method to turn this iterator into a list first!")

    fullNames = list(fullNames)

    print("\nNow we should be able to display its contents:")
    print(small_divider)
    show_title_and_contents("Full Names", fullNames)

    print("Excellent.  Now let's see how many tuples are in this list:")
    show_length_of_collection("Full Names", fullNames)

    print("\nRemember that our list of first names contained many copies of 'Frank' and held 10 total elements")
    print("We used this list, not the set that had removed elements, to create this new list of zipped tuples")
    print("This new list of full name tuples only contains 7 elements.")
    print("This is because the collection of least values determines the length of a collection created by the zip method")
    print("Once all elements of the smallest collection have been zipped, the method terminates, and the collection is finalized")

########################################################################################################################################

    print()
    print()
    print(divider)
    print("String Lists 2. Random Choice")
    print(divider)

    print("\nNow let's use the random.choice() method and our custom built sentence_generator() method to simulate penalties being assessed against the hockey players described in our collections:")
    print(small_divider)
    print("First penalty:")
    sentence_generator(fullNames, ranks, positions, penalties)
    
    print(small_divider)
    print("Second penalty:")
    sentence_generator(fullNames, ranks, positions, penalties)
    
    print(small_divider)
    print("Third penalty:")
    sentence_generator(fullNames, ranks, positions, penalties)
    
    print(small_divider)
    print("Fourth penalty:")
    sentence_generator(fullNames, ranks, positions, penalties)
    
    print(small_divider)
    print("Last penalty:")
    sentence_generator(fullNames, ranks, positions, penalties)
    
    print(small_divider)

########################################################################################################################################
    print()
    print()
    print(divider)
    print("String Lists 3. Get Unique Words")
    print(divider)

    print("\nNow we are going to read a text file and create a list out of the words contained within it.")
    print("\nWe will use text_zen_of_python.txt for this exercise")

    with open("text_zen_of_python.txt", "r") as fileObject:
        text = fileObject.read()

        print("\nHere is the unaltered text from the file:")
        print(f"{small_divider}\n")
        print(text)
        print(f"\n{small_divider}")

        print("\nWe can assign the result of text.split() to create a list of ALL words (including duplicates)")
        list_words = text.split()  # split on whitespace

        print("\nHere is the list of words from the file:")
        print(small_divider)
        show_title_and_contents("List of Words", list_words)
        print(f"\n{small_divider}")        

        print("\nLike we did above when removing duplicates from the firstNames list, we can remove duplicates from this list using the set() function here too")
        unique_words = set(list_words)  # remove duplicates

        print("\nHere is the list of unique words from the file after assigning set(list_words) to a variable:")
        print(small_divider)
        show_title_and_contents("List of Unique Words", unique_words)
        print(f"\n{small_divider}")   

        print(f"The length of the collection with ALL words is {len(list_words)}")
        print(f"The length of the collection with unqiue words is {len(unique_words)}")
        print(f"When converting the list of all words to a set, {len(list_words) - len(unique_words)} words were identified as duplicates and were removed")



