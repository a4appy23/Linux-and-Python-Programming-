# Handin 5

<table>
  <tr>
    <td>Due date</td>
    <td>Tuesday, Oct 8 </td>
  </tr>
  <tr>
    <td>Format</td>
    <td>Unix part: Put the relevant commands into the handin5.sh file. The individual exercises should be separated by empty lines (see the "Github, git and the weekly hand-ins" page on Absalon for an example).
Python part: Put your Python code into the <code>handin5.py</code> and <code>handin5_test.py</code> files (see which code to put in which file below). 
When you are ready to submit, use the <code>git commit -a -m "Submission 1"</code> command, where you replace <code>"Submission 1"</code> with a brief message explaining how this version of the files differs from the last, (e.g. <code>"Initial submission"</code>, <code>"Fixed bug in subquestion 1"</code>, etc), followed by <code>git push</code> </td>
  </tr>
  <tr>
    <td>Setup</td>
    <td><strong>Please make sure that your name and email address have been set up correctly</strong> for <code>git</code>. This is very important, since otherwise you will not receive emails about the correctness of your code (and we cannot see who is who). See the <a href="https://absalon.ku.dk/courses/35880/pages/github-git-and-the-weekly-hand-ins?module_item_id=801269">Github, git and the weekly hand-ins</a> page for details.
  </tr> 
  <tr>
    <td>Other comments</td>
    <td>As usual, the hand-in covers the topics covered in this week of the course. This means that there might be a few things that you won't be able to solve until after the Friday lecture. </td>
  </tr>
</table>


## Unix part

We have uploaded two versions of the british-english dictionary.
They are located at:

http://wouterboomsma.github.io/lpp2019/data/british-english

and

http://wouterboomsma.github.io/lpp2019/data/british-english-subset

1. Download both files to your current directory using appropriate unix commands.
2. In the <code>_subset</code> file, I have excluded words starting with specific letters in the alphabet. Write a command that prints out exactly which letters I ommitted from subset, one letter on each line, and each letter occurring only once. Hint: the <code>diff</code> command will list the differences, and the <code>-b</code> option of the cut command will give you a specific character in each line.
3. Find a way to reproduce the <code>british-english-subset</code> file from the original <code>british-english</code> file, i.e., write a Unix command involving <code>grep</code> that takes the original <code>british-english</code> file and produces the <code>british-english-subset</code> file. Note that the <code>grep</code> command understands regular expressions (which means, for instance, that you can match something occurring at the beginning of a line). Save the output produced by the command to a file called <code>british-english-subset2</code>.


## Python part

For this exercise, we are going to experiment with some real data. Your repository includes the following file:

<pre><code>Ecoli.prot.fasta</code></pre>

which contains amino acid sequences for all known proteins in the E. coli organism. It is in the so-called Fasta format, which means that for every protein, we first have a line starting with <code>&gt;</code> containing the name, e.g.:

<pre><code>&gt;CCMA_ECOLI</code></pre>

and then some lines containing the sequence of amino acids, e.g.:

<pre><code>
MGMLEARELLCERDERTLFSGLSFTLNAGEWVQITGSNGAGKTTLLRLLTGLSRPDAGEVLWQGQPLHQV
RDSYHQNLLWIGHQPGIKTRLTALENLHFYHRDGDTAQCLEALAQAGLAGFEDIPVNQLSAGQQRRVALA
RLWLTRATLWILDEPFTAIDVNGVDRLTQRMAQHTEQGGIVILTTHQPLNVAESKIRRISLTQTRAA</code></pre>

1. Create a module called <code>handin5</code>, and inside that module define a function called <code>read_fasta</code>.  This function should take one argument: a string that is a filename (or full path) to a fasta file.  This function should open and read the supplied fasta file, then create and return a dictionary, where the keys are the names of the proteins (without the <code>&gt;</code> character) and the sequences are the values. Make sure to add a docstring to your function. <br>Hint1: remember to remove the newline characters at the end of each line. <br>Hint2: Think of the exercise like this: for each line, you should check whether the line is a header or not. If it is a header, it should be added to the dictionary as a key - if it is not, it should be added to the dictionary as a sequence - adding to whatever sequence was already there.

2. Create a new file, called <code>handin5_test.py</code> where you import the <code>handin5</code> module. Then call the <code>read_fasta</code> function and save the result in a variable called <code>fasta_dict</code>. Print the number of keys in this dictionary to screen.

3. In the <code>handin5</code> module, create another function called <code>find_prot</code> that takes a dictionary as first argument, and as second argument takes a protein name (a string). The function should use the provided dictionary to lookup and return the sequence corresponding to the provided name.  If the name is not present in the dictionary, the function should print an error message and return <code>None</code>. The error message should be <code>Error: protein name NAME not found</code>, where NAME is the protein name you are searching for. Make sure to include a docstring.

4. In the <code>handin5_test.py</code> file, call the <code>find_prot</code> function on the protein name <code>YHCN_ECOLI</code>. Save the result to a variable called <code>yhcn</code>.

5. In the <code>handin5_test.py</code> file, call the <code>find_prot</code> function on the protein name <code>BOOM_ECOLI</code>. Save the result to a variable called <code>boom</code>. Note that this case should print an error, since this is not an actual Ecoli protein name.

6. In the <code>handin5</code> module, create a function called <code>find_prot2</code> that takes a dictionary and regular expression (as a string), and returns a list of all of the *keys* in the dictionary that the pattern matches. Make sure to include a docstring.

7. In <code>handin5_test.py</code>, use the <code>find_prot2</code> function to return all the protein names in Ecoli that only consist of three characters before <code>_ECOLI</code> (e.g. <code>EX1_ECOLI</code>). Save the result in a variable called <code>matches</code>". Print the number of matches to screen. 