#1. Use the time command to measure the execution time of handin6_test1.py
time python handin6_test1.py




#2. Use the time command to measure the execution time of handin6_test2.py
time python handin6_test2.py



#3. Use the time command to measure the execution time of handin6_test3.py
time python handin6_test3.py



#4. The diff command can be used to solve the same task as our Python script above. Write a command that does this. The command should just print out the number of differences (i.e. the number of words in file1 that do not occur in file2).
diff british-english american-english | grep -e '<' | wc -l



#5. Repeat the previous question, but now use the time command to measure its performance.
time diff british-english american-english | grep -e '<' | wc -l



