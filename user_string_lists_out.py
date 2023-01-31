
# (base) C:\Users\timgo> cd  c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes\

# (base) c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes>
# (base) c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes>python user_string_lists.py
# ============================================================
# String Lists 1. Using Python Built-In Functions
# ============================================================

# In this section, we will use len(), set(), and zip()

# First, let's take a look at the values in our lists:
# ------------------------------------------------------------
# Title: First Names

# Contents:
# ['John', 'Adam', 'Barry', 'Clark', 'Daniel', 'Eric', 'Frank', 'Frank', 'Frank', 'Frank']
# ------------------------------------------------------------
# Title: Last Names

# Contents:
# ['Garfield', 'Harris', 'Johnson', 'Kraft', 'Langdon', 'Morris', "O'Dowd"]
# ------------------------------------------------------------
# Title: Positions

# Contents:
# ['left wing', 'right wing', 'goalie', 'center', 'defense']
# ------------------------------------------------------------
# Title: Ranks

# Contents:
# ['skater', 'skater', 'skater', 'skater', 'skater', 'skater', 'skater', 'skater', 'assistant captain', 'captain']
# ------------------------------------------------------------
# Title: Penalties

# Contents:
# ['high sticking', 'interference', 'cross checking', 'hooking', 'boarding', 'roughing']
# ------------------------------------------------------------

# Oh no! For some reason, 'Frank' is listed in our First Name list 4 times!

# We can remove these duplicates by creating a set from this list instead
# If we assign the return of set(firstNames) to a new variable and display its contents, we see the following result:
# ------------------------------------------------------------
# Title: First Name Set

# Contents:
# {'John', 'Frank', 'Barry', 'Clark', 'Daniel', 'Adam', 'Eric'}
# ------------------------------------------------------------

# Much better!  Now Frank is only listed one time.

# We may want to do a similar thing to our list that shows the different ranks a player can be

# This list contains 'skater' many more times than the other elements, as there are many more regular skaters on a hockey team than there are players who are captains or assistant captains

# These collections have different numbers of elements.  Let's take a look:
# ------------------------------------------------------------
# First Names List has a length of 10.
# First Names Set has a length of 7.
# Last Names has a length of 7.
# Positions has a length of 5.
# Ranks has a length of 10.
# Penalties has a length of 6.
# ------------------------------------------------------------

# Notice that the Set of first names has a lower number of elements than the list of first names

# Now let's zip the first name and last name lists into a list of tuples!
# ------------------------------------------------------------
# Title: Full Names

# Contents:
# <zip object at 0x000002A363D80F80>
# ------------------------------------------------------------
# Oops! The result of the zip(firstNames, lastNames) is a zip object - if we try to print this, we only print its memory address.

# Let's use the list() method to turn this iterator into a list first!

# Now we should be able to display its contents:
# ------------------------------------------------------------
# Title: Full Names

# Contents:
# [('John', 'Garfield'), ('Adam', 'Harris'), ('Barry', 'Johnson'), ('Clark', 'Kraft'), ('Daniel', 'Langdon'), ('Eric', 'Morris'), ('Frank', "O'Dowd")]
# ------------------------------------------------------------
# Excellent.  Now let's see how many tuples are in this list:
# Full Names has a length of 7.

# Remember that our list of first names contained many copies of 'Frank' and held 10 total elements
# We used this list, not the set that had removed elements, to create this new list of zipped tuples
# This new list of full name tuples only contains 7 elements.
# This is because the collection of least values determines the length of a collection created by the zip method
# Once all elements of the smallest collection have been zipped, the method terminates, and the collection is finalized


# ============================================================
# String Lists 2. Random Choice
# ============================================================

# Now let's use the random.choice() method and our custom built sentence_generator() method to simulate penalties being assessed against the hockey players described in our collections:
# ------------------------------------------------------------
# First penalty:
# Eric Morris a(n) captain playing center has been sent to the penalty box for 2 minutes for boarding.
# ------------------------------------------------------------
# Second penalty:
# Daniel Johnson a(n) skater playing right wing has been sent to the penalty box for 2 minutes for interference.
# ------------------------------------------------------------
# Third penalty:
# Barry Johnson a(n) skater playing defense has been sent to the penalty box for 2 minutes for boarding.
# ------------------------------------------------------------
# Fourth penalty:
# Barry Harris a(n) skater playing right wing has been sent to the penalty box for 2 minutes for cross checking.
# ------------------------------------------------------------
# Last penalty:
# Barry Langdon a(n) skater playing center has been sent to the penalty box for 2 minutes for interference.
# ------------------------------------------------------------


