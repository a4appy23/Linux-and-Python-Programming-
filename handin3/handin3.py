#1. Open the alice.txt file, and read the file into a list variable called lines where each element in the list corresponds to a line in the file.
file = open("alice.txt","r")
lines = file.readlines()
print(lines)

#2. Calculate and print how many lines there are in the file.
nlines=len(lines)
print(nlines)

#3. Print the 41st line.
print(lines[40])

#4. Count the number of words in the 43rd line and print the result.
line43 = lines[42].split(" ")
print(len(line43))

#5. Open a new file called "junk.txt", saving it to a variable called "junk_file". Use the writelines method to write the 9th to the 11th line (both included)  Remember to close the file when you are done.
junk_file= open("junk.txt","w")
junk_file.writelines(lines[8:11])
junk_file.close()
