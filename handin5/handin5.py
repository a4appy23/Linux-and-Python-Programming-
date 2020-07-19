
#1
def read_fasta(fastafile):
    '''Read a file from a FASTA format'''

    dictionary = {}
    with open(fastafile) as file:
        text = file.readlines()

    file.close()

    seq=''
    name=''

    #Create blocks of fasta text for each sequence, EXCEPT the last one
    for line in text:
        if line[0]=='>':
            dictionary[name] = seq
            name=line[1:].strip()
            seq=''

        else: seq = seq + line.strip()

    #Create the fasta text for the LAST sequence
    dictionary[name] = seq
    del dictionary['']
    return dictionary





#3. In the "handin5" module, create another function called "find_prot" that takes a dictionary as first argument, and as second argument takes a protein name (a string). The function should use the provided dictionary to lookup and return the sequence corresponding to the provided name .  If the name is not present in the dictionary, the function should print an error message and return None. The error message should be "Error: protein name NAME not found", where NAME is the protein name you are searching for. Make sure to include a docstring.
def find_prot(dict, protname):
    '''sequence in the dictionary,  protein name'''

    if protname in dict:
        return dict[protname]
    else:
        return print("Error: protein name %s not found" % (protname))
        return None


#6. In the "handin5" module, create a function called "find_prot2" that takes a dictionary and regular expression (as a string), and returns a list of all of the *keys* in the dictionary that the pattern matches. Make sure to include a docstring.
import re

def find_prot2(dict, regex):
    '''Look in the dictionary in the form of regular expression y'''

    keys = []
    pattern = re.compile(regex)

    for item in dict:
        match = pattern.match(item)
        if match:
            keys.append(item)

    return keys