# ============================================================
# String Lists 3. Get Unique Words
# ============================================================

# Now we are going to read a text file and create a list out of the words contained within it.

# We will use text_zen_of_python.txt for this exercise

# Here is the unaltered text from the file:
# ------------------------------------------------------------

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# ------------------------------------------------------------

# We can assign the result of text.split() to create a list of ALL words (including duplicates)

# Here is the list of words from the file:
# ------------------------------------------------------------
# Title: List of Words

# Contents:
# ['Beautiful', 'is', 'better', 'than', 'ugly.', 'Explicit', 'is', 'better', 'than', 'implicit.', 'Simple', 'is', 'better', 'than', 'complex.', 'Complex', 'is', 'better', 'than', 'complicated.', 'Flat', 'is', 'better', 'than', 'nested.', 'Sparse', 'is', 'better', 'than', 'dense.', 'Readability', 'counts.', 'Special', 'cases', "aren't", 'special', 'enough', 'to', 'break', 'the', 'rules.', 'Although', 'practicality', 'beats', 'purity.', 'Errors', 'should', 'never', 'pass', 'silently.', 'Unless', 'explicitly', 'silenced.', 'In', 'the', 'face', 'of', 'ambiguity,', 'refuse', 'the', 'temptation', 'to', 'guess.', 'There', 'should', 'be', 'one--', 'and', 'preferably', 'only', 'one', '--obvious', 'way', 'to', 'do', 'it.', 'Although', 'that', 'way', 'may', 'not', 'be', 'obvious', 'at', 'first', 'unless', "you're", 'Dutch.', 'Now', 'is', 'better', 'than', 'never.', 'Although', 'never', 'is', 'often', 'better', 'than', '*right*', 'now.', 'If', 'the', 'implementation', 'is', 'hard', 'to', 'explain,', "it's", 'a', 'bad', 'idea.', 'If', 'the', 'implementation', 'is', 'easy', 'to', 'explain,', 'it', 'may', 'be', 'a', 'good', 'idea.', 'Namespaces', 'are', 'one', 'honking', 'great', 'idea', '--', "let's", 'do', 'more', 'of', 'those!']
# ------------------------------------------------------------

# ------------------------------------------------------------

# Like we did above when removing duplicates from the firstNames list, we can remove duplicates from this list using the set() function here too

# Here is the list of unique words from the file after assigning set(list_words) to a variable:
# ------------------------------------------------------------
# Title: List of Unique Words

# Contents:
# {'Namespaces', 'Simple', 'explicitly', 'do', 'never', 'more', 'refuse', 'not', 'practicality', 'unless', 'Now', "let's", 'silently.', '--obvious', "you're", 'be', 'one', 'that', 'pass', 'may', 'ambiguity,', 'never.', "it's", 'Sparse', 'guess.', 'enough', 'face', 'rules.', 'complicated.', 'of', 'ugly.', 'nested.', 'is', 'implementation', '*right*', 'good', 'If', 'beats', 'only', 'should', 'first', "aren't", 'now.', 'Although', 'one--', 'special', 'Readability', 'Explicit', 'at', 'cases', 'break', 'easy', 'In', 'Special', 'Beautiful', 'to', 'idea', 'silenced.', 'hard', 'great', 'preferably', 'temptation', 'dense.', 'purity.', 'the', 'There', 'are', 'it', 'those!', 'than', '--', 'it.', 'a', 'idea.', 'Unless', 'explain,', 'and', 'Complex', 'honking', 'Dutch.', 'bad', 'Errors', 'implicit.', 'complex.', 'often', 'way', 'counts.', 'Flat', 'better', 'obvious'}
# ------------------------------------------------------------

# ------------------------------------------------------------
# The length of the collection with ALL words is 137
# The length of the collection with unqiue words is 90
# When converting the list of all words to a set, 47 words were identified as duplicates and were removed

# (base) c:\Users\timgo\OneDrive\Desktop\School\Spring2023\Week3\datafun-03-datatypes>