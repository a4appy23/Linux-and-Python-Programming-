#1. Create a directory called handin1 in your current directory.
mkdir handin1


#2. Create a directory called test1.
cd handin1
mkdir test1


#3. Use a Unix command to download the following file   m_scrambled.txt.
cd test1
wget http://people.binf.ku.dk/wb/data/m_scrambled.txt


#4. Make a copy of the test1 directory, called test2.
cd ..
cp -r test1 test2


#5. Go to the handin1 directory, and use the find command to output all files and directories under this directory.
cd .
find 

#6. Remove the test2 directory.
rm -r test2


#7. Use the cat command to take a look at the m_scrambled.txt you just downloaded.
cd test1
cat m_scrambled.txt


#8. Find a way to "unscramble" the image into a new file called m.txt (in the test1 directory).
cd ~/lpp2019/handin1-a4appy23/handin1/test1
sort -n m_scrambled.txt > m.txt


#9. Find a way to download, unscramble and save in a single command. Again, save it to a file called m.txt in the test1 directory.
wget http://people.binf.ku.dk/wb/data/m_scrambled.txt | sort -n m_scrambled.txt > m.txt


#10. Delete the handin1 directory and all directories below it
cd ..
cd ..
rm -rf handin1

