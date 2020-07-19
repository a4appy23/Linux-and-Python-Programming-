# Handin 2
<table>
  <tr>
    <td>Due date</td>
    <td>Tuesday, Sep 17 </td>
  </tr>
  <tr>
    <td>Format</td>
    <td>Put the relevant commands into the handin2.sh file. The individual exercises should be separated by empty lines (see the "Github, git and the weekly hand-ins" page on Absalon for an example). When you are ready to submit, use the 'git commit -a -m "Submission 1"' command, where you replace "Submission 1" with a brief message explaining how this version of the files differs from the last, (e.g. "Initial submission", "Fixed bug in subquestion 1", etc).</td>
  </tr>
  <tr>
    <td>Setup</td>
    <td><strong>Please make sure that your name and email address have been set up correctly</strong> for <code>git</code>. This is very important, since otherwise you will not receive emails about the correctness of your code (and we cannot see who is who). See the <a href="https://absalon.ku.dk/courses/35880/pages/github-git-and-the-weekly-hand-ins?module_item_id=801269">Github, git and the weekly hand-ins]</a> page for details.
  </tr> 
  <tr>
    <td>Other comments</td>
    <td>The hand-in covers the topics covered in this week of the course. This means that there might be a few things that you won't be able to solve until after the Friday lecture. </td>
  </tr>
</table>  

1. We would like to know the various backgrounds of the students attending the course. So start by writing a Unix command that simply prints this information (e.g. "Biology", "Physics", "Computer Science", ...), and redirects it to a file called background.txt.
2. Next, write a command that downloads the following file
http://people.binf.ku.dk/wb/data/th_en_US_v2.dat
This is a file with synonyms for words in the dictionary.
3. Within this file, search for all lines that contain the word "hacker"
4. Repeat 3), but now include only the lines that start with a "(" character.
5. Repeat 4), but now only include the first result.
6. Repeat 5), but now output the individual synonyms on separate lines (hint: replace the "|" characters in the input with "\n", which means new-line).
7. Repeat 6), but omit the first line in the output (the one that just says "(noun)").
8. Repeat 7), but now add line numbers to the output.
9. Repeat 8), but now save the output to a file called "hacker_output.txt", instead of outputting it to screen.

