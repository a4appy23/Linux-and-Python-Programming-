#1. Use bzip2 to compress the file, but in a way that preserves the original.
bzip2 -k experimental_results.txt 

#2. Use ls to output how large the two files are.
ls -l experimental_results.txt* | tr -s " " | cut -d " " -f 5

#3. The tr command has the functionality to recognise digits. Use this to replace all the number in the original file with "0.000000".
cat experimental_results.txt | tr [:digit:] "0" > experimental_results_zeros.txt

#4. Check that the "experimental_results_zeros.txt" file has the same size as the "experimental_results.txt" file, using the same output format as in question 2.
ls -l experimental_results.txt experimental_results_zeros.txt | tr -s " " | cut -d " " -f 5

#5. Use bzip2 to compress the "experimental_results_zeros.txt" file (again keeping the original), and print out the sizes of the original and compressed files, in the same output format as in question 2.
bzip2 -k experimental_results_zeros.txt
ls -l experimental_results_zeros.txt experimental_results_zeros.txt.bz2 | tr -s " " | cut -f 5 -d " "

#6. Try to explain why there is a difference - use echo and tee to write the explanation both to a file called "explanation.txt" and to stdout.
echo " the Burrow-Wheeler transformation uses the permutation of the order of the digits. here,  the digits are the same (0), and its  easier to encrypt" | tee explanation.txt

