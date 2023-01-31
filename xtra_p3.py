"""
Tim Gormly
1/30/2023

In this program, we are going to use collections to analyze two plays by Shakespeare: Hamlet, and Julius Ceasar

In particular, this program will count the number of times all words appear in these two plays.  In an attempt to
compare only the "important" words in these two plays, we will only really be reviewing words that are longer than 10 characters.

So, a list will be made from each play that contains all words that are at least 10 characters in length

Then, sets will be built from these lists, and all all duplicate words in these lists will be removed

We will then check the length of each list, as well as the intersection of these sets (the words shared by these two lists)

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# read from first file and get a list of words

def retrieve_word_list_from_file(filepath):
    '''This function will receive a file path.  The method will load this text file and then
    load all words into a list that is then returned.  The words will be separated by whitespace
    
    Files are closed automatically at the end of this function call'''
    try:
        with open(f"{filepath}", "r") as f:
            text = f.read()
            wordlist = text.split()
            return wordlist
    except Exception as e:
        print(f"ERROR: {e}")
        return None

    return wordlist

def filter_list_based_on_string_length(iterable, maxlength):
    '''This function will receive an iterable and a maximum length
    
    The function then filters the list provided so that a new list is created that includes only strings with legnths greater than the maximum length provided
    '''
    try:
        filtered_list = [word for word in iterable if len(word) > maxlength]
    except Exception as e:
        print(f"ERROR: {e}")
        return None

    return filtered_list

if __name__ == "__main__":

    # read from first file and get a list of words
    wordlist1 = retrieve_word_list_from_file("text_hamlet.txt")

    # read from second file and get a list of words
    wordlist2 = retrieve_word_list_from_file("text_juliuscaesar.txt")

    # test prints to confirm lists have been populated
    # print(f"{wordlist1[:10]}")
    # print(f"{wordlist2[:10]}")

    # Done with files - let the files close and the work begin
    # file closure occurs automatically at end of function call

    # Remove duplicates by creating two sorted sets
    # hint: use sorted() to sort the list
    # hint: use set() to remove duplicates
    # name them wordset1 and wordset2
    # this step is somewhat unnecessary - we could create a set after filtering the list for words with lengths greater than 10 characters.
    # I'm not sure which approach would be more optimized.
    # if we create sets after filtering, we skip these set() calls, but the list comprehension we use next will have a much larger iterable to iterate over
    wordset1 = set(wordlist1)  
    wordset2 = set(wordlist2)  


    # initialize a variable maxlen = 10
    maxlen = 10

    # use a list comprension to get a list of words longer than 10
    # for word in wordset1
    # That is:
    # in a list (e.g. square brackets)
    # say "[Give me word (for each word in wordset1)
    #      if len(word) is greater than maxlen]"

    longwordlist1 = filter_list_based_on_string_length(wordset1, maxlen)
    longwordlist2 = filter_list_based_on_string_length(wordset2, maxlen)

    # then convert the list to a set to we can take the intersection
    # hint: use set()
    # name them longwordset1 and longwordset2

    longwordset1 = set(longwordlist1)  
    longwordset2 = set(longwordlist2)  

    # find the intersection of the two sets
    # that is, the words in both longwordset1 1 & longwordset2
    # name this variable longwords
    longwords = longwordset1 & longwordset2

    # print the length of the sets and the list
    print(len(longwordset1))
    print(len(longwordset2))
    print(len(longwords))
    print()
    print(f"{sorted(longwords) = }")
    print()

    # check your work
    print("TESTING...if nothing prints before the testing is done, you passed!")
    doctest.testmod()
    print("TESTING DONE")
