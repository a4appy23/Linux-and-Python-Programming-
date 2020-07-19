#1. Find out how to get the sort command to sort by the second column in a file. Use this to write a command that finds the largest value in the second column of the experimental_results.txt file. Note that the command should just return a single number.
cat experimental_results.txt | sort -k 2 | cut -d ' ' -f 2 | tail -n 1


#2.Find documentation on the xargs and the du commands (either in the man pages or online). Using this information, construct a unix pipeline that finds all files under the /usr/share/dict directory containing the word "english" (using the find command), calculates the size of each of them, and then sorts the lines so that the largest files appear at the bottom (hint: you might need to use the -n 1 option for xargs). For those of you not using the virtual machine, you will only be able to test this locally if you download two files https://wouterboomsma.github.io/lpp2018/data/british-english and https://wouterboomsma.github.io/lpp2018/data/american-english and put them into your local /usr/share/dict directory. Alternatively, you can just test only on the server. 
find /usr/share/dict  -type f | xargs -n 1  du |grep "english"| sort -n

