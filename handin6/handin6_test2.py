import handin6
import timeit
from handin6 import wordfile_to_list


#5



fileone = "british-english"
filetwo = "american-english"

start_time = timeit.default_timer()

differences=handin6.wordfile_differences_binary_search(fileone, filetwo)

time_spent = timeit.default_timer() - start_time


print(time_spent)
   
print('done')


