#1. Create a module file called handin6.py containing a function called wordfile_to_list, which takes a single argument called filename. This function should read the file, and return a list with words. You can assume that each line in the file only contains a single word. Please remember to the remove newlines at the end of each line.
def wordfile_to_list(filename):
    """ an object of a list"""
    
    with open(filename) as file:
        text = file.readlines()

    file.close()

    list = []

    for line in text:
        list.append(line.strip())

    return list


#2. Add a function to the handin6 module called wordfile_differences_linearsearch, which takes two filenames as arguments, and calls wordfile_to_list to create a list for each of these files. The function should contain a loop that for each word in the first list looks through the second list to see if there is a match. It should return a list of words that are in the first file but not in the second file. 


def wordfile_differences_linear_search(fileone, filetwo):
    """T. The function returns a list of words that appears in the first file but not in the second one"""

    list1 = wordfile_to_list(fileone)
    list2 = wordfile_to_list(filetwo)
    difference = []

    for word1 in list1:
        if word1 not in list2:
            difference.append(word1)

    return difference



#4. Add this function to the handin6 module, and add another function called wordfile_differences_binarysearch. Again, this function should take two filename arguments, and return a list of the words that appear in the first file, but not in the second. This difference is that this time, you should call the binary_search function for each element in the outer loop.
def binary_search(sorted_list, element):
    """Search for element in list using binary search. Assumes sorted list"""

    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False



def wordfile_differences_binary_search(fileone, filetwo):
    """Turn two files into two lists and compares them line by line, using a binary search.
    The function returns a list of words that appears in the first file but not in the second one"""

    list1 = wordfile_to_list(fileone)
    list2 = wordfile_to_list(filetwo)
    difference = []

    for word1 in list1:
        if not binary_search(list2, word1):
            difference.append(word1)

    return difference



#6. Finally, we will test the speed of lookups in a Python dictionary. Create a function called wordfile_to_dict in the handin6 module. This function should be identical to wordfile_to_list, but save the results as keys in a dictionary rather than in a list (you can choose whatever you like for the values - for instance None).
def wordfile_to_dict(filename):
    """Receives a file as in input and turns every line into a key of a dictionary"""

    with open(filename) as file:
        text = file.readlines()

    file.close()

    dictionary = {}

    for line in text:
        dictionary[line.strip()] = None

    return dictionary



#7. Add a function to the handin6 module called wordfile_differences_dictsearch, which takes two filenames as arguments and calls wordfile_to_list on the first file and wordfile_to_dict on the second file. The function should contain a loop that for each word in the list looks in the dictionary to see if there is a match. It should return a list of words that are in the first file but not in the second file. 
def wordfile_differences_dict_search(fileone, filetwo):
    """ function returns a list of words that appears in the first file but not in the second one"""

    list1 = wordfile_to_list(fileone)
    dictionary = wordfile_to_dict(filetwo)
    difference = []

    for word1 in list1:
        if word1 not in dictionary:
            difference.append(word1)

    return difference


