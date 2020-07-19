# Handin4

<table>
  <tr>
    <td>Due date</td>
    <td>Tuesday, Oct 1 </td>
  </tr>
  <tr>
    <td>Format</td>
    <td>Unix part: Put the relevant commands into the handin4.sh file. The individual exercises should be separated by empty lines (see the "Github, git and the weekly hand-ins" page on Absalon for an example).
Python part: Put your Python code into the handin4.py file. Note that you no longer have to separate the Python code by whitespace now that you are writing functions.
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

Start by downloading the file:
https://wouterboomsma.github.io/lpp2018/data/experimental_results.txt

## Unix part:

1. Find out how to get the <code>sort</code> command to sort by the second column in a file. Use this to write a command that finds the largest value in the second column of the <code>experimental_results.txt</code> file. Note that the command should just return a single number.

2. Find documentation on the <code>xargs</code> and the <code>du</code> commands (either in the <code>man</code> pages or online). Using this information, construct a unix pipeline that finds all files under the <code>/usr/share/dict</code> directory containing the word "english" (using the <code>find</code> command), calculates the size of each of them, and then sorts the lines so that the largest files appear at the bottom (hint: you might need to use the -n 1 option for xargs). For those of you not using the virtual machine, you will only be able to test this locally if you download two files <code>https://wouterboomsma.github.io/lpp2018/data/british-english</code> and <code>https://wouterboomsma.github.io/lpp2018/data/american-english</code> and put them into your local <code>/usr/share/dict</code> directory. Alternatively, you can just test only on the server.


## Python part:

1. Create a function called <code>read_data</code>, that takes a filename as argument. The function should open the file, and read its contents into a list of list of floats, where the outer list corresponds to the lines of the file, and the inner lists correspond to the columns (that is, convert the strings of each line to a list of two numeric values, and append them to an outer list). The function should return this list. Test the function by calling it on the <code>experimental_results.txt</code> file like this:

<pre><code>list_of_rows = read_data('experimental_results.txt')
print(list_of_rows)
</code></pre>

2. Write a function called <code>calc_averages</code> that takes a list of list of floats as input, and calculates the average value for each column by iterating over the rows. The function should return these two values. Test the function by calling it like this: 

<pre><code>col1_avg, col2_avg = calc_averages(list_of_rows)
print(col1_avg, col2_avg)
</code></pre>

3. Write a function called <code>transpose_data</code> that turns the list of lists around so that it becomes a list of columns, rather than a list of rows. This means that the outer list now has two elements each containing a list of all the values in the corresponding column. In other words, if I want to access the 26th value in the 2nd column, I would now index with [1][25] instead of [25][1].
Hint: Note that these two nested lists are just two different ways of representing the same table of data. Here is a sketch of the two variants:

<p align="center">
   <img src="https://wouterboomsma.github.io/lpp2019/images/list_list_transpose.svg">
</p>

Test the function by calling it like this:

<pre><code>list_of_columns = transpose_data(list_of_rows)
print(list_of_columns)    
</code></pre>

**Remember to add doc-strings to all your functions! If you forget, the tests will not pass.**