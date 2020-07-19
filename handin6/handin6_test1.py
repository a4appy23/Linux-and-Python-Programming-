import handin6
import timeit
from handin6 import wordfile_to_list
#3In the file called handin6_test1.py, call the wordfile_differences_linear_search on the input files, using british-english as file1 and american-english as file2 (it is ok to test it on the test files first, but please switch to the full files before submitting), and saves the result in a variable called differences



fileone = "british-english"
filetwo = "american-english"

start_time = timeit.default_timer()

differences=handin6. wordfile_differences_linear_search(fileone, filetwo)

time_spent = timeit.default_timer() - start_time



   
print('done')
print(time_spent)











